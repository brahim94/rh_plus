# -*- coding: utf-8 -*-

from odoo import models, fields, api

class certificationsorder(models.Model):
    _name = "certificat.order"
    _inherit = ['mail.thread', 'mail.activity.mixin','portal.mixin','utm.mixin' ]

    #name = fields.Char('Attestation')
    type_attestation = fields.Selection([
            ('job', 'Attestation de travail'),
            ('salary', 'Attestation de salaire '),
            ('domiciliation', 'Domiciliation'),
            ('leave', 'Attestation de congé'),
            ('work', 'Certificats de  travail'),
            ('notify', 'Notification de départ'),
            ], setting='Type Attestation', default='job')
    name = fields.Char(string='Certifica Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    name_sal = fields.Char(string='Certifica salary Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    company_id = fields.Many2one(
    'res.company',
    'Company',
    default=lambda self: self.env['res.company']._company_default_get('attestation')
    )
    cnss_number = fields.Char(string='C.N.S.S. N°')
    write_date = fields.Date(string='Write Date')
    demand_date = fields.Datetime(string="Date demande")
    send_date = fields.Datetime(string="Date envoi")
    employee_id = fields.Many2one('hr.employee', string="Employee")
    email_id = fields.Char(string="Email")
    date_hire = fields.Date(string="Date d'embauche")
    state = fields.Selection([
        ('brouillon', 'Nouveau'),
        ('valide', 'Validé'),
        ('envoyer', 'Envoyé'),
        ], setting='State', readonly=True, default='brouillon')
    amount_money = fields.Char(string='Salaire brut en Dh')
    salary_date_create = fields.Date(string="Date de paye")
    months_number = fields.Integer(string='N° Mois')
    name_bank = fields.Char(string='Banque')
    name_agency = fields.Char(string='Agence')
    rib_number = fields.Char(string='N° RIB')
    leave_date_start = fields.Date(string="Début de congé")
    leave_date_end = fields.Date(string="Fin de congé")
    date_leave = fields.Date(string="Date de départ")
    cin_number = fields.Char(string='CIN N°')

    def _get_default_contrat(self):
        return self.env['hr.contract'].search([], limit=1).id

    contrat = fields.Many2one('hr.contract', string='Contrat', default=_get_default_contrat, domain=[])
    
    @api.onchange('employee_id')
    def onchange_contrat_id(self):
        self.contrat = self.employee_id.contract_id 

    def _get_default_job(self): 
        return self.env['hr.job'].search([], limit=1).id

    fiche_poste = fields.Many2one('hr.job', string='Fiche de poste', default=_get_default_job, domain=[])
    
    @api.onchange('employee_id')
    def onchange_id(self):
        self.fiche_poste = self.employee_id.job_id
    
    @api.onchange('employee_id')
    def onchange_email_id(self):
        self.email_id = self.employee_id.work_email
    #def _get_default_hire(self):
        #return self.env['hr.contract'].search([('name', '=', 'date_start')], limit=1).id

    #date_hire = fields.Many2one('hr.contract', string="date d'embauche", default=_get_default_hire, domain=[('name', '=', 'date_start')])
    
    @api.onchange('employee_id')
    def onchange_hire_id(self):
        self.date_hire = self.contrat.date_start 
    
    def _get_default_manager(self):
        return self.env['hr.employee'].search([('name', '=', 'parent_id')], limit=1).id

    manager = fields.Many2one('hr.employee', string='Manager', default=_get_default_manager, domain=[('name', '=', 'parent_id')])
    
    @api.onchange('employee_id')
    def onchange_manager(self):
        self.manager = self.employee_id.parent_id
    
    @api.onchange('employee_id')
    def onchange_wage_id(self):
        self.amount_money = self.contrat.wage

    @api.model 
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('job.order') or ('New')
        result = super(certificationsorder, self).create(vals)
        return result
    
    @api.model 
    def create_sal(self, vals):
        if vals.get('name_sal', ('New')) == ('New'):
            vals['name_sal'] = self.env['ir.sequence'].next_by_code('salary.order') or ('New')
        result_sal = super(certificationsorder, self).create_sal(vals)
        return result 

    def action_validate(self):
        for rec in self:
            rec.state = 'valide'
    
    def print_job(self):
        return self.env.ref('rh_plus.action_report_job').report_action(self)
    
    def send_job_certifica(self):
        template_id = self.env.ref('rh_plus.job_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer'
    
    def action_validate_salary(self):
        for rec in self:
            rec.state = 'valide'

    def print_salary(self):
        return self.env.ref('rh_plus.action_report_salary').report_action(self)

    def send_salary_certifica(self):
        template_id = self.env.ref('rh_plus.salary_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer'

    def action_validate_domiciliation(self):
        for rec in self:
            rec.state = 'valide'

    def print_domiciliation(self):
        return self.env.ref('rh_plus.action_report_domiciliation').report_action(self)

    def send_domiciliation_certifica(self):
        template_id = self.env.ref('rh_plus.domiciliation_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer'

    def action_validate_leave(self):
        for rec in self:
            rec.state = 'valide'

    def print_leave(self):
        return self.env.ref('rh_plus.action_report_leave').report_action(self)

    def send_leave_certifica(self):
        template_id = self.env.ref('rh_plus.leave_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer' 
    
    def action_validate_work(self):
        for rec in self:
            rec.state = 'valide'

    def print_work(self):
        return self.env.ref('rh_plus.action_report_work').report_action(self)

    def send_work_certifica(self):
        template_id = self.env.ref('rh_plus.work_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer'  

    def action_validate_notify(self):
        for rec in self:
            rec.state = 'valide'

    def print_notify(self):
        return self.env.ref('rh_plus.action_report_notify').report_action(self)

    def send_notify_certifica(self):
        template_id = self.env.ref('rh_plus.notify_certifica_email_template').id 
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        self.state = 'envoyer'