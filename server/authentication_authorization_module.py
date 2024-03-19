from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_required
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# Define models for user and role
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


# Login route using Flask-JWT
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

# Protected route requiring authentication and authorization


@app.route('/protected')
@jwt_required()
@roles_required('admin')
def protected_route():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
    app.run(debug=True)
