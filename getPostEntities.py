from imports import *

def getPostEntities(db,post_id):
    cur = db.cursor()
    sql = "SELECT entity_id FROM post2entity where post_id = %d" %(post_id)
    cur.execute(sql)
    data = cur.fetchall()
    pc = map(list,data)             #List for storing post categories
    cur.close()
    return list(itertools.chain.from_iterable(pc))
