from init import db

class Roles(db.Model):
    __tablename__ = 'roles'

    IDRoles = db.Column(db.Integer, primary_key=True)
    RoleName = db.Column(db.String(32))

    @property
    def serialize(self):
        return {
            'id': self.IDRoles,
            'name': self.RoleName
        }