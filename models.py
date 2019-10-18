from peewee import *
import datetime


DATABASE = SqliteDatabase('journal.db')


class Entries(Model):
    title = TextField()
    dateCreated = DateField(default=datetime.datetime.now)
    timeSpent = IntegerField()
    learned = TextField()
    resources = TextField()

    @classmethod
    def create_entry(cls, title, timespent, learned, resources, datecreated):
        try:
            with DATABASE.transaction():
                cls.create(
                    title=title,
                    timeSpent=timespent,
                    learned=learned,
                    resources=resources,
                    dateCreated=datecreated)
        except IntegrityError:
            raise ValueError("Entry already exists!")

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entries], safe=True)
    DATABASE.close()
