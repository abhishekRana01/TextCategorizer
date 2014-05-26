from imports import *

def getPostcategories(db,offset,limit):
    cur = db.cursor()
    cmmnd = "SELECT post_category FROM wp_posts where post_type = 'normal' and post_status = 'publish' LIMIT %d OFFSET %d" %(limit,offset)
    cur.execute(cmmnd)
    data = cur.fetchall()
    pc = map(list,data)             #List for storing post categories
    cur.close()
    db.commit()
    return list(itertools.chain.from_iterable(pc))
