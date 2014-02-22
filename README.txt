Build/execution instructions:
1. Open up command prompt (Windows) or terminal (Mac/Linux) and navigate to the project's root directory.
2. Run the command 'python manage.py runserver'. You will see a note saying "Starting development server...", as well as some other information. Leave that running.
3. Open up your favorite web browser and type 'localhost:8000' in the URL field, and go.
4. Enjoy the site!
5. Back in the command prompt/terminal, use <Ctrl-C> to terminate the server.

Extra notes:
1. You must have your Python installation directory included in your PATH environment variable for the 'python manage.py runserver' command to work.
2. You must have Python installed, of course (latest version recommended).
3. You must have Django installed, either in Python's 'Lib/site-packages' directory, or the project's root directory. Instructions at: http://www.djangoproject.com/download/ (latest version recommended).
4. There is a test superuser account created (Username: testuser  Password: test). You can use this account to access the admin backend (at '/admin') to see some cool stuff, and to login.

Known issues/bugs:
1. For now, the 'Food of the Day' link won't display a food item when clicked on. This will be implemented later.
