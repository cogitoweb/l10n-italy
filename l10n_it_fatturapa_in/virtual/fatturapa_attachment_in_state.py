# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools

from psycopg2.extensions import AsIs


class VirtualFatturaPAAttachmentInState(models.Model):

    _name = 'virtual.fatturapa.attachment.in.state'
    _auto = False

    # fields
    state = fields.Selection(
        [
            ('registered', 'Registered'),
            ('not_registered', 'Not registered'),
        ],
        string='State',
        readonly=True
    )
    total_fatturapa_in = fields.Integer(readonly=True)
    total_fatturapa_in_current_month = fields.Integer(readonly=True)
    total_fatturapa_in_current_year = fields.Integer(readonly=True)

    # filter methods
    @api.multi
    def action_open_view_state(self):
        self.ensure_one()
        action = self.env.ref('l10n_it_fatturapa_in.action_fatturapa_attachment').read()[0]
        action['context'] = {'search_default_' + self.state: True}
        return action

    @api.multi
    def action_open_view_state_current_month(self):
        self.ensure_one()
        action = self.env.ref('l10n_it_fatturapa_in.action_fatturapa_attachment').read()[0]
        action['context'] = {'search_default_' + self.state: True, 'search_default_current_month': True}
        return action

    @api.multi
    def action_open_view_state_current_year(self):
        self.ensure_one()
        action = self.env.ref('l10n_it_fatturapa_in.action_fatturapa_attachment').read()[0]
        action['context'] = {'search_default_' + self.state: True, 'search_default_current_year': True}
        return action

    # This is executed on every module update
    @api.model_cr
    def init(self):
        view_name = 'public.' + self._table
        tools.drop_view_if_exists(self.env.cr, view_name)

        _sql_view = """
            CREATE OR REPLACE VIEW %(table)s AS
            SELECT
            	CASE
            		WHEN fai.registered = FALSE THEN 'not_registered'
            		WHEN fai.registered = TRUE THEN 'registered'
            	END AS state,
                coalesce(count(fai.registered), 0) AS total_fatturapa_in,
                coalesce(sum(CASE WHEN fai.create_date >= date_trunc('month', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_in_current_month,
               	coalesce(sum(CASE WHEN fai.create_date >= date_trunc('year', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_in_current_year,
               	CASE
            		WHEN fai.registered = FALSE THEN 1
            		WHEN fai.registered = TRUE THEN 2
            		ELSE 0
            	END AS id
            FROM
            	fatturapa_attachment_in fai
            GROUP BY
            	fai.registered
            ORDER by
            	id
        """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
