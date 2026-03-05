from flask import Flask, render_template, abort
from datetime import datetime

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "Getting Started with Flask",
        "content": "Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. In this post, we'll explore the basics of Flask and how to set up your first application.",
        "author": "Abdul Rahman",
        "date": datetime(2024, 3, 1),
        "published": True,
        
    },
    {
        "id": 2,
        "title": "Understanding Jinja Templates",
        "content": "Jinja is a modern and designer-friendly templating language for Python. It is fast, widely used and secure with the optional sandboxed template execution environment. Template inheritance allows you to build a base skeleton template that contains all the common elements of your site.",
        "author": "Hassan Ali",
        "date": datetime(2024, 2, 28),
        "published": True,
       
    },
    {
        "id": 3,
        "title": "Python Best Practices",
        "content": "Writing clean, maintainable Python code is essential for any project. This post covers PEP 8 guidelines, code organization, and tips for writing better Python code that your future self will thank you for.",
        "author": "John",
        "date": datetime(2024, 2, 25),
        "published": True,
        
    },
    {
        "id": 4,
        "title": "Advanced Flask Patterns (Draft)",
        "content": "This post is currently being written and will cover advanced Flask patterns including blueprints, application factories, and deployment strategies.",
        "author": "David",
        "date": datetime(2024, 2, 20),
        "published": False,
        
    },
    {
        "id": 5,
        "title": "Building REST APIs with Flask",
        "content": "REST APIs are the backbone of modern web applications. Learn how to build robust and scalable APIs using Flask and best practices for API design.",
        "author": "Imran Khan",
        "date": datetime(2024, 2, 15),
        "published": True,
       
    },
    {
        "id": 6,
        "title": "Database Integration (Draft)",
        "content": "A comprehensive guide to integrating databases with Flask applications using SQLAlchemy and Flask-SQLAlchemy extensions.",
        "author": "Frank Brown",
        "date": datetime(2024, 2, 10),
        "published": False,
        
    }
]


@app.route("/")
def home():
  
    published_posts = [post for post in posts if post["published"]]
    unpublished_count = len([post for post in posts if not post["published"]])
    total_posts = len(posts)

    return render_template(
        "home.html",
        posts=published_posts,
        unpublished_count=unpublished_count,
        total_posts=total_posts
    )


@app.route("/post/<int:post_id>")
def post_detail(post_id):
  
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        abort(404)

    return render_template("post.html", post=post)


@app.route("/dashboard")
def dashboard():
    return render_template("home.html", posts=posts, show_all=True, is_admin=True)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
