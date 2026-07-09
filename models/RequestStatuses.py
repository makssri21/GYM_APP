from init import db

class RequestStatuses(db.Model):
    __tablename__ = 'request_statuses'

    IDRequestStatus = db.Column(db.Integer, primary_key=True)
    RequestStatusName = db.Column(db.Unicode(32))

    @property
    def serialize(self):
        return {
            'id': self.IDRequestStatus,
            'name': self.RequestStatusName
        }