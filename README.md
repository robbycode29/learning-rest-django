# learning-rest-django

1. Set up the project in a virtual environment (conda)

2. Install dependencies

3. Start a database server using Postgresql and create a database with the name mydb (modify settings.py according to your database connection if it's different)

4. Create superuser with >> python manage.py createsuperuser

5. Sync the db by running >> python manage.py migrate

6. Run the app with >> python manage.py runserver


Only logged in users can modify data in the db (read only for logged out users *anonymous users*)

To log in and out go to:

  localhost:8000/accounts/login ,
  localhost:8000/accounts/logout

The api has endpoints for the following tables in the db: 

  1. books:        localhost:8000/api/books
                   localhost:8000/api/books/<int:pk>
               
  2. authors:      localhost:8000/api/authors
                   localhost:8000/api/authors/<int:pk>
               
  3. publishers:   localhost:8000/api/publishers
                   localhost:8000/api/publishers/<int:pk>
