from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'appointment record'
    _order = 'appointment_date desc'

    def delete_lines(self):
        for rec in self:
            print("rec", rec)
            rec.appointment_lines=[(5,0,0)]


    def action_confirm(self):
        for rec in self:
            rec.state='confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    # Id sequence
    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or ('New')
        result = super( HospitalAppointment, self).create(vals)
        return result

    # Override Write Function in Odoo
    def write(self, vals):
        res=super(HospitalAppointment, self).write(vals)
        print("Test write functon")
        return res

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))

    patient_id=fields.Many2one('hospital.patient',string='Patient',required=True)
    patient_age = fields.Integer('Age',related="patient_id.patient_age")
    notes = fields.Text(string=' Registration Notes')
    doctor_note = fields.Text(string=' Note')
    pharmacy_note = fields.Text(string=' Note')
    appointment_date=fields.Date(string='Date')
    appointment_lines=fields.One2many('hospital.appointment.lines', 'appointment_id',string="Appointment Lines")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, default='draft')


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id=fields.Many2one('product.product',string="Medicine")
    product_qty=fields.Integer(string="Quantity")
    appointment_id=fields.Many2one('hospital.appointment',string="Appointment ID")

