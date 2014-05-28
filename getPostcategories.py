from imports import *

def getPostcategories(db,offset,limit):
    cur = db.cursor()
    sql = """SELECT post_category FROM wp_posts 
where post_type = 'normal' 
and post_status = 'publish' 
LIMIT %s OFFSET %s"""
    cur.execute(sql, (limit, offset))
    data = cur.fetchall()
    pc = map(list,data)             #List for storing post categories
    cur.close()
    return list(itertools.chain.from_iterable(pc))
