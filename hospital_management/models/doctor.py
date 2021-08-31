from odoo import models, fields, api
from odoo.exceptions import ValidationError


class hospital_doctor(models.Model):
    _name = 'hospital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'doctor record'
    _rec_name = 'doctor_name'

    # @api.onchange('Objervation_time')
    # def compute_time(self):
    #     if self.Objervation_time:
    #         self.beschreibung = str(now) + '\n' + str(self.beschreibung)
    #     else:
    #         self.beschreibung = ' '

    # ValidationError Message
    @api.constrains('doctor_age')
    def check_age(self):
        for rec in self:
            if rec.doctor_age <= 15:
                raise ValidationError("The Age must be Grater than 15.")

    doctor_name = fields.Char(string='Name',required=True,track_visibility="always")
    doctor_age = fields.Integer('Age',track_visibility="always")
    title = fields.Text(string='Title')
    phone=fields.Char(string='Phone Number',required=True)
    images = fields.Binary(string='Image')
    diease_specialist=fields.Text(string='Specialist')
    doctor_chamber = fields.Text(string=' Chamber')
    room = fields.Integer(string='Rooms')
    date_from = fields.Datetime(string="From")
    date_to= fields.Datetime(string="TO")
    checkup_time = fields.Char(string='Checkup Time',default='15min')

    # Objervation_time = fields.Float(string='Time',compute="compute_time")
    name_seq = fields.Char(string='Doctor ID', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))
    user_id=fields.Many2one('res.users',string='Related User')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')


    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or ('New')

        result = super(hospital_doctor, self).create(vals)
        return result

