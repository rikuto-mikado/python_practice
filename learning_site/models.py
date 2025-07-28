from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class StidyLog(db.model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    minutes = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    note = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
