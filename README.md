![Customer_Feedback (1)](https://github.com/user-attachments/assets/c42a1758-0b84-434b-84f3-621da30bb5f0)

# ![school (2)](https://github.com/user-attachments/assets/ca807c33-ae65-4eca-99fa-2c57a3d18ded) Cebu Institute of Technology - University
![stack-of-books](https://github.com/user-attachments/assets/fa80d092-8a57-45a7-81cf-3d7f5a729daa) *CSIT327 - G5* <br>
![graduation-hat](https://github.com/user-attachments/assets/6e2fb881-1084-4d8e-94ea-c8a6119ed249) *BSIT - 3*

# ![group](https://github.com/user-attachments/assets/72b77262-5970-427b-8af5-32ea9ed6b180) Group Members
- Kenneth Jan T. Ambos
- James Queddeng
- Paul De Los Santos

# ![support](https://github.com/user-attachments/assets/3e5e59e9-1dfb-4b59-93f7-1559ed8e8111) About The Project
The *Customer Feedback System* is an innovative solution designed to **gather**, **analyze**, and **manage** customer opinions effectively. This system empowers businesses to capture valuable insights from their customers. <br> <br>
The system features an interface for customers to submit feedback, including comments, and suggestions. 

### ![key-chain (2)](https://github.com/user-attachments/assets/cd555c51-4ff7-431d-80a6-ee2320495cee) Key Features
- ![support (1)](https://github.com/user-attachments/assets/1c546e5b-6028-4ccb-bc22-04ae88ce9359) **User-Friendly UI**: A simple and intuitive interface allows customers to provide comments and suggestions.
- ![chatbot](https://github.com/user-attachments/assets/f8640424-d683-40dc-af66-e2d4c6d0e0a4) **Automated Response**: When submitting a form, a thank you email is sent to the customer.
- ![multiple](https://github.com/user-attachments/assets/fc7908d9-c8d2-4435-b5ac-5b7571ffaff4) **Multi-Form**: The customer can choose which type of form they would like to submit to the company.

# ![settings (1)](https://github.com/user-attachments/assets/ae00f572-7f09-47ea-a796-0908ca356c09) Built With
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Google Fonts](https://img.shields.io/badge/Google%20Fonts-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://fonts.google.com/)


# ![power](https://github.com/user-attachments/assets/a926c297-4877-4fcf-93bc-f28d10fc4b46) Getting Started

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
   
- Run the development server:
   ```bash
   python manage.py runserver
   ```
- Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# ![checklist](https://github.com/user-attachments/assets/cd8ca616-7856-437e-b09b-2c50559047b6) Functional Requirements
### ![web-design (3)](https://github.com/user-attachments/assets/ebf1d6a3-e828-4a08-b39c-274e329ee92c) Planning & Design
- ![team-meeting](https://github.com/user-attachments/assets/37ea0ebd-b2c0-412e-8e45-452e146f7d7a) Planning the Project
- ![web-design (1)](https://github.com/user-attachments/assets/a618bfc1-e6c0-44f2-8500-ecddd8d07fbc) Website Design and Layout
- ![assign](https://github.com/user-attachments/assets/5f8ac9e1-da90-4011-82f2-8a5f2bf95776) Assigning of roles
- ![app](https://github.com/user-attachments/assets/c40b22fb-a09c-4615-bcb8-9801ab389f11) Color Theme selection

### ![authentication (1)](https://github.com/user-attachments/assets/0186692d-eadb-44a8-af1a-159b0574111d) User Authentication and Verification
- ![captcha](https://github.com/user-attachments/assets/ace074aa-cef7-4cd7-ad9c-4db2e8c8908f) Captcha
- ![input](https://github.com/user-attachments/assets/c6932dab-23aa-4af3-9b2e-08f629dbe8dd) Input Boxes
- ![login](https://github.com/user-attachments/assets/d6bb77e3-2623-4c59-8acc-957bfc59c570) Login and Sign-up

### ![data-collection (1)](https://github.com/user-attachments/assets/300f4831-7809-443d-a15f-2a0266f16e40) Feedback Collection
- Customers can either submit a
  - ![document](https://github.com/user-attachments/assets/b7ca02cf-c007-49eb-8723-803d546ebc36) General Feedback Form
  - ![complaint](https://github.com/user-attachments/assets/66cf7999-ff7c-40ea-8455-53f1d207c46a) Complaint Form
  - ![directions](https://github.com/user-attachments/assets/1976509a-54e0-40a6-949f-94c2552d860a) Compliment Form

### ![data-audit (1)](https://github.com/user-attachments/assets/c51d5d07-3bb5-4481-8f7f-611d29e81f43) Data Validation
- ![medical](https://github.com/user-attachments/assets/4b2e640d-0f88-4de1-b5d4-0e3a69f8f9b7) Required Fields on Forms
- ![captcha](https://github.com/user-attachments/assets/ace074aa-cef7-4cd7-ad9c-4db2e8c8908f) Required Captcha

### ![project-manager](https://github.com/user-attachments/assets/2e3d6f03-ef8a-4734-8793-26ecbb34aaaf) Feedback Management and Storage
- ![database](https://github.com/user-attachments/assets/69254b5f-51b9-4577-ad2d-c84804119122) Submitted forms are stored in the database

### ![auto-reply](https://github.com/user-attachments/assets/2cfa31ed-5508-4311-94f3-bdbc186a057c) Automated Response and Notifications
- ![email](https://github.com/user-attachments/assets/74827bf2-a28c-49ea-a8d3-34f55296bf1c) Automated Email is sent to the customer once their form has been submitted

### ![report](https://github.com/user-attachments/assets/4f874cff-8f1a-41a0-8a34-2069b208f29e) Reporting and Analytics
- ![benchmarking](https://github.com/user-attachments/assets/e1455c9a-c90d-44a2-b260-2c017d7ded3c) Admin page where history of submissions can be seen

# ![website (1)](https://github.com/user-attachments/assets/d93cb5bf-b898-47a0-bc42-1f25634be5c8) Page Information
#### ![house](https://github.com/user-attachments/assets/d8a43177-56cf-43c2-8db5-19f160bfadb2) *Home page:*
- Button to Feedback page
- Button to Complaint page
- Button to Compliment page

#### ![feedback](https://github.com/user-attachments/assets/3cb60844-3837-44ad-a499-bb01f5ee6ccc) *Feedback page:*
- Input boxes for user information
- Radio buttons
- Captcha
- Submit button

#### ![bad](https://github.com/user-attachments/assets/bf6d3cf5-ef60-4769-b753-6bfd60d3df42) *Complaint page:*
- Input boxes for user information
- Radio buttons
- Captcha
- Submit button

#### ![love](https://github.com/user-attachments/assets/6e9bd51c-289b-432a-82c5-86f923eb444a) *Compliment page:*
- Input boxes for user information
- Input box for compliment
- Captcha
- Submit button

#### ![software-engineer](https://github.com/user-attachments/assets/d50deced-64fd-4f7b-a6b3-b76d307ee5fc) *Admin page:*
- Reporting and Analytics Feature

# ![documents](https://github.com/user-attachments/assets/d89d4c1d-02de-4f46-9d74-c42912cc3b24) Documents
### ERD


### Gantt Chart

#
> There is always <br>
> one more bug to fix. <br>
>  – Ellen Ullman

Thank you for reading this and being part of this adventure! ![thanks](https://github.com/user-attachments/assets/20f0115c-b0ae-4711-8ea5-d502f71bbfb9)
