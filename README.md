🚀 Project Setup Guide
This guide will help you set up and run the project locally.
🛠 Prerequisites
Make sure you have the following installed:

-Python
-PostgreSQL
-pgAdmin

⚙️ Steps to Run the Project
1. Create a Virtual Environment
First, create a virtual environment by running the following command: py -m venv venv
💡 Note: If py doesn't work, try using python or python3.

2. Activate the Virtual Environment
To activate the virtual environment, use the appropriate command:
On Windows:
 .\venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Next, install the required dependencies from the requirements.txt file: pip install -r requirements.txt
💡 Tip: If pip doesn't work, use pip3.

4. Configure Local Settings
Copy the example settings file to a new local_settings.py file: cp local_settings_example.py local_settings.py

Then, update the database configuration in local_settings.py based on your database setup.

🛠 Setting Up the Database
-Open pgAdmin or your preferred PostgreSQL management tool.
-Create a new database and give it a name.
-Update the database details in local_settings.py.

5. Apply Database Migrations
Run the following commands to apply the database migrations:

-python manage.py makemigrations
-python manage.py migrate

6. Create a Superuser
Create a superuser to access the Django admin panel by running: python manage.py createsuperuser
Follow the prompts to set up a username and password.

7. Run the Server
Finally, start the development server: python manage.py runserver
You can now view the project by visiting http://127.0.0.1:8000 in your web browser.

📸 Screenshots
Include some screenshots or project visuals here:
<img src="https://github.com/username/repo-name/blob/main/assets/screenshot.png" width="400" />![image](https://github.com/user-attachments/assets/f775ed27-334d-4655-826c-85cafe12cf1f)

