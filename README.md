## Getting Started

**_Prerequisites: Python 3.9.0._**

```shell script
$ git clone https://github.com/outono-org/thanksbut.no.git

$ cd startup-jobs

$ python3 -m venv venv              # Create a virtual environment.

$ source venv/bin/activate          # Activate your virtual environment.

$ pip install -r requirements.txt   # Install project requirements.

$ cd application/

$ export FLASK_APP=app.py

$ export FLASK_ENV=development      # Enable hot reloading, debug mode.

$ flask run
```

## Setting up the database

Create a `.env` file in the root directory of your project and connect the app to a MongoDB atlas cluster.
