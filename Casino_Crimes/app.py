from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
app = Flask(__name__)
# This is the sqlite:///... connection string that you used to connect to the casino db
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///Casino.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine("sqlite:///sqliteCasino.")
db = SQLAlchemy(app)
class CasinoSW(db.Model):
    __tablename__ = 'casinoSW'
    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String)
    SuspiciousActivity = db.Column(db.Float)
    Industry = db.Column(db.String)
    Long = db.Column(db.String)
    Lat = db.Column(db.String)
    Year = db.Column(db.String)
    Countym = db.Column(db.String)
    Count = db.Column(db.String)
    
@app.route('/')
def index():
    results = CasinoSW.query.limit(5)
    return render_template('index.html', results=results)

@app.route('/about')
def about():
    results = CasinoSW.query.limit(5)
    return render_template('about.html', results=results)

@app.route('/api/v1.0/fincrimes')
def fincrimes():
    # fincrimes = CasinoSW.query
    results = db.session.query(CasinoSW.id, CasinoSW.State, CasinoSW.SuspiciousActivity, CasinoSW.Industry,
    CasinoSW.Long, CasinoSW.Lat, CasinoSW.Year,  CasinoSW.Countym, CasinoSW.Count).all()
    fincrimes=[]
    for a, b, c, d, e, f, g, h, i  in results:
        entry = {
            "id": a,
            "State": b,
            "SuspiciousActivity": c,
            "Industry": d,
            "Long": e,
            "Lat": f,
            "Year": g,
            "Countym": h,
            "Count": i
        }
        fincrimes.append(entry)
    final_result = {"fincrimes":fincrimes}
    return jsonify(fincrimes)
# @app.route('/api/v1.0/fincrimes/<state_name>')
# def fincrimes_state(state_name):
#     canonicalized = state_name.replace(" ", "").lower()
#     for state in fincrimes:
#         search_term = state["state_name"].replace(" ", "").lower()
#         if search_term == canonicalized:
#             return jsonify(state)
#     return jsonify({"error": f"State {state_name} not found."}), 404

@app.route("/industry")
def industryType():
    """Return a list fo types of industry with their number for each state"""
    # session = Session(engine)
    results = db.session.query(CasinoSW.Industry, CasinoSW.State, str(CasinoSW.Lat), str(CasinoSW.Long), func.sum(CasinoSW.Count)).\
        group_by(CasinoSW.Industry, CasinoSW.State).order_by(func.sum(CasinoSW.Count).desc()).all()
    industry = []
    for a,b,d,e,f in results:
        entry = {
            "Industry": a,
            "State": b,
            "Lat": d,
            "Long": e,
            "Count":f
        }
        industry.append(entry)
    final_result = {"industry":industry}
    # industry, casino_types = {}, []
    # for x in results:
    #     for column, value in x.items():
    #         industry = {**industry, **{column:value}}
    #     casino_types.append(industry)
    # session.close()
    return jsonify(industry)
# @app.route("/states")
# def states():
#     session = Session(engine)
#     state_data = db.session.query(CasinoSW.State, CasinoSW.Industry, CasinoSW.Year, str(CasinoSW.Lat), str(CasinoSW.Long), func.sum(CasinoSW.Count)).\
#         group_by(CasinoSW.State, CasinoSW.Industry, CasinoSW.Year).order_by(func.sum(CasinoSW.Count).desc()).all()
#     session.close()
#     return jsonify(state_data)

@app.route("/county")
def counties():
    # session = Session(engine)
    county_data = db.session.query(CasinoSW.Countym, CasinoSW.State, CasinoSW.Industry, CasinoSW.Year, str(CasinoSW.Lat), str(CasinoSW.Long), func.sum(CasinoSW.Count)).\
        group_by(CasinoSW.Countym, CasinoSW.State, CasinoSW.Industry, CasinoSW.Year).order_by(func.sum(CasinoSW.Count).desc()).all()
    # session.close()
    counties = []
    for a,b,c,d,e,f,g in county_data:
        entry = {
            "Countym": a,
            "State": b,
            "Industry": c,
            "Year": d,
            "Lat": e,
            "Long": f,
            "Count": g
        }
        counties.append(entry)
    final_result = {"counties":counties}
    return jsonify(counties)

@app.route("/SuspiciousActivity")
def suspicious_act():
    # session = Session(engine)
    suspicious_activity = db.session.query(CasinoSW.SuspiciousActivity,  CasinoSW.State, func.sum(CasinoSW.Count)).\
        group_by(CasinoSW.State, CasinoSW.SuspiciousActivity).order_by(func.sum(CasinoSW.Count)).all()
    # session.close()
    activities = []
    for a,b,c in suspicious_activity:
        entry = {
            "SuspiciousActivity": a,
            "State": b,
            "Count": c
        }
        activities.append(entry)
    final_result = {"activities":activities}
    return jsonify(activities)
if __name__ == '__main__':
    app.run(debug=True)