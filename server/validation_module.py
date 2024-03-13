#  import the necessary modules and initialize the Flask application and SQLAlchemy object
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


# define a model with validated fields
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, validators=[
                         DataRequired(), Length(min=4, max=20)])
    email = db.Column(db.String(120), unique=True, nullable=False, validators=[
                      DataRequired(), Email(), Length(min=6, max=120)])
    password = db.Column(db.String(128), nullable=False, validators=[
                         DataRequired(), Length(min=8, max=128)])
    confirm_password = db.Column(db.String(128), nullable=False, validators=[
                                 DataRequired(), EqualTo('password')])

    def __repr__(self):
        return f'<User {self.username}>'


# create a new User object with validated fields
@app.route('/register', methods=['POST'])
def register():
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        confirm_password = request.json['confirm_password']

        new_user = User(username=username, email=email,
                        password=password, confirm_password=confirm_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'})

    except ValidationError as e:
        return jsonify({'message': str(e)}), 400
