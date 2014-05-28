from imports import *

def getPostIds(db,offset,limit):
    cur = db.cursor()
    cmmnd = "SELECT id FROM wp_posts where post_type = 'normal' and post_status = 'publish' LIMIT %d OFFSET %d" %(limit,offset)
    cur.execute(cmmnd)
    data = cur.fetchall()
    pc = map(list,data)             #List for storing post categories
    cur.close()
    return list(itertools.chain.from_iterable(pc))
