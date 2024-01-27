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

def validate_option(form, field):
    if field.data == 'choose':
        raise ValidationError('Please select an option.')

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    cuisine_type = SelectField('Cuisine Type', choices=[
        ('choose', 'Choose'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('indian', 'Indian'),
        ('chinese', 'Chinese'),
        # Add more cuisine types as needed
    ], default='choose', validators=[validate_option])
    meal_type = SelectField('Meal Type', choices=[
        ('choose', 'Choose'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        # Add more meal types as needed
    ], default='choose', validators=[validate_option])
    prep_time = StringField('Preparation Time (e.g., 30 minutes)', validators=[DataRequired()])
    cook_time = StringField('Cooking Time (e.g., 1 hour)', validators=[DataRequired()])
    servings = StringField('Number of Servings', validators=[DataRequired()])
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
    # Here, you can process the form data, save it to a database, etc.
    flash('Recipe submitted successfully!', 'success')
    # Clear the form data after submission
    form.recipe_name.data = ''
    form.ingredients.data = ''
    form.instructions.data = ''
    form.prep_time.data = ''
    form.cook_time.data = ''
    form.servings.data = ''
  return render_template('index.html', form=form, name=name)

# Infomation page about the form
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


# Used to run the application
if __name__ == '__main__':
    app.run(debug=True)