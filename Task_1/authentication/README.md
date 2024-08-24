Here's a detailed README file for your Django project `profile_app`:

---

# Profile App

## Overview

`profile_app` is a Django project designed for user registration, login, and profile management. It provides a comprehensive user management system where users can register, log in, update their profiles, and manage their accounts. The application ensures proper handling of errors, including null fields and invalid entries, and enforces password complexity requirements.

## Features

- **User Registration**: Users can register with basic information including username, email, password, and password confirmation. The system validates entries and provides error handling for issues like null fields and weak passwords.
- **Profile Creation**: Upon successful registration, a user profile is automatically created using Django signals.
- **Login Functionality**: Users can log in using their username and password. Access is restricted to authenticated users only.
- **Profile Management**: After logging in, users can view and update their profile details including name, email address, username, phone number, description, and date of birth.
- **Profile Photo**: Users can upload and update their profile photo. A default user icon is displayed if no photo is uploaded.
- **Account Management**: Users can edit or delete their accounts. 
- **Logout**: Users can log out from the application.

## Deployment

The `profile_app` is deployed and accessible online. You can test the website with the following default credentials:

- **Username**: `test`
- **Password**: `test@123`

Visit the deployed application here: [Profile App](https://user-authentication-app-xzcg.onrender.com)

## Installation and Setup

To run the project on your local server, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone  https://github.com/sainandini1/Future_Intern_Tasks.git
   cd profile_app
   ```

2. **Install Dependencies**

   Make sure you have `pip` installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**

   Set up the database by applying the migrations:

   ```bash
   python manage.py migrate
   ```

4. **Run the Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

1. **Registration**: Navigate to the registration page and enter your details. Ensure that all fields are filled correctly and passwords meet the complexity requirements.

2. **Login**: Use the login page to authenticate. Enter your username and password to access the website.

3. **Profile Management**: After logging in, go to the profile page. You can view and edit your profile information, upload a profile photo, and manage your account (edit or delete).

4. **Logout**: Use the logout button to end your session and return to the login page.

## Project Structure

- `profile_app/`: The main project directory containing the application code.
- `profile_app/settings.py`: Contains the project settings.
- `profile_app/urls.py`: URL routing configuration.
- `profile_app/views.py`: Defines the views for the application.
- `profile_app/models.py`: Contains the data models.
- `profile_app/forms.py`: Defines the forms used in the application.
- `profile_app/templates/`: Directory for HTML templates.
- `profile_app/static/`: Directory for static files (CSS, JavaScript).

## Contributing

If you wish to contribute to the project, please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.
