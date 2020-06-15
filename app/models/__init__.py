from app import db


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    description = db.Column(db.Text)
    is_done = db.Column(db.Boolean, default=False)
    date_posted = db.Column(db.DateTime)
    date_finished = db.Column(db.DateTime, nullable=True)

    def __init__(self, header, description, is_done, date_posted):
        self.header = header
        self.description = description
        self.is_done = is_done
        self.date_posted = date_posted
