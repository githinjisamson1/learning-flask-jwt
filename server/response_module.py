# strings
@app.route('/')
def hello():
    return 'Hello, World!'


# templates
@app.route('/')
def index():
    return render_template('index.html', name='John')


# json
@app.route('/json')
def json_example():
    data = {'name': 'John', 'age': 30}
    return jsonify(data)


# custom response codes
@app.route('/error')
def custom_error():
    response = make_response('Something went wrong!', 500)
    return response


# redirect
@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'Please log in'


# abort
@app.route('/user/<int:user_id>')
def get_user(user_id):
    if user_id == 0:
        # If user_id is 0, return a 404 Not Found error with a custom message
        abort(404, description="User not found")
    else:
        # Return user details
        return f'User ID: {user_id}'
