# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# import datetime


class hospital_management(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'patient record'
    _rec_name = 'patient_name'

    @api.model
    def test_cron_job(self):
        print('abcd')
        # code acordingly to excute the cron

    # def name_get(self):
    #     rec=[]
    #     for record in self:
    #         result=record.append((rec.id,'%s %s' % (record.name_seq,record.patient_name)))
    #     return result

    def action_send_card(self):
        template_id = self.env.ref('hospital_management.patient_card_email_template').id
        template= self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    # # ValidationError Message
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <=5:
                raise ValidationError("The Age must be Grater than 5.")

    # # Major & Minor Grouping
    @api.depends('patient_age')
    def set_of_group(self):
        for rec in self:
            if rec.patient_age < 18:
                rec.age_group='minor'
            else:
                rec.age_group='major'
    #        #smart_button add
    def open_patient_appointment(self):
        return {
            'name': ('appointment'),
            'domain': [('patient_id', '=', self.id)],
            'views_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',

        }
    def set_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count=count


    name = fields.Char(string='Contact Number')
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))
    gender=fields.Selection([
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ],string='Gender',default='male')
    age_group=fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ],string='Age Group',compute='set_of_group')
    patient_name = fields.Char(string='Name',required=True,track_visibility="always")
    patient_age = fields.Integer('Age', track_visibility="always")
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    notes = fields.Text(string=' Registration Notes')
    images = fields.Binary(string='Image')
    appointment_count=fields.Integer(string='Appointment',compute='set_appointment_count')
    active=fields.Boolean("Active", default="True")
    user_id = fields.Many2one('res.users', string='Pro')
    email_id = fields.Char(string=' Email')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)


    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or ('New')
        result = super(hospital_management, self).create(vals)
        return result





    # @api.model
    # def create(self, vals):
    #     if vals.get('name_seq', ('New')) == ('New'):
    #         vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or ('New')
    #         patient = self.env['hospital.appointment'].search([('appointment_date', '<', datetime.now()), ('appointment_date', '>', datetime.now())])
    #         vals['appointment_time'] = "datetime.now() + timedelta(mins=9)"
    #     result = super(hospital_management, self).create(vals)
    #     return result

