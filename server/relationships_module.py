'''
one to many relationship
In a one-to-many relationship, one model instance can have many related instances of another model. For example, a User model can have many Post instances.
The backref parameter in the relationship() function creates a author attribute in the Post model that contains the related User instance
'''


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


'''
many to one relationship
In a many-to-one relationship, many model instances can be related to one instance of another model. For example, many Comment instances can be related to one Post instance.
The backref parameter in the relationship() function creates a post attribute in the Comment model that contains the related Post instance.
'''


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)


'''
many to many relationship
In a many-to-many relationship, many instances of one model can be related to many instances of another model. For example, many User instances can be related to many Role instances.
The User model has a many-to-many relationship with the Role model. The users_roles table is used as the join table for the many-to-many relationship. The User model has a roles attribute that contains a list of related Role instances. The Role model has a users attribute that contains a list of related User instances.
'''
users_roles = db.Table('users_roles',
                       db.Column('user_id', db.Integer, db.ForeignKey(
                           'user.id'), primary_key=True),
                       db.Column('role_id', db.Integer, db.ForeignKey(
                           'role.id'), primary_key=True)
                       )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=users_roles,
                            backref=db.backref('users', lazy='dynamic'))


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)


'''
When defining relationships in Flask-SQLAlchemy, you can also specify additional parameters in the relationship() function, such as lazy, cascade, and single_parent. Here's a brief explanation of these parameters:

lazy: Specifies how the related instances should be loaded. The default value is 'select', which means that the related instances are loaded using a separate SQL query. You can also set lazy to 'joined' to load the related instances using a JOIN query, or 'subquery' to load the related instances using a subquery.
cascade: Specifies what operations should be cascaded to the related instances. The default value is 'save-update, merge, refresh-expire, expunge', which means that operations like add(), update(), and delete() will be cascaded to the related instances. You can also set cascade to 'all, delete-orphan' to delete any related instances that are not associated with a parent instance.
single_parent: Specifies whether a related instance can have only one parent instance. The default value is False. You can set single_parent to True to ensure that a related instance can have only one parent instance.
'''