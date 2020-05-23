# Khobor24ghonta
#### Django full functional newsportal web application.

![Image of homeage of this repository](https://github.com/nasim-007/nasimportfolio/blob/master/nasimp.png)

#### Prerequisite:
###### 1: python 3.8
# How to install:
###### Download or clone the reposatory. Goto project root folder.

```
C:\>git clone https://github.com/nasim-007/khobor24ghonta.git

C:\>cd khobor24ghonta

C:\khobor24ghonta>virtualenv venv

C:\khobor24ghonta>cd venv

C:\khobor24ghonta\venv>scripts\activate.bat

(venv)C:\khobor24ghonta\venv>cd ..

(venv)C:\khobor24ghonta>pip freeze > requirements.txt

(venv)C:\khobor24ghonta>pip install -r requirements.txt

(venv)C:\khobor24ghonta>python manage.py migrate

(venv)C:\khobor24ghonta>python manage.py runserver
```

```
### It will start a local server on 'http://localhost:8000'
```

###### create a super user using,
```
(venv)C:\khobor24ghonta>python manage.py createsuperuser
```
###### then go to http://localhost:8000/admin to accesss your administrations to control your dynamic application.


###### It's ready to deploy in heroku.Before deploy in heroku, change the local database in settings.py according to:
###### You will find database settings like this.
```
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   
   }

}
```

###### You need to change it like below,

```
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
       
        'NAME': 'example_db',
        
        'USER': 'your user',
        
        'PASSWORD': 'your password',
        
        'HOST': 'localhost',
        
        'PORT': '2000',
        
    }

}
```
```
###### Congrats! everything is setup. Your project ready to deploy in heroku for live your project online.
Get any error, send me the scrrenshot at my inbox, i will try to give you the solution.
Facebook: https://facebook.com/Nasim.nimu2011
Email: nasim.mahmud.1996@gmail.com
Phone: 01777-424142
```
