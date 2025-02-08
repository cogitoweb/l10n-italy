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
    total_fatturapa_out_actual_month = fields.Integer(readonly=True)

    @api.multi
    def _get_action(self, action_xmlid):
        action = self.env.ref(action_xmlid).read()[0]
        if self:
            action['display_name'] = self.display_name
        return action

    # filter methods
    @api.multi
    def get_action_fatturapa_current_month_tree(self):
        """ extra action to filter on dashboard """
        return self._get_action('l10n_it_fatturapa_pec.action_fatturapa_current_month_tree')

    @api.multi
    def get_action_fatturapa_current_year_tree(self):
        """ extra action to filter on dashboard """
        return self._get_action('l10n_it_fatturapa_pec.action_fatturapa_current_year_tree')

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
                s.state,
                coalesce(count(fao.state), 0) AS total_fatturapa_out,
                coalesce(sum(CASE WHEN fao.create_date >= date_trunc('month', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_out_actual_month,
                CASE
            	    WHEN s.state = 'ready' THEN 1
            	    WHEN s.state = 'sent' THEN 2
            	    WHEN s.state = 'sender_error' THEN 3
            	    WHEN s.state = 'recipient_error' THEN 4
            	    WHEN s.state = 'rejected' THEN 5
            	    WHEN s.state = 'validated' THEN 6
            	    WHEN s.state = 'accepted' THEN 7
            	    ELSE 0
            	END AS id
            FROM
                states s
            LEFT JOIN fatturapa_attachment_out fao ON fao.state = s.state
            GROUP BY
                s.state
            ORDER BY
                id
        """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
