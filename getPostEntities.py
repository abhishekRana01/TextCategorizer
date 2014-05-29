from imports import *

def getPostEntities(db,postids):
    cur = db.cursor()
    format_strings = ','.join(['%s'] * len(postids))
    cur.execute("SELECT * FROM post2entity WHERE post_id IN (%s)" % format_strings,tuple(postids))
    data = cur.fetchall()
    pc = map(list,data)
    cur.close()
    return np.array(pc)
