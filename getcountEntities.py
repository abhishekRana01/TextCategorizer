from imports import *

def getcountEntities(db):
    cur = db.cursor()
    cur.execute("SELECT MAX(entity_id) from post2entity")
    data = cur.fetchone()
    return data[0]
