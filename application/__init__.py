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
    submit = SubmitField('Stay Tuned')

# Start of Views


db = Config.mongo.db


@app.get("/")
def home():
    form = SubscribeForm()
    questions = [
        "What if we didn't have to work to afford living?",
        "What if there were new and more engaging ways of expressing ourselves?",
        "What if schools let kids follow their own curiosity and learning path?",
        "What if women didn't have to carry a baby in their womb?",
        "What if could live for 200 years?",
        "What if we could provide clean and affordable energy for everyone?",
        "What if we could communicate with anyone fluently without having to learn another language?",
        "What if we could connect in more meaningful ways?",
        "What if we could get from Tokyo to Madrid in 4 hours?",
        "What if we could make any drink from our kitchen?",
        "What if we could breathe underwater without any equipment?",
        "What if we could make beautiful cities again?",
        "What if we didn't need cars to commute?"
    ]

    return render_template('index.html', form=form, questions=questions)


@app.get("/who")
def who():
    return render_template('who.html')


@app.get("/wall")
def wall():
    return render_template('wall.html')


@app.post("/subscribe")
def subscribe():
    form = SubscribeForm()
    email = form.email.data

    if form.validate_on_submit():
        db.subscribers.insert_one(
            {"email": email})
        return thankyou()


@app.get("/thankyou")
def thankyou():
    return render_template('fragments/thankyou.html')
