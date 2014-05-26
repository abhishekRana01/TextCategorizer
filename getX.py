from getPostIds import getPostIds
from getPostEntities import getPostEntities
from getcountEntities import getcountEntities
from imports import *


def getX(db,offset,limit):
    row = []
    col = []
    data = []
    i = 0
    postids = getPostIds(db,offset,limit)
    for item in postids:
        k = getPostEntities(db,item)
        col.append(k)
        for j in range(len(k)):
            row.append(i)
            data.append(1)
        i += 1
    col  = list(itertools.chain.from_iterable(col))
    if not row:
        nrow = 1
    else:
        nrow = max(row) + 1
    ncol = getcountEntities(db)
    csr  =  csr_matrix( (data,(row,col)), shape=(nrow,ncol+1) )
    return csr
