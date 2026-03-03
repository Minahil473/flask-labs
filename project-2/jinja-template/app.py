from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def student_profile():
    return render_template(
        'profile.html',
        name="minsa",
        is_topper=True,
        subjects=["Math", "Science", "English"]
        )