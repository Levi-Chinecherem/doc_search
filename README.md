
# Documentary Search Project

![Documentary Search Logo](https://github.com/Levi-Chinecherem/doc_search/blob/master/sample.PNG)

Welcome to the Documentary Search project! 🎥 This is an archive of documentary projects where you can search for and explore various research topics. It's like a library for documentaries!


## current admin user

username: admin
password: password123
## Features

- 📚 Search for documentaries by title, author, and year
- 📝 Register and upload your own documentaries
- 👀 View documentary details including likes, comments, and sharing
- 👍 Like and comment on documentaries
- 📤 Share documentaries with others

## Technologies Used

The Documentary Search project uses different technologies to make everything work together:

- **Backend**: Django 🐍
- **Frontend**: HTML, CSS, JavaScript (jQuery) 🌐
- **Database**: SQLite (can be extended to other databases supported by Django) 🗃️
- **Authentication**: Django-allauth (with support for Gmail and Facebook) 🔒
- **Documentary PDF Preview**: PDF.js 📄
- **File Uploads**: Django default file handling 📂
- **Ajax and jQuery**: For smooth interactions and real-time updates ⚡

## Project Setup

To run the Documentary Search project on your computer, follow these steps:

1. **Clone the project**: Download the project files to your computer by clicking on the "Clone" button and selecting "Download ZIP". Unzip the downloaded file to a folder of your choice.

2. **Create and activate a virtual environment**: Open your command-line interface (Terminal, Command Prompt, etc.) and navigate to the project's folder. Create a virtual environment by running the following command:
   ```
   python -m venv env
   ```
   Activate the virtual environment:
   - For Windows:
     ```
     env\Scripts\activate
     ```
   - For macOS/Linux:
     ```
     source env/bin/activate
     ```

3. **Install dependencies**: Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations**: Apply the necessary database migrations by running the following command:
   ```
   python manage.py migrate
   ```

5. **Create a superuser**: Create a superuser account to access the admin panel and have additional privileges by running the following command:
   ```
   python manage.py createsuperuser
   ```

6. **Start the development server**: Launch the development server by running the following command:
   ```
   python manage.py runserver
   ```

7. **Access the project**: Open your web browser and visit `http://localhost:8000` to access the Documentary Search project.

## Contributors

The following awesome people contributed to the development of the Documentary Search project:

- Levi Chinecherem (Project Lead) 👨‍💻
- Lambert God'stime (Research work person)👨‍💻

---

Thank you for choosing the Documentary Search project! 🙌 Start exploring and enjoy watching documentaries!



Let me know if you have any further questions!
