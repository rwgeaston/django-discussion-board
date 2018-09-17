Discussion board related to "entities".

summary
-------

models are
- entities (guid only under assumption other details are stored elsewhere)
- users
- threads, owned by a user and can be associated with an entity
- messages, messages in order within a thread

and there are REST APIs for each of these.

    /api/users/
    /api/users/robert/threads/
    /api/threads/
    /api/threads/1/messages/
    /api/entities/1234/threads/

and some others

setup
------

Make a local_settings.py in main folder with values like:

    DEBUG=True

    SECRET_KEY='something secret'
    
    ALLOWED_HOSTS = ['0.0.0.0']

then run

    docker-compose up
    
to run the server but as a one off you need to do 

    docker-compose exec web python app/manage.py migrate

(leave docker-compose up while doing this.)

you can also do 

    docker-compose exec web python app/manage.py test

to run the tests.

Precommit hook runs pylint which I advise doing in a python3.6 virtualenv (pip install -r local_requirements.txt in this).
