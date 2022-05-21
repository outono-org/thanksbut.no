from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField
from wtforms.validators import DataRequired, Email

load_dotenv()
app = Flask(__name__)


# TODO: Move class to another config.py file
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # PyMongo Configuration
    app.config["MONGO_URI"] = os.environ.get("MONGODB_URI")
    mongo = PyMongo(app)


app.config.from_object(Config)

# Start of Forms
# TODO: Move forms to another forms.py file


class SubscribeForm(FlaskForm):
    email = EmailField(validators=[Email(), DataRequired()])
    submit = SubmitField('Join the party')

# Start of Views


@app.route("/", methods=['GET', 'POST'])
def home():

    db = Config.mongo.db

    form = SubscribeForm()
    email = form.email.data

    if form.validate_on_submit():
        db.subscribers.insert_one(
            {"email": email})
        # TODO: Create module to replace form.

    return render_template('index.html', form=form, email=email)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
