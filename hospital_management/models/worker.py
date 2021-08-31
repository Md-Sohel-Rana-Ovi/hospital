from odoo import models, fields, api



class hospital_worker(models.Model):
    _name = 'hospital.worker'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'worker record'
    _rec_name = 'worker_name'


    worker_name = fields.Char(string='Name',required=True,track_visibility="always")
    worker_age = fields.Integer('Age',track_visibility="always")
    worker_address = fields.Text(string='Address')
    phone=fields.Char(string='Phone Number',required=True)
    images = fields.Binary(string='Image')
    worker_seq = fields.Char(string='Worker ID', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: ('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')


    @api.model
    def create(self, vals):
        if vals.get('worker_seq', ('New')) == ('New'):
            vals['worker_seq'] = self.env['ir.sequence'].next_by_code('hospital.worker.sequence') or ('New')

        result = super(hospital_worker, self).create(vals)
        return result

