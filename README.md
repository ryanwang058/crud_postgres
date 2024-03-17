## How to use the proram

### Python setup

1. Initialize virtual environment

    $ python3 -m venv venv

2. Activate virtual environment

    $ source venv/bin/activate

3. Install dependencies

    $ pip install -r requirements.txt

4. Deactivate virtual environment

    $ deactivate

### Databse setup

1. Create a `.env` file containing information of your database
e.g.,

    ```
    DB_NAME=3005
    DB_HOST=localhost
    DB_USER=student
    DB_PASSWORD=123456
    DB_PORT=5432
    ```

2. Create a database named `DB_NAME` using pgAdmin

3. Populate the database with the provided `schema.sql` using pgAdmin

### Run the program

1. Activate virtual environment

    $ source venv/bin/activate

2. Execute the program

    $ python app.py

3. In the program, enter numnber (1 for READ, 2 for ADD, 3 for UPDATE, 4 for DELETE, q to Quit) to test the CRUD operations. Check the effects in the database using pgAdmin.

4. Deactivate the virtual environment

    $ deactivate