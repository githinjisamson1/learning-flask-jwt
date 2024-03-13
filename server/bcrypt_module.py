from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
bcrypt = Bcrypt(app)


#  define a function to hash a password using bcrypt

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')


#  register a new user with a hashed password

@app.route('/register', methods=['POST'])
def register():
    password = request.json['password']
    hashed_password = hash_password(password)
    new_user = User(password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})


# verify a password against a hashed password

@app.route('/login', methods=['POST'])
def login():
    password = request.json['password']
    user = User.query.filter_by(username=request.json['username']).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'})
