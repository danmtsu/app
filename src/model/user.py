from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name:str, password:str):
        self.name = name
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"
