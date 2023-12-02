l_first_cmd="wait-for-it.sh db:3306 -- python manage.py makemigrations"
l_sec_cmd="python ./Student/manage.py migrate"
l_third_cmd="python ./Student/manage.py runserver 0.0.0.0:8000"
$l_first_cmd
$l_sec_cmd
$l_third_cmd

