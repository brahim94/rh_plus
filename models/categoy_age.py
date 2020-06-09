# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class categoryageinhe(models.Model):
    _inherit = "hr.employee"

    profile = fields.Char(string='Profile')

class categoryage(models.Model):
    _name = "category.age"
    #_rec_name = "age"

    #name_cate = fields.Char(string="nom category")
    date_birth = fields.Date(string="Date de naissance")
    #age = fields.Char(compute="_cal_age", string="Age")
    age = fields.Integer(string='Age', compute="_cal_age", search='_value_search', stored=True)
    category_id = fields.Many2one('categ.age', "Categorie d'age")
    name_test = fields.Char(related='category_id.name')
    etat = fields.Selection([ ('type1', 'Stagiaire'),('type2', 'Titulaire'),('type3', 'Retraité '),('type4', 'Démissionné'),('type5', 'Décédé'),],'Etat', default='type2')
    #@api.onchange('age')
    #def onchange_age(self):
        #self.category_id.name = 'type2' if self.age < 20 else 'type3'
    #@api.depends('age')
    #def set_age_group(self):
        #if self.age < 18:
            #self.name_test = 'Majeur'
        #else:
            #self.name_test = 'Mineur'

    @api.depends('date_birth')
    def _cal_age(self):
        for rec in self:
            rec.years = relativedelta(date.today(), rec.date_birth).years
            rec.age = rec.years
    
    def _value_search(self, operator, value):
        recs = self.search([]).filtered(lambda x : x.age is True )
        if recs:
            return [('id', 'in', [x.id for x in recs])]


class cat_age(models.Model):
    _name = "categ.age"
    _description = "Catégorie d'age"

    name = fields.Char(string="Nom de catégorie", store=True, readonly=False)
    #_sql_constraints = [        
    #('name_uniq',
    #    'UNIQUE (name)',
    #    'name corp must be unique.')
    #]
    begin_age = fields.Integer(string="Age de début")
    final_age = fields.Integer(string="Age Fin")

    

    
