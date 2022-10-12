import sqlalchemy as db
from sqlalchemy.orm import Session


def get_order():
    owner_id = message.from_user.id
    engine = db.create_engine(f'sqlite:///D:/dev/DubnaHackaton/DubnaWebApp/db.sqlite3')
    session = Session(bind=engine)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table('webapp_order', metadata, autoload=True, autoload_with=engine)
    query = session.query(table).filter_by(owner_id=owner_id).first()
    return print(query)