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
            SELECT
                ROW_NUMBER() OVER() AS id,
                state,
                count(*) as total_fatturapa_out
            FROM
                fatturapa_attachment_out fao
            WHERE
                create_date >= date_trunc('month', now()) AND create_date < date_trunc('month', now()) + '1 month'::interval
            GROUP BY
                state
        """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
