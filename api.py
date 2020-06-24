from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import json

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/bitmexdev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,email):
        self.username = username
        self.email  = email

class UserSchema(ma.Schema):
    class Meta:
        fields = ('username','email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/test", methods=["GET"])
def test():
    return 'hello world'


@app.route("/add", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username,email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)

@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)