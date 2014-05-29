from getPostIds import getPostIds
from getPostEntities import getPostEntities
from getcountEntities import getcountEntities
from imports import *

def getX(postids,postentities,columns):
    row = []
    col = []
    i = 0
    j = 0
    temp = []
    n = len(postentities)
    data = [1]*n
    col  =  postentities[0:n , 1]
    col  =  col-1
    col = col.tolist()
    temp =  postentities[0:n , 0].tolist()
    for item in postids:
        count = temp.count(item)
        l = [j]*count
        row.extend(l)
        j += 1

    if not row:
        nrow = 1
    else:
        nrow = max(row) + 1
    ncol =  columns
    csr  =  csr_matrix( (data,(row,col)), shape=(nrow,ncol) )
    return csr
