from init import db

class Users(db.Model):
    __tablename__ = 'users'

    IDUser = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(32))
    FullName = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Password = db.Column(db.String(255))  # nova kolona
    RoleId = db.Column(db.Integer, db.ForeignKey('roles.IDRoles'), nullable=False)
    IsActive = db.Column(db.Integer)

    role = db.relationship('Roles', backref='users')
    
    @property
    def serialize(self):
        return {
            'id': self.IDUser,
            'username': self.Username,
            'password': self.Password,
            'full_name': self.FullName,
            'email': self.Email,
            'role_id': self.RoleId,
            'is_active': self.IsActive

        }