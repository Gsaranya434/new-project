from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost/sql')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


def get_user_info():
    print('To a Person Details')
    sample_dict = {}
    book = ['Name','Mobile_Number', 'Location', 'Gmail']
    for x in book:
        get = input(x+': ')
        sample_dict.update({x: get})
    return sample_dict


class Create_Table(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, unique=True)
    phone_number = Column(String(10))
    address = Column(String(15))
    name = Column(String(20))
    gmail = Column(String(30))

    def __init__(self, app_data):
        self.phone_number = app_data['Mobile_Number']
        self.address = app_data['Location']
        self.name = app_data['Name']
        self.gmail = app_data['Gmail']

class Create(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True, unique=True)
    phone_number = Column(String(10))
    address = Column(String(15))
    name = Column(String(20))
    gmail = Column(String(30))

    def __init__(self, app_data):
        self.phone_number = app_data['Mobile_Number']
        self.address = app_data['Location']
        self.name = app_data['Name']
        self.gmail = app_data['Gmail']


Base.metadata.create_all(engine)
