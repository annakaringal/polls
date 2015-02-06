# polls_djangular
Django Polls with DRF API

Getting Started
---------------

### Initial Setup ###
1. Clone this repository : git clone https://github.com/campbellchri/polls.git
2. Make a new virtualenv (outside of the polls directory/repo): ``virtualenv pollsEnv``
3. Activate the virtualenv: ``source pollsEnv/bin/activate``
4. Install the project requirements: ``pip install -r polls/requirements.txt``
5. Edit ``mysite/settings.py:36`` to match your timezone
6. Navigate to the polls directory and sync the database : ``python manage.py syncdb``
7. Install the frontend dependencies : ``python manage.py bower_install``
8. Collect the static files : ``python manage.py collectstatic``
9. Run the server: ``python manage.py runserver 8000``
10. Navigate to the polls angular application  ``http://localhost:8000/polls_app/`` or admin at ``http://localhost:8000/admin`` (admin:admin)

### URLS you have access to ###
http://127.0.0.1:8000/polls_app/ -> Angular Application
http://127.0.0.1:8000/admin/ -> Django Admin panel
http://127.0.0.1:8000/api/ -> Django Rest Framework Admin, sample endpoints for the API

Javascript files are found in : ``static/static/polls_app``

### After your first successful setup ###
1. Activate the virtualenv: ``source pollsEnv/bin/activate``
2. Run the server: ``python manage.py runserver``
3. Open website in browser at ``http://localhost:8000/polls`` or admin at ``http://localhost:8000/admin`` (admin:admin)