# Flask Blog Dashboard

A simple blog dashboard built with Flask to demonstrate Flask fundamentals, Jinja templates, template inheritance, and conditional statements.

## Features

- **Dynamic Post Rendering**: Posts are rendered dynamically using Jinja templates
- **Template Inheritance**: Base template provides consistent layout across all pages
- **Conditional Logic**: Handles published and unpublished (draft) posts differently
- **Responsive Design**: Clean, modern UI that works on all devices
- **Dashboard**: Separate view showing all posts including drafts

## Project File Structure

flask-blog-dashboard/
│
├── app.py                 
├── requirements.txt       
├── README.md             
│
├── templates/
│   ├── base.html        
│   ├── home.html       
│   └── post.html        
│
└── static/
    └── css/
        └── style.css   


## Key Concepts Covered

### 1. Flask Application Structure
- Application factory pattern
- Route definitions
- Error handlers
- Context processors

### 2. Routing in Flask
- Basic routes (`/`, `/dashboard`)
- Dynamic routes with parameters (`/post/<int:post_id>`)
- URL building with `url_for()`

### 3. Jinja Templates
- Variable rendering: `{{ variable }}`
- Template filters: `{{ post.date.strftime('%B %d, %Y') }}`
- Loop rendering: `{% for post in posts %}`

### 4. Template Inheritance
- Base template with `{% block content %}`
- Child templates extending base with `{% extends "base.html" %}`
- Overriding blocks in child templates

### 5. Conditional Statements in Jinja
```jinja2
{% if post.published %}
    <a href="{{ url_for('post_detail', post_id=post.id) }}">
        {{ post.title }}
    </a>
{% else %}
    {{ post.title }}
{% endif %}
```

## Installation & Setup

1. **Clone or download the project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to `http://localhost:5000`

## Routes

| Route | Description |
|-------|-------------|
| `/` | Home page - shows only published posts |
| `/post/<id>` | Individual post page |
| `/admin` | Admin dashboard - shows all posts including drafts |

## Sample Data

The application comes with 6 sample posts:
- 4 published posts (visible on home page)
- 2 draft posts (only visible in admin dashboard)

## Template Features

### Base Template (`base.html`)
- Common HTML structure
- Navigation header
- Footer with dynamic year
- Content block for child templates

### Home Template (`home.html`)
- Statistics cards showing post counts
- Grid of post cards
- Conditional rendering for draft posts
- Draft badge for unpublished content

### Post Template (`post.html`)
- Full post content display
- Breadcrumb navigation
- Author information
- Status badges (Published/Draft)
- Related posts section

## Customization

### Adding New Posts
Edit the `posts` list in `app.py`:

```python
{
    "id": 7,
    "title": "Your New Post",
    "content": "Post content here...",
    "author": "Your Name",
    "date": datetime(2024, 3, 4),
    "published": True,
}
```

### Modifying Styles
Edit `static/css/style.css` to customize the appearance.

## Learning Checklist

- [ ] Understand Flask app structure
- [ ] Can create routes with parameters
- [ ] Know how to use `render_template()`
- [ ] Understand template inheritance (`extends`, `block`)
- [ ] Can use Jinja conditionals (`if`, `else`, `endif`)
- [ ] Can use Jinja loops (`for`, `endfor`)
- [ ] Know how to use `url_for()` for URL generation
- [ ] Understand template filters


