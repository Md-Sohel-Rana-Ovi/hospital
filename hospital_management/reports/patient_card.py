# # -*- coding: utf-8 -*-

from odoo import models, fields, api


class PatientCardReport(models.AbstractModel):
    _name = 'report.hospital_management.report_patient'
    _description = 'Patient card Record'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("yes  intered here in the function")
        print("docids",docids)
        # model=self.env.context.get('active_mode')
        docs=self.env['hospital.patient'].browse(docids[0])
        appointments=self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list=[]
        for app in appointments:
            vals={
                'name': app.name,
                'notes': app.notes,
                'appointment_date': app.appointment_date
            }
            appointment_list.append(vals)
        print('appointments',appointments)
        print('appointment_list',appointment_list)

        # docids: pass from the wizard print button.
        # records = self.env[objectname].browse(docids)
        return {
            'doc_model': 'hospital.patient',
            'docs': docs,
            'data': data,
            'appointment_list': appointment_list,
        }



