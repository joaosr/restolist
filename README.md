## Restaurant list


### Setup Commands

  - to install the dependencies:

  ```sh
  $ pip install -r requirements.txt
  ```
  or
  ```sh
  $ pipenv install
  ```

  - database setup:

  ```sh
  $ python manage.py migrate
  $ python manage.py loaddata core/fixtures/restaurants.json
  ```
