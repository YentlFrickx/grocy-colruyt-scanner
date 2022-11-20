from flask_login import UserMixin

from db import db


class User(UserMixin, db.Model):

    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    profile_pic = db.Column(db.String(100))
    grocy_api_key = db.Column(db.String(1000))

    def __init__(self,
                 id_,
                 name,
                 email,
                 profile_pic,
                 grocy_api_key=''):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.grocy_api_key = grocy_api_key
