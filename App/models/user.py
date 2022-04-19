from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    score = db.Column(db.Integer, default=0,nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)


    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'score': self.score,
        }
    
    def is_authenticated(self):
        return True;
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.id

    def set_password(self, password):
        """Create hashed password."""
        print(password,self)
        self.password = generate_password_hash(password, method='sha256')
        return self.password
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

