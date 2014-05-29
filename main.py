from getX import getX
from train import train
from predict import predict
from getPostcategories import getPostcategories
from getPostIds import getPostIds
from prcntagaccurcy import prcntagaccurcy
from imports import *
from getPostEntities import getPostEntities
from getcountEntities import getcountEntities
start = timeit.default_timer()

def main():
    db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="xataka")

    postids = getPostIds(db,0,5)
    postentities =  getPostEntities(db,postids)

    columns = getcountEntities(db)

    X_train = getX(postids,postentities,columns)
    Y_train = getPostcategories(db , 0 ,5)

    train(X_train,Y_train,100)
    prediction = predict(X_train,100)
    
    acc = prcntagaccurcy(prediction,Y_train)           ## calculate the accuracy of classifier
    print "Accuracy :", acc , "%"
    
    stop = timeit.default_timer()                      ## calculate time taken by program to run
    print "Time Taken :", stop-start, "seconds"         
    
if __name__ == "__main__" :
    main()
