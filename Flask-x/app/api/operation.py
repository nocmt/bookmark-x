from app.api.models import db

def db_add(obj):
    db.session.add(obj)
    db.session.commit()