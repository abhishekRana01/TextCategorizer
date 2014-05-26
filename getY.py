from getPostcategories import getPostcategories
from imports import *

def getY(db,offset,limit):
    postcats = getPostcategories(db,offset,limit)
    return postcats
