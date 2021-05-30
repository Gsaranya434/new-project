from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model import Create_Table, get_user_info, Create


class CRUD_sql:
    def __init__(self, clss):
        self.engine = create_engine('mysql+pymysql://root:@localhost/sql')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.Base = declarative_base()
        self.cls = clss

    def insert(self):
        get_dict = get_user_info()
        self.Base.metadata.create_all(self.engine)
        new_result = self.cls(get_dict)
        self.session.add(new_result)
        self.session.commit()

    def repeat(self):
        query = self.session.query(self.cls)
        for x in query:
            print([x.id], end='')
        get_data = input('which Id you like to read or update or delete : ')
        return get_data

    def read(self):
        try:
            get = self.repeat()
            new_query = self.session.query(self.cls).filter(self.cls.id == get)
        except Exception as err:
            return err
        finally:
            for x in new_query:
                print([x.id, x.name, x.gmail, x.address, x.phone_number])

    def update(self):
        try:
            get = self.repeat()
            new_query = self.session.query(self.cls).filter(self.cls.id == get)
        except Exception as err:
            return err
        else:
            for x in new_query:
                get_dict = get_user_info()
                x.name = get_dict['Name']
                x.phone_number = get_dict['Mobile_Number']
                x.gmail = get_dict['Gmail']
                x.address = get_dict['Location']
            self.session.commit()

    def delete(self):
        try:
            get = self.repeat()
            new_query = self.session.query(self.cls).filter(self.cls.id == get)
        except Exception as err:
            return err
        finally:
            for x in new_query:
                self.session.delete(x)
            self.session.commit()

    def main(self):
        get_data = input('----> enter the operation [1.Create 2.read 3.update 4.delete] <----:')
        if get_data == '1':
            self.insert()
        elif get_data == '2':
            self.read()
        elif get_data == '3':
            self.update()
        elif get_data == '4':
            self.delete()
        else:
            print('process finished')
        return self.main()


if __name__ == '__main__':
    call_class = CRUD_sql(Create)
    obj = call_class.main()