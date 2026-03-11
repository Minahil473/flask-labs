from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)

app.secret_key = "my-secret-key"


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('username')
        if not name:
         flash('Please enter your name')
         return redirect(url_for('form'))
        flash(f'Thank you for your feedback, {name}!')
        return redirect(url_for('thankyou'))
    return render_template('form.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')