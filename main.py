from sqlalchemy import create_engine, func
from models import students, Base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from random import randint

engine = create_engine('sqlite:///students.db')
session = Session(bind=engine)
student = list()
student.append(students(
    name = 'Islam',
    second_name = 'Uzakbek',
    hobbie = 'programming',
    birth_year = datetime(2004, 4, 9),
    marks = 20
))
# Base.metadata.create_all(engine)
student.append(students(name='Nuraaly', second_name='Melisbekov', hobbie = 'programming', birth_year = datetime(2005, 3, 1), marks = 15))
student.append(students(name='Argen', second_name='Toktorbaev', hobbie = 'boxing', birth_year = datetime(2005, 11, 12), marks = 16))
student.append(students(name='Azamat', second_name='Bashkirov', hobbie = 'learning', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Abil', second_name='Tokoev', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Bakyt', second_name='Mambetaliev', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Magomed', second_name='Omarov', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Nursultan', second_name='Erlanov', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Iskander', second_name='Bakytbekov', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))
student.append(students(name='Eliza', second_name='Gaparova', hobbie = 'programming', birth_year = datetime(randint(2001, 2007), randint(1, 12), randint(1, 30)), marks = randint(0, 20)))

# session.add_all(student)
# ,ession.commit()
even_10symbols = session.query(students).filter(func.length(students.second_name) >= 10).all()
for i in even_10symbols:
    print(i.second_name)
    
print('\n\n\ngeniuses:')

geniuses = session.query(students).filter(students.marks >= 10).all()
for item in geniuses:
    print(item.name)
    item.name = 'Genius'

session.commit()


