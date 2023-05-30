from database.utils.list_commands import Interface_DB
from database.common.models import db, History

db.connect()
db.create_tables([History])

inter_db = Interface_DB()


if __name__=="main":
    inter_db()
