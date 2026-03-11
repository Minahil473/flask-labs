from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    # post method here is used to check it if the data is coming from the form or not and get method is used to check if the data is coming from the url or not
    if request.method == 'POST':
        # get here is used to read the name and message owhich is the user input from the form and store it in the variable name and message
        name = request.form.get('username')
        message = request.form.get('message')
    # here render template render it to the thankyou page
        return render_template('thankyou.html', user=name , message=message)
    # this return render feedback from again if there is any error in thankyou page rendering
    return render_template('feedback.html')