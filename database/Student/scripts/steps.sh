l_first_cmd="python ./Student/manage.py makemigrations"
l_sec_cmd="python ./Student/manage.py migrate"
l_third_cmd="python ./Student/manage.py runserver 0.0.0.0:8000"
sh $l_first_cmd
sh $l_sec_cmd
sh $l_third_cmd
