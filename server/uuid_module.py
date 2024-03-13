from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)


class MyModel(db.Model):
    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<MyModel {self.name}>'


# how to create instance
new_object = MyModel(name='example')
db.session.add(new_object)
db.session.commit()

# how to retrieve an object by its uuid
uuid_value = uuid.UUID('a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6')
object = MyModel.query.filter_by(id=uuid_value).first()
