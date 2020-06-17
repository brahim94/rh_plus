from odoo import models, fields, api


class salary(models.Model):
    _name = "hr.salary"

    month = fields.Selection([('1', 'Janvier'), ('2', 'Février'), ('3', 'Mars'), ('4', 'Avril'),('5', 'Mai'), ('6', 'Juin'), ('7', 'Juillet'), ('8', 'Aout'),('9', 'Septembre'), ('10', 'Octobre'), ('11', 'Novembre'), ('12', 'Decembre'), ],'Mois', default='1')
    year = fields.Char('Année')
    employee_id = fields.Many2one('hr.employee', string="Employee")
    registration = fields.Char('Matricule')
    date_salary = fields.Date('Date salaire')
    salary_amount = fields.Float('salaire brut')
    file1 = fields.Binary("Importation salaire")
    importation_salaire = fields.Char('Importation')