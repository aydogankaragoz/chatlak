Create a virtual environment named `env` inside the created directory by,
```bash
virtualenv env
```

To activate this environment use this command `chatlak` directory.
```bash
source env/bin/activate
```

When you need to deactivate the virtual environment do it using `deactivate` command.
```bash
deactivate
```

To Run:
```bash
python app.py
```
or
```bash
FLASK_APP=app.py flask run
```

Create DB:
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
