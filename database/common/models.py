import peewee as pw
from datetime import datetime

db = pw.SqliteDatabase('request_history.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    yars = pw.TextField()
    rat_kp = pw.TextField()
    sort = pw.TextField()
