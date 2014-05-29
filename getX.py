from getPostIds import getPostIds
from getPostEntities import getPostEntities
from getcountEntities import getcountEntities
from imports import *

def getX(postentities,columns):
    row = []
    col = []
    data = []
    dict = {}
    count = 0
    for item in postentities:
        postid = item[0]
        if not dict.has_key(postid):
            dict[postid] = count;
            count += 1
        row.append(dict[postid])
        col.append(item[1]-1)
        data.append(1)
    nrow = len(dict)
    csr  =  csr_matrix( (data,(row,col)), shape=(nrow,columns) )
    print csr.todense()
    return csr
