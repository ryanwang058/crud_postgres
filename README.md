initialize virtual environment
$ python3 -m venv venv

activate virtual environment
$ source venv/bin/activate

install dependencies
$ pip install -r requirements.txt

create a .env file
e.g.,
DB_NAME=3005
DB_HOST=localhost
DB_USER=student
DB_PASSWORD=123456
DB_PORT=5432

run the program
$ python app.py

deactivate
$ deactivate