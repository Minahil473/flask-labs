from flask import Flask , request , redirect , url_for , session , Response

# its use to tell that its a main file 
app = Flask(__name__)
app.secret_key = 'supersecret' #when u work with session u have to define the secret-key 

# homepage login page
@app.route('/', methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == '123':
           session['user'] = username
           return redirect(url_for('welcome'))
        else:
           return Response("invalid credentials. Try again.", mimetype='text/plain') #mimetype is used to tells the browser to the plain text not any kinda html like text/html 
        
    return '''
    <h2>Login Page</h2>
        <form method="post">
            Username: <input type="text" name="username" ><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''
# welcome page
@app.route('/welcome')
def welcome():
    if 'user' in session:
        return f''' 
        <h2>Welcome,{session['user']}!</h2>
        <a href="{url_for('logout')}">Logout</a>

        '''
    
# logout route
@app.route('/logout')
def logout():
    session.pop('user') #this will remove the user from the session 
    return redirect(url_for('login')) #after logout it will redirect to login page

