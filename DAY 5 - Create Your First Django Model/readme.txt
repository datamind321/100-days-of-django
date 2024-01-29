Step 1 : first create your model in  models.py file .
step 2 : Register your model in admin.py file.


After step 2 , run some commands for  model migrations :-

> python manage.py makemigrations
> python manage.py migrate 

For access django-admin create a superuser :-

> python manage.py createsuperuser 

- provide username like 'admin'
- provide email like 'admin@gmail.com'
- provide a password like 'admin666' 
- click on 'y' and superuser created successfully.

Run your project and below the url type /admin and access to your django-admin panel using your name and password when you have created superusers time. 
