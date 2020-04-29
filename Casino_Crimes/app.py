# Import dependecies


import os
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

import decimal
import datetime
def decoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL', '') or "sqlite:///Casino.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)
engine = create_engine("sqlite:///casino.sqlite", encoding = "utf8")
conn = engine.connect()
session = Session(engine)

# Save reference to the table
Keys = Base.classes.keys

casinoSW = Base.classes.casinoSW


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Return the homepage."""
    return render_template("index.html")
#     return(
#         f"(Project II - Step 2 Flask App). <br><br>"
#         f"Available Routes: <br>"

#         f"/api/v1.0/data<br/>"
#         f"Returns data in data set. <br><br>"

#         f"/api/v1.0/industry<br/>"
#         f"Returns a list of casino types. <br><br>"

#         f"/api/v1.0/states<br/>"
#         f"Returns list of states  in data set. <br><br>"

#         f"/api/v1.0/county<br/>"
#         f"Returns data by counties.<br><br>"

#         f"/api/v1.0/Suspicious Activity<br/>"
#         f"Returns top of Suspicious activities by states.<br><br>"
#    )


@app.route("/api/casinos")
def casinos():
    """Visit data."""
    # return render_template("data.html")

    # Create our session (link) from Python to the DB

    # Query all Casino DB
    results = db.session.query(casinoSW.id, casinoSW.Year, casinoSW.State, casinoSW.Countym,  casinoSW.Industry, casinoSW.Activity, casinoSW.Count, casinoSW.Lat, casinoSW.Long).all()
    data = []
    for a, b, c, d, e, f, g, h, i in results:
        entry = {
            "id": a,
            "year": b,
            "state": c,
            "countym": d,
            "industry": e,
            "activity": f,
            "count": g,
            "lat": decoder(h),
            "long": decoder(i)
            
        }
        data.append(entry)

    final_results = {"data": data}
    return jsonify(data)


# @app.route("/industry")
# def industryType():
#     """Return a list fo types of industry with their number for each state"""
#     session = Session(engine)
#     casino_types = session.query(casinoSW.Industry, casinoSW.State, casinoSW.Year, str(casinoSW.Lat), str(casinoSW.Long), func.sum(casinoSW.Count)).\
#         group_by(casinoSW.Industry, casinoSW.State, casinoSW.Year).order_by(func.sum(casinoSW.Count).desc()).all()
#     session.close()
#     return jsonify(casino_types)

# @app.route("/states")
# def states():
#     session = Session(engine)
#     state_data = session.query(casinoSW.State, casinoSW.Industry, casinoSW.Year, str(casinoSW.Lat), str(casinoSW.Long), func.sum(casinoSW.Count)).\
#         group_by(casinoSW.State, casinoSW.Industry, casinoSW.Year).order_by(func.sum(casinoSW.Count).desc()).all()
#     session.close()
#     return jsonify(state_data)


# @app.route("/county")
# def counties():
#     session = Session(engine)
#     county_data = session.query(casinoSW.Countym, casinoSW.State, casinoSW.Industry, casinoSW.Year, str(casinoSW.Lat), str(casinoSW.Long), func.sum(casinoSW.Count)).\
#         group_by(casinoSW.Countym, casinoSW.State, casinoSW.Industry, casinoSW.Year).order_by(func.sum(casinoSW.Count).desc()).all()
#     session.close()
#     return jsonify(county_data)



# @app.route("/Suspicious Activity")
# def suspicious_act():
#     session = Session(engine)
#     suspicious_activity = session.query(casinoSW.Activity,  casinoSW.State, casinoSW.Countym, casinoSW.Industry, casinoSW.Year, str(casinoSW.Lat), str(casinoSW.Long), func.sum(casinoSW.Count)).\
#         group_by(casinoSW.Activity, casinoSW.State, casinoSW.Industry, casinoSW.Countym, casinoSW.Year).order_by(func.sum(casinoSW.Count).desc()).all()
#     session.close()
#     return jsonify(suspicious_activity)



if __name__ == '__main__':
    app.run(debug=True)