# Django-ToDo-app
Django todo app to manage your daily tasks.

![image](https://user-images.githubusercontent.com/130636082/231813968-3a741db5-4d1f-4cf0-98af-f70a19511174.png)
### Setup
To get this repository, run the following command inside your git enabled terminal

```bash
$ git clone https://github.com/modeslatt/Django-ToDo-app.git
```
To run the app you will need django to be installed on your computer.
Once it's downloaded, head to the cloned repo directory and run the following command:

```bash
$ python manage.py makemigrations
```

Now to apply the migrations run:

```bash
$ python manage.py migrate
```

Now we need to create and admin user to run the app. Run the following command in your terminal and follow the instructions from the terminal:

```bash
$ python manage.py createsuperuser
```

Now we can start the server by running the following command and following the provided link: 

```bash
$ python manage.py runserver
```

To enter the admin panel head over to http://127.0.0.1:8000/admin and enter you login and password.

