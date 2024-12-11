![Customer_Feedback (1)](https://github.com/user-attachments/assets/c42a1758-0b84-434b-84f3-621da30bb5f0)

# Cebu Institute of Technology - University
*CSIT327 - G5* <br>
*BSIT - 3*

# Group Members
- Kenneth Jan T. Ambos
- James Queddeng
- Paul De Los Santos

# About The Project
The *Customer Feedback System* is an innovative solution designed to **gather**, **analyze**, and **manage** customer opinions effectively. This system empowers businesses to capture valuable insights from their customers. <br> <br>
The system features an interface for customers to submit feedback, including comments, and suggestions. 

### Key Features
- **User-Friendly UI**: A simple and intuitive interface allows customers to provide comments and suggestions.
- **Automated Response**: When submitting a form, a thank you email is sent to the customer.
- **Multi-Form**: The customer can choose which type of form they would like to submit to the company.

# Built With
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Google Fonts](https://img.shields.io/badge/Google%20Fonts-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://fonts.google.com/)


# Getting Started

### 1. Install Python  
Django requires Python to run.

1. Download Python from [Python.org](https://www.python.org/downloads/) and install it.
2. During installation, check the option to **Add Python to PATH**.
3. Verify the installation:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

### 2. Verify or Install pip (Python Package Manager)

`pip` is the package manager for Python, typically included with Python 3.4+.

- Check if pip is installed:
  ```bash
  pip --version
  ```
- If pip is not installed, run:
  ```bash
  python -m ensurepip --upgrade
  ```

### 3. Set Up a Virtual Environment (Optional but Recommended)

Virtual environments help isolate dependencies for your project.

- Create a virtual environment:
  ```bash
  python -m venv env
  ```
- Activate the virtual environment:
  - **Windows**:
    ```bash
    .\env\Scripts\activate
    ```
  - **macOS/Linux**:
    ```bash
    source env/bin/activate
    ```

### 4. Install Django

Install Django using pip:
```bash
pip install django
```

### 5. Verify Django Installation

Check the Django version to confirm installation:
```bash
django-admin --version
```

- Navigate to the main project directory:
   ```bash
   cd mainpage
   ```
- Navigate to the `UI` directory:
   ```bash
   cd UI
   ```
- Run the development server:
   ```bash
   python manage.py runserver
   ```
- Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# Functional Requirements
### Planning & Design
- Planning the Project
- Website Design and Layout
- Assigning of roles
- Color Theme selection

### User Authentication and Verification
- Captcha
- Input Boxes
- Login and Sign-up

### Feedback Collection
- Customers can either submit a
  - General Feedback Form
  - Complaint Form
  - Compliment Form

### Data Validation
- Required Fields on Forms
- Required Captcha

### Feedback Management and Storage
- Submitted forms are stored in the database

### Automated Response and Notifications
- Automated Email is sent to the customer once their form has been submitted

### Reporting and Analytics
- Admin page where history of submissions can be seen


# Documents
### ERD


### Gantt Chart


> There is always <br>
> one more bug to fix. <br>
>  – Ellen Ullman

Thank you for reading this and being part of this adventure!
