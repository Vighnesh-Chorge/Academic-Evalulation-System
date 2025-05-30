# 🎓 Academic Evaluation System

This is a Flask-based web application designed to evaluate and manage student academic performance. The system provides separate interfaces for students and administrators to input and review academic data.

## 📁 Project Structure

```
academic-evaluation-system/
│
├── app.py                         # Main Flask application: handles routes, form logic, and DB interaction
│
├── static/
│   └── css/
│       └── styles.css             # Custom styles for the app
│
├── templates/
│   ├── admin_students.html        # Admin dashboard to view/manage students
│   ├── form.html                  # Form for student mark submission
│   └── login.html                 # Login page for authentication
```

## 🚀 Features

- Student login and data entry form
- Admin view to manage and evaluate student performance
- Evaluation based on various academic inputs (UT marks, semester, etc.)
- Clean and responsive UI using custom CSS

## 🧠 How it Works

- `app.py` is the heart of this project. It:
  - Initializes the Flask app
  - Defines routes for:
    - `/login`: User login page
    - `/form`: Student mark entry form
    - `/admin`: Admin panel to view student data
  - Handles form submissions and redirects
  - Connects to the database to fetch and store student data
  - Renders HTML templates using Flask's `render_template()`

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (custom styles)
- **Templating**: Jinja2
- **Database**: (Add MySQL/SQLite info here if applicable)

## 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/academic-evaluation-system.git
   cd academic-evaluation-system
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```


3. **Configure the database**

   - Create your database and update credentials in `app.py` (or a separate `config.py` if used).
   - Initialize tables (manually or via script if provided).

4. **Run the application**
   ```bash
   python app.py
   ```

## 📈 Future Enhancements

- Add student performance prediction using ML
- Export results as PDF/Excel
- Role-based access (Admin, Teacher, Student)
- Integration with Power BI dashboards
