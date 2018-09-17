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

Not dockerised yet so not production ready:

- make a python3.6 virtualenv,
- pip install requirements
- make a local_settings.py file in same folder as settings with

    DEBUG=True

    SECRET_KEY='something secret'

- python app/manage.py migrate
- python app/manage.py runserver
