# 🛕 Srivari Seva Portal — Temple Management System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**A full-stack Temple Management and Online Darshan Booking System inspired by TTD architecture.**  
Built with Django, HTML, CSS, Bootstrap, and SQLite3.

🌐 **Live Demo:** [srivari-booking.onrender.com](https://srivari-booking.onrender.com)

</div>

---

## 📌 Overview

The **Srivari Seva Portal** is a devotional web application that enables devotees to access temple services online — from booking darshan tickets and sevas to making donations and staying updated on festivals. Inspired by the Tirumala Tirupati Devasthanams (TTD) platform, it brings the spiritual experience of temple management into a modern, accessible digital format.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🙏 **Darshan Booking** | Book darshan slots online and avoid long queues |
| 🪔 **Seva Booking** | Reserve sacred poojas and temple seva activities |
| 💛 **Online Donation** | Contribute to temple development securely |
| 🎉 **Festival Updates** | Browse upcoming temple festivals and celebrations |
| 🖼️ **Temple Gallery** | View divine moments captured at the temple |
| 📬 **Contact Form** | Send messages directly via EmailJS integration |
| 🔐 **User Auth** | Login, session management, and profile support |
| 📱 **Responsive UI** | Fully mobile-friendly across all screen sizes |

---

## 🛠️ Tech Stack

**Backend**
- Python 3.x
- Django 4.x
- SQLite3

**Frontend**
- HTML5 & CSS3
- Bootstrap 5
- Vanilla JavaScript
- Google Fonts (Poppins, Cinzel)
- Font Awesome 6
- EmailJS (contact form)

**Deployment**
- Render (cloud hosting)

---
 
## 📁 Project Structure
 
```
tms_project/
│
└── Temple/                        # Root Django project folder
    │
    ├── Temple/                    # Project config (settings, urls, wsgi)
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    ├── Templeapp/                 # Main Django app
    │   ├── migrations/
    │   │   └── 0001_initial.py
    │   │
    │   ├── templates/             # HTML templates
    │   │   ├── home.html
    │   │   ├── about.html
    │   │   ├── contact.html
    │   │   ├── darshan.html
    │   │   ├── seva.html
    │   │   ├── festival.html
    │   │   ├── donation.html
    │   │   ├── gallery.html
    │   │   ├── login.html
    │   │   ├── otp.html
    │   │   ├── profile.html
    │   │   └── download.html
    │   │
    │   ├── static/                # App static assets
    │   │   ├── logo.png
    │   │   ├── banner.png
    │   │   ├── profile.png
    │   │   ├── a.png / a.jpg
    │   │   ├── temp.png / tem.png
    │   │   ├── s1.png – s4.png    # Service icons
    │   │   ├── f1.png – f5.png    # Festival images
    │   │   └── 1.jpg – 13.jpg     # Gallery images
    │   │
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── apps.py
    │
    ├── staticfiles/               # Collected static files (Render deploy)
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── build_files.sh             # Render build script
    └── vercel.json                # Vercel deployment config
```
---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- pip package manager
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Manoj-Developer360/tms_project.git
cd tms_project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Then open your browser and visit **http://127.0.0.1:8000/**

---

## 📸 Pages

- **Home** — Hero banner, services overview, about section, counter stats, gallery preview
- **About** — Portal mission, features, and temple background
- **Darshan** — Slot booking interface
- **Seva** — Sacred seva reservation
- **Festivals** — Upcoming temple events
- **Donation** — Online contribution portal
- **Gallery** — Photo gallery of temple moments
- **Contact** — EmailJS-powered contact form

---

## 🌐 Live Deployment

This project is deployed on **Render**:  
🔗 [https://srivari-booking.onrender.com](https://srivari-booking.onrender.com)

> **Note:** The server may take 30–60 seconds to wake up on first visit (free-tier cold start).

---

## 🙌 Acknowledgements

- Inspired by the [TTD Online Services Portal](https://www.ttdsevaonline.com/)
- Temple imagery and spiritual design language from Tirumala traditions
- EmailJS for contact form email delivery

---

## 📄 License
 
This project was developed as an **academic assignment** — the objective was to design and build a full-stack temple management web application inspired by the TTD (Tirumala Tirupati Devasthanams) portal architecture.
 
> This project does not represent, endorse, or favor any religion. It was built purely for educational and technical demonstration purposes as part of a college/university assignment.
 
---
 
## 👨‍💻 Developer
 
<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Manoj Kumar V</td>
  </tr>
  <tr>
    <td><strong>Role</strong></td>
    <td>Data Analyst · UI Web Developer · Python Django Developer</td>
  </tr>
  <tr>
    <td><strong>Education</strong></td>
    <td>B.E Computer Science & Engineering — SSM Institute of Technology (CGPA: 7.94)</td>
  </tr>
  <tr>
    <td><strong>Location</strong></td>
    <td>Dindigul, Tamil Nadu, India</td>
  </tr>
  <tr>
    <td><strong>Portfolio</strong></td>
    <td><a href="https://mkv-portfolio.vercel.app/">mkv-portfolio.vercel.app</a></td>
  </tr>
  <tr>
    <td><strong>GitHub</strong></td>
    <td><a href="https://github.com/Manoj-Developer360">github.com/Manoj-Developer360</a></td>
  </tr>
  <tr>
    <td><strong>Email</strong></td>
    <td><a href="mailto:kumarvmanoj329@gmail.com">kumarvmanoj329@gmail.com</a></td>
  </tr>
  <tr>
    <td><strong>LinkedIn</strong></td>
    <td><a href="https://www.linkedin.com/in/manoj-kumar-v-a4b48a30a/">linkedin.com/in/manoj-kumar-v</a></td>
  </tr>
</table>
Designed and developed end-to-end as an assigned academic project.
 
---
