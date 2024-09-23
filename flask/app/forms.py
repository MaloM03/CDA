from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#=================================================================
class ConfigForm(FlaskForm):
    odoo_addr = StringField('Odoo @IP', validators=[DataRequired()])
    odoo_port = StringField('Odoo port', validators=[DataRequired()])
    submit = SubmitField('Submit')
