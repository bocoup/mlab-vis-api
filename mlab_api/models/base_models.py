# -*- coding: utf-8 -*-
from flask_restplus import fields
from mlab_api.rest_api import api

# ---
# Base Models
# ---
base_meta_fields = api.model('Base Meta', {
    'client_continent': fields.String(description="Parent continent of Location."),
    'client_country': fields.String(description="Parent country of Location."),
    'client_region': fields.String(description="Parent region of Location."),
    'client_city': fields.String(description="Name of city, if location is a city.")
})


search_data_fields = api.model('Search Data', {
    'last_three_month_test_count': fields.Integer(description="Test counts over last 3 months."),
    'test_count': fields.Integer(description="Test counts over entire MLab dataset")
})
