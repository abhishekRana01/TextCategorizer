from getX import getX
from getY import getY
from train import train
from predict import predict
from getPostcategories import getPostcategories
from getPostIds import getPostIds
from prcntagaccurcy import prcntagaccurcy
from imports import *

start = timeit.default_timer()

def main():
    db = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="xataka")

    X_train = getX(db,0,20)                     ## getX returns the X matrix to by constructing it from posts starting with offset 0 and limited up to 20(1st and 2nd argument respectively)
    Y_train = getY(db,0,20)                     ## getY returns the Y matrix to by constructing it from post catgories starting with posts from offset 0 and limited up to 20(1st and 2nd argument respectively)
    
    X_test = getX(db,20,6)
    Y_test = getY(db,20,6)

    train(X_train,Y_train,100)                  ## train takes as arguments X,Y and batchsize
    pred = predict(X_test,Y_test,1000)          ## predict takes as arguments X,Y and batchsize
    acc = prcntagaccurcy(pred,Y_test)           ## calculate the accuracy of classifier
    print "Accuracy :", acc , "%"

    stop = timeit.default_timer()               ## calculate time taken by program to run
    print stop-start, "seconds"         


if __name__ == "__main__" :
    main()
