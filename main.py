from flask import Flask, Response, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Create a flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key"


class NamerForm(FlaskForm):
    name = StringField("Whats your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    # In your templates directory, create a mobile version of your site (mobile.index.html).
    # Likewise, add your desired desktop template as well (desktop.index.html).

    if "iphone" in user_agent:
        return render_template('mobile.index.html')
    elif "android" in user_agent:
        return render_template('mobile.index.html')
    else:
        return render_template('desktop.index.html')


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully")
    return render_template('name.html', name=name, form=form)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/my-journey')
def my_journey():
    return render_template('myDiabetesjourney.html')


if __name__ == '__main__':
    app.run(debug=True)

