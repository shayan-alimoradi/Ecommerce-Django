# shop-app

*This repo implement a eshop app that uses **Django** as a backend framework foundation on **Python***

### Usage

**Requirements**

*Python3.8*

```
    1. Create a virtual environment via **virtualenv venv**.
    2. Activate venv through **source venv/bin/activate**.
    3. You must copy a sample of .env-sample in .env file with **cp .env-sample .env**.
    4. Install docker from:
      * [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
    5. Install docker-compose from:
      * [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
    6. Install rabbitmq from:
      * [https://www.rabbitmq.com/download.html](https://www.rabbitmq.com/download.html)
    7. install all of the requirements package via command **pip install -r requirements.txt**.
    8. Run the following command to get the database ready to go:

        python manage.py migrate
```

*Now you can run the project with **python manage.py runserver** and this site will be available on localhost://8000*

- - -

#### Run Service

```
docker-compose up -d
```