# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools

from psycopg2.extensions import AsIs


class VirtualFatturaPAAttachmentOutState(models.Model):

    _name = 'virtual.fatturapa.attachment.out.state'
    _auto = False

    # fields
    state = fields.Char(readonly=True)
    total_fatturapa_out = fields.Integer(readonly=True)

    # This is executed on every module update
    @api.model_cr
    def init(self):
        view_name = 'public.' + self._table
        tools.drop_view_if_exists(self.env.cr, view_name)

        _sql_view = """
            CREATE OR REPLACE VIEW %(table)s AS
            WITH states AS (
                SELECT 'ready' AS state
                UNION
                SELECT 'sent'
                UNION
                SELECT 'sender_error'
                UNION
                SELECT 'recipient_error'
                UNION
                SELECT 'rejected'
                UNION
                SELECT 'validated'
                UNION
                SELECT 'accepted'
            )
            SELECT
                row_number() over() AS id,
                s.state,
                coalesce(count(fao.state), 0) AS total_fatturapa_out
            FROM
                states s
            LEFT JOIN fatturapa_attachment_out fao ON fao.state = s.state
            AND
                fao.create_date < date_trunc('month', now()) AND fao.create_date < date_trunc('month', now()) + '1 month'::interval
            GROUP BY
                s.state
            ORDER BY
                s.state
        """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
