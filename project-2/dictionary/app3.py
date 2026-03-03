# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def login():
#     return render_template('login.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     # if username == 'mina' and password == 'pass':
#     #     return render_template('welcome.html', name=username)


# # use of dictionary to store valid users and their passwords
#     valid_users = {
#         "mina": "pass",
#         "admin": "123",
#         "john": "password"
#     }
#     # membership operater to check the value in the dict
#     if username in valid_users and password == valid_users[username]:
#         return render_template('welcome.html', name=username)
#     else:
#         return render_template('login.html', error="Invalid credentials")