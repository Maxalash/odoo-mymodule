# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string ='title', required=True)
    description = fields.Text()
    state = fields.Selection([
      ('on_going', 'On going'),
      ('stopped', 'Stopped')
    ], required=True, default='stopped')
    instructor_id = fields.Many2one('openacademy.instructor', 
        string="Instructor")


class Instructor(models.Model):
    _name = 'openacademy.instructor'
    _description = 'Open Academy instructor'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    image = fields.Binary(string="Image")



