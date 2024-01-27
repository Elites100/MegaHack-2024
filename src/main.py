from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators, TextAreaField
from wtforms.validators import DataRequired,  ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


# making sure the selectfield is selected
def validate_option(form, field):
    if field.data == 'choose':
        raise ValidationError('Please select a option')

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[validators.DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[validators.DataRequired()])
    instructions = TextAreaField('Instructions', validators=[validators.DataRequired()])
    submit = SubmitField('Submit Recipe')
    

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Main webpage which is the form
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = RecipeForm()
    if form.validate_on_submit():
        form.vNumber.data= ''
        form.name.data = ''
        form.email.data = ''
        form.SN.data = ''
        form.CRN.data = ''
        form.addtionalComment.data = ''
        flash('The course override has been submitted', 'success')
    return render_template('index.html', form=form, name=name)

# Infomation page about the form
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# Used to run the application
if __name__ == '__main__':
    app.run(debug=True)