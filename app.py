from flask import Flask, render_template, send_file

app = Flask(__name__)

PORTFOLIO = {
    "name": "Nivyesh Jitendrabhai Chaudhari",
    "title": "Data Analyst",
    "subtitle": "Excel • Power BI • SQL • Python",
    "location": "Surat, Gujarat, India",
    "phone": "+91 7572841856",
    "email": "chaudharinivyesh92@gmail.com",

    # Social Profiles
    "linkedin": "https://www.linkedin.com/in/nivyesh-chaudhari-9a93332bb/",
    "github": "https://github.com/Nivyesh",

    "summary": (
        "Computer Science & Engineering graduate with hands-on experience in "
        "Microsoft Excel, Power Query, Power BI, SQL, Python, and Pandas for "
        "data cleaning, analysis, dashboard development, and MIS reporting."
    ),

    "skills": [
        "Excel",
        "Power Query",
        "Power BI",
        "DAX",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "Python",
        "Pandas",
        "NumPy",
        "Data Cleaning",
        "Data Analysis",
        "MIS Reporting",
        "Data Modeling",
        "Git",
        "GitHub"
    ],

    "projects": [
        {
            "title": "Sales Dashboard — Power BI",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=85",
            "description": (
                "Interactive dashboard analyzing sales, orders, quantity, "
                "discounts, regional performance and product-level trends."
            ),
            "tools": [
                "Power BI",
                "Power Query",
                "DAX",
                "Data Visualization"
            ]
        },

        {
            "title": "Employee Attendance MIS — Excel",
            "image": "https://images.unsplash.com/photo-1556761175-b413da4baf72?auto=format&fit=crop&w=1200&q=85",
            "description": (
                "Interactive employee dashboard using Power Query, Pivot Tables "
                "and Excel formulas for KPI-based MIS reporting."
            ),
            "tools": [
                "Excel",
                "Power Query",
                "Pivot Tables",
                "MIS"
            ]
        },

        {
            "title": "Human Resource Management System",
            "image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=85",
            "description": (
                "HRMS developed during the KAPS/NPCIL internship for employee "
                "information and administrative data management."
            ),
            "tools": [
                "PHP",
                "MySQL",
                "Database Design",
                "HRMS"
            ]
        }
    ],

    "education": (
        "Bachelor of Engineering — Computer Science & Engineering, 2022–2026"
    ),

    "college": (
        "R.N.G. Patel Institute of Technology, Bardoli • "
        "Gujarat Technological University"
    ),

    "cgpa": "8.24/10",

    "certifications": [
        "Microsoft Excel Beginners to Advance Course",
        "Microsoft Excel with A.I. Masterclass",
        "Deloitte Data Analytics Job Simulation — Forage",
        "SQL Micro Course",
        "Power BI Micro Course"
    ]
}


@app.route("/")
def home():
    return render_template("index.html", p=PORTFOLIO)


@app.route("/resume")
def resume():
    return send_file(
        "Nivyesh_Resume_DA(1).pdf",
        as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)