from models import User
from faker import Faker
from config import db, app

fake = Faker()


# function to seed the database
def seed_database():
    User.query.delete()

    for _ in range(5):
        user = User(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password=fake.unique.password()

        )
        db.session.add(user)
        db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        seed_database()
