

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

     def __repr__(self):
        return '<CasinoSW %r>' % (self.name)