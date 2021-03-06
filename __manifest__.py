# -*- coding: utf-8 -*-
{
    'name': "rh_plus",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/category_age.xml',
        'report/job_report.xml',
        'report/salary_report.xml',
        'report/domiciliation_report.xml',
        'report/leave_report.xml',
        'report/work_report.xml',
        'report/notify_report.xml',
        'data/mail_template.xml',
        'data/sequence.xml',
        'views/salary.xml',
        'views/certifications.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
