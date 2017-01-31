rm -rf */migrations/
find . -name '*.pyc' -delete
if [ -d "uploads" ]; then
  echo "Upload directory exists!"
else
  mkdir uploads
fi;
appNames=(client utility)
for i in ${appNames[@]}; do
  mkdir $i/migrations/
  touch $i/migrations/__init__.py
done
echo 'DROP SCHEMA public CASCADE; CREATE SCHEMA public;' | ./manage.py dbshell
./manage.py heroku_deploy
./manage.py makemigrations
./manage.py migrate
./manage.py shell < heroku/drf_logger_init_data_load.py
gunicorn drflogger.wsgi --timeout 300 --limit-request-line 8190 --limit-request-fields 200 --limit-request-field_size 8190 --keep-alive 5 --log-file -
