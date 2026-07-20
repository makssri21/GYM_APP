from init import db
from flask_login import UserMixin
from datetime import datetime


class Requests(UserMixin, db.Model):
    __tablename__ = 'requests'

    IDRequest = db.Column(db.Integer, primary_key=True)
    RequestTitle = db.Column(db.Unicode(128))
    DateOfBirth = db.Column(db.Date)
    Place = db.Column(db.Unicode(64))
    Comment = db.Column(db.Unicode(1024))
    CreatedAt = db.Column(db.DateTime, default = datetime.utcnow)
    CreatedBy= db.Column(db.String(50))
    UpdatedAt = db.Column(db.DateTime)
    UpdatedBy= db.Column(db.String(50))
    RequestStatusId = db.Column(db.Integer, db.ForeignKey('request_statuses.IDRequestStatus'), nullable=False)
  

    request_status = db.relationship('RequestStatuses', backref='requests')

    def get_id(self):
        return str(self.IDUser)
    
    @property
    def serialize(self):
        return {
            'id': self.IDRequest,
            'request_title': self.RequestTitle,
            'date_of_birth': self.DateOfBirth,
            'place': self.Place,
            'comment': self.Comment,
            'created_at': self.CreatedAt,
            'created_by': self.CreatedBy,
            'updated_at': self.UpdatedAt,
            'updated_by': self.UpdatedBy,
            'request_status_id': self.RequestStatusId
      

        }
