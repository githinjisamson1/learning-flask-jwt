from flask_mailman import Mail
from flask_mailman import EmailMessage


# # configuration of mail
app.config['MAIL_SERVER'] = environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


class Index(Resource):
    def get(self):
        msg = EmailMessage(
            'Welcome Message',
            "Welcome!",
            "samsongithinji@fastmail.com",
            ["githinjisamson148@gmail.com"]

        )

        msg.send()

        return "Hello World", 200

