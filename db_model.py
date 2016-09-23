from peewee import *


db = PostgresqlDatabase('sprint reporter')


class UserStory(Model):
    story_title = CharField()
    user_story = TextField()
    criteria = TextField()
    business_value = IntegerField()
    estimation_time = FloatField()
    status = TextField()

    class Meta:
        database = db


def create_tables():
    db.create_tables([UserStory], safe=True)
