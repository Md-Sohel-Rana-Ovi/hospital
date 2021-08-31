from odoo import models, fields, api



class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'


    patient_id=fields.Many2one('hospital.patient', string='Patient')
    appointment_date=fields.Date(string='Appointment Date')

    def create_appointment(self):
        vals={
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date
        }
        self.patient_id.message_post(body='Appointment Created Successfully',subject='Appointment Creation')
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("Get Data Function")
        appointments=self.env["hospital.appointment"].search([('patient_id', '=', 6)])
        for rec in appointments:
            print("Appointment Name",rec.name)


