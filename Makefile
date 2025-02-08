run-dev:
	poetry run python manage.py runserver
run-prod:
	poetry run gunicorn django_app_template.wsgi:application --bind 0.0.0.0:8000
migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
dumpdata:
	poetry run python -Xutf8 manage.py dumpdata --indent=2 app.Model -o fixtures/Model
loaddata:
	poetry run python -Xutf8 manage.py loaddata fixtures/Model
tests:
	poetry run python manage.py test .
createsuperuser:
	poetry run python manage.py createsuperuser
collectstatic:
	poetry run python manage.py collectstatic --no-input
