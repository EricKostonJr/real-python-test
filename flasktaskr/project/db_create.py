# project/db_create.py


from views import db
from models import Task
from datetime import date

# create the database and the db table
db.create_all()

# insert data
# db.session.add(Task("Finish flasktaskr tutorial", date(2020, 6, 21), 10, 1))
# db.session.add(Task("Finish Real Python Course 2", date(2020, 7, 20), 10, 1))

# commit the changes
db.session.commit()