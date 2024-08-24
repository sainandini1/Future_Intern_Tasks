
- **Username**: `admin`
- **Password**: `admin@1234`

## Installation and Setup

To run the project on your local server, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sainandini1/Future_Intern_Tasks.git
   cd Task_2/employ_management_system
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

