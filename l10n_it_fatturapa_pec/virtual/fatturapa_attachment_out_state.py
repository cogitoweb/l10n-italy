# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools

from psycopg2.extensions import AsIs


class VirtualFatturaPAAttachmentOutState(models.Model):

    _name = 'virtual.fatturapa.attachment.out.state'
    _auto = False

    # fields
    state = fields.Selection(
        [
            ('ready', 'Ready to Send'),
            ('sent', 'Sent'),
            ('sender_error', 'Sender Error'),
            ('recipient_error', 'Not delivered'),
            ('rejected', 'Rejected (PA)'),
            ('validated', 'Delivered'),
            ('accepted', 'Accepted'),
        ],
        string='State',
        readonly=True
    )
    total_fatturapa_out = fields.Integer(readonly=True)
    total_fatturapa_out_current_month = fields.Integer(readonly=True)
    total_fatturapa_out_current_year = fields.Integer(readonly=True)

    color = fields.Char(readonly=True)
    icon1 = fields.Char(readonly=True)
    icon2 = fields.Char(readonly=True)

    # filter method
    @api.multi
    def action_open_view_state(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        ctx.update({
            'search_default_' + self.state: True
        })
        action = self.env.ref('l10n_it_fatturapa_out.action_fatturapa_attachment').read()[0]
        action['context'] = ctx
        return action

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
                CASE
            	    WHEN s.state = 'ready' THEN 1
            	    WHEN s.state = 'sent' THEN 2
            	    WHEN s.state = 'sender_error' THEN 3
            	    WHEN s.state = 'recipient_error' THEN 4
            	    WHEN s.state = 'rejected' THEN 5
            	    WHEN s.state = 'validated' THEN 6
            	    WHEN s.state = 'accepted' THEN 7
            	    ELSE 0
            	END AS id,
                s.state,
                coalesce(count(fao.state), 0) AS total_fatturapa_out,
                coalesce(sum(CASE WHEN fao.create_date >= date_trunc('month', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_out_current_month,
                coalesce(sum(CASE WHEN fao.create_date >= date_trunc('year', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_out_current_year,
            	CASE
            	    WHEN s.state = 'ready' THEN '#99ccff'
            	    WHEN s.state = 'sent' THEN '#6699ff'
            	    WHEN s.state = 'sender_error' THEN '#ffff99'
            	    WHEN s.state = 'recipient_error' THEN '#ffff99'
            	    WHEN s.state = 'rejected' THEN '#ff9999'
            	    WHEN s.state = 'validated' THEN '#99ff99'
            	    WHEN s.state = 'accepted' THEN '#33cc33'
            	END AS color,
            	CASE
            	    WHEN s.state = 'ready' THEN 'fa fa-paper-plane-o fa-2x'
            	    WHEN s.state = 'sent' THEN 'fa fa-paper-plane fa-2x'
            	    WHEN s.state = 'sender_error' THEN 'fa fa-bug fa-2x'
            	    WHEN s.state = 'recipient_error' THEN 'fa fa-bug fa-2x'
            	    WHEN s.state = 'rejected' THEN 'fa fa-times fa-2x'
            	    WHEN s.state = 'validated' THEN 'fa fa-check-circle-o fa-2x'
            	    WHEN s.state = 'accepted' THEN 'fa fa-check-circle fa-2x'
            	END AS icon1,
            	CASE
            	    WHEN s.state = 'sender_error' THEN 'fa fa-level-up fa-2x'
            	    WHEN s.state = 'recipient_error' THEN 'fa fa-level-down fa-2x'
            	    WHEN s.state = 'validated' THEN 'fa fa-level-down fa-2x'
            	    else ''
            	END AS icon2
            FROM
                states s
            LEFT JOIN fatturapa_attachment_out fao ON fao.state = s.state
            GROUP BY
                s.state
            ORDER BY
                id
            """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
