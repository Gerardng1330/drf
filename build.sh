set -o errexit

pip install -r requirements.txt

pyhon manage.py collectstatic --no-input
python manage.py migrate