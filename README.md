# Todo App - Web version

Todo app using django 3. 

# Running backend server

#### Clone this repository
```
$ git clone <https://github.com/gilsongindrejr/TodoApp-Web.git>
```

#### Access the project folder
```
$ cd TodoApp-Web
```

#### Activate the virtual enviroment
```
$ source venv/bin/activate
```

#### Install requirements
```
$ pip install -r requirements.txt
```

#### Migrate the database
```
$ python manage.py migrate
```

#### Run server
```
$ python manage.py runserver
```

#### The server will be initiated on port 8000 - access <http://127.0.0.1:8000> 

# Testing

The tests was made using django test module.


#### Run tests and show coverage
```
$ python manage.py test
```
