from datetime import datetime
from logs import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    #fname and lname are not unique in the event that two different pepole with same names are registered in the system
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(),unique = True, nullable = False)
    fname = db.Column(db.String(),unique = False, nullable = False)
    lname = db.Column(db.String(),unique = False, nullable = False)
    email = db.Column(db.String(), unique = True, nullable = False)
    phone = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column(db.String(), unique = True, nullable = False)
    log = db.relationship('Entry', backref = 'user', lazy = True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Entry(db.Model):

    id = db.Column(db.Integer(), primary_key = True, unique = True)
    client = db.Column(db.String(), unique = False, nullable = False)
    company = db.Column(db.String(), unique = False, nullable = True)
    contact = db.Column(db.String(), unique = False, nullable = False)
    email = db.Column(db.String(), unique = False, nullable = True)
    query = db.Column(db.String(), unique = False, nullable = False)
    description = db.Column(db.String(), unique = False, nullable = False)
    date = db.Column(db.DateTime(), unique = False, nullable = False, default = datetime.now)
    status = db.Column(db.String(), unique = False, nullable = False, default = 0)
    ref = db.Column(db.DateTime(), unique = False, nullable = False, default = datetime.now)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), unique = False, nullable = False)


    def __repr__(self):
        return f"Post('{self.query}','{self.description}','{self.status}')"