from sqlalchemy import *


class ConnectHTMLSQL:
    def __init__(self):
        self.engine = create_engine('sqlite:///:memory:', echo=True)
        self.metadata = MetaData()
        self.conn = self.engine.connect()
        self.users = None
        self.e_books = None
        self.booking = None
        self.self_publishing = None

    def create_all_tables(self):

        users = Table('users', self.metadata,
                      Column('user_id', Integer, primary_key=True),
                      Column('name', String(20)),
                      Column('email', String(30)),
                      Column('phone_no', String(15)),
                      )
        self.users = users
        ebooks = Table('ebooks', self.metadata,
                       Column('book_id', Integer, primary_key=True),
                       Column('title', String),
                       Column('author', String),
                       Column('genre', String),
                       Column('release_date', String)
                       )
        self.e_books = ebooks
        booking = Table('booking', self.metadata,
                        Column('booking_id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.user_id')),
                        Column('book_id', None, ForeignKey('ebooks.book_id')),
                        Column('date', String)
                        )
        self.booking = booking
        self_publishing = Table('self publishing', self.metadata,
                                Column('entry_id', Integer, primary_key=True),
                                Column('user_id', ForeignKey('users.user_id')),
                                Column('book_id', ForeignKey('ebooks.book_id')),
                                Column('book_content', String)
                                )
        self.self_publishing = self_publishing
        self.metadata.create_all(self.engine)


    # def add_customer(self):
    #     self.users = Table('users', self.metadata,
    #                        Column('user_id'),
    #                        Column('name'),
    #                        Column('email'),
    #                        Column('phone_no'),
