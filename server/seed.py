from models import User
from faker import Faker
from config import db, app, bcrypt

fake = Faker()


# function to seed database
def seed_database():
    User.query.delete()

    # static values
    usernames = [
        "johndoe",
        "julianamonroe",
        "briankimani",
        "mayaandreas"
    ]

    emails = [
        "johndoe1@gmail.com",
        "julianamonroe2@gmail.com",
        "briankimani3@gmail.com",
        "mayaandreas4@gmail.com"
    ]

    passwords = [
        "passjohndoe",
        "passjulianamonroe",
        "passbriankimani",
        "passmayaandreas"
    ]

    for i in range(4):
        user = User(
            username=usernames[i],
            email=emails[i],
            _password_hash=bcrypt.generate_password_hash(
                passwords[i].encode('utf-8'))

        )
        db.session.add(user)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        seed_database()
