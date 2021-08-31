# -*- coding: utf-8 -*-
{
    'name': "Hospital_Management",
    'version':'13.0.1.0.0',

    'summary': """
        Module for managing the Hospital""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends' : ['mail'],
    'depends' : ['sale'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/data.xml',
        'data/mail_template.xml',
        'data/cron.xml',
        'wizards/create_appointment.xml',
        'views/doctor.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/worker.xml',
        'views/lab.xml',
        'reports/patient_card.xml',
        'reports/report.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
