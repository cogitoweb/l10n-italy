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
            ('to_register', 'To register'),
        ],
        string='State',
        readonly=True
    )
    total_fatturapa_in = fields.Integer(readonly=True)
    total_fatturapa_in_current_month = fields.Integer(readonly=True)
    total_fatturapa_in_current_year = fields.Integer(readonly=True)

    color = fields.Char(readonly=True)
    icon = fields.Char(readonly=True)

    # filter method
    @api.multi
    def action_open_view_state(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        ctx.update({
            'search_default_' + self.state: True
        })
        action = self.env.ref('l10n_it_fatturapa_in.action_fattura_pa_in').read()[0]
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
                SELECT FALSE AS registered
                UNION
                SELECT TRUE as registered
            )
			SELECT
                CASE
            		WHEN s.registered = FALSE THEN 1
            		WHEN s.registered = TRUE THEN 2
            		ELSE 0
            	END AS id,
            	CASE
            		WHEN s.registered = FALSE THEN 'to_register'
            		WHEN s.registered = TRUE THEN 'registered'
            	END AS state,
                coalesce(count(fai.registered), 0) AS total_fatturapa_in,
                coalesce(sum(CASE WHEN fai.create_date >= date_trunc('month', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_in_current_month,
               	coalesce(sum(CASE WHEN fai.create_date >= date_trunc('year', now()) THEN 1 ELSE 0 END), 0) AS total_fatturapa_in_current_year,
                CASE
            	    WHEN s.registered = FALSE THEN '#99ccff'
            	    WHEN s.registered = TRUE THEN '#33cc33'
            	END AS color,
                CASE
            	    WHEN s.registered = FALSE THEN 'fa fa-check-circle-o fa-2x'
            	    WHEN s.registered = TRUE THEN 'fa fa-check-circle fa-2x'
            	END AS icon
            FROM
            	states s
            LEFT JOIN fatturapa_attachment_in fai ON fai.registered = s.registered
            GROUP BY
            	s.registered
            ORDER by
            	id
        """

        self.env.cr.execute(_sql_view, {'table': AsIs(view_name)})
