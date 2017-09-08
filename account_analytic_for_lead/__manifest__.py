# -*- coding: utf-8 -*-
{
    'name': "Account analytic for lead",

    'summary': """
        Account analytic for lead""",

    'author': "Telematel",
    'website': "http://www.telematel.com",

    'category': 'Project',
    'version': '10.1.0.0',
    'license': 'AGPL-3',

    'depends': [
        'account_accountant',
        'crm'
    ],

    'data': [
        'views/inherit_crm_lead_views.xml',
    ],

    'demo': [
    ],
}
