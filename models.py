from peewee import *
import datetime


DATABASE = SqliteDatabase('journal.db')


class Entries(Model):
    title = TextField()
    dateCreated = DateTimeField(default=datetime.datetime.now)
    timeSpent = TextField()
    learned = TextField()
    resources = TextField()

    @classmethod
    def create_entry(cls, title, timeSpent, learned, resources, dateCreated):
        try:
            with DATABASE.transaction():
                cls.create(
                    title=title,
                    timeSpent=timeSpent,
                    learned=learned,
                    resources=resources,
                    dateCreated=dateCreated)
        except IntegrityError:
            raise ValueError("Entry already exists!")

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entries], safe=True)
    DATABASE.close()