import os 
import numpy as n

## finding parameter in regression
def linear(ind,dep):
    x=n.array(ind)
    y=n.array(dep)
    b1=(((n.mean(x)*n.mean(y))-n.mean(x*y))/((n.mean(x)*n.mean(x))-n.mean(x*x)))
    b1=round(b1,2)
    b0=(n.mean(y)-n.mean(x)*b1)
    b0=round(b0,2)

    return (b0,b1)

x=[40,60,70,80,50,20]
y=[1,2,3,4,5,6]  
b0,b1=linear(x,y) 
print("the model is y=",b1,"*x+",b0)

##Prediction of Y
y_predict= n.array([b0+(b1*x)for x in x])
print("the predicted value is",y_predict)

##Finding error terms
def error(y,y_predict):
    e=(y-y_predict)**2
    e_mean=n.mean(e)
    error=n.sqrt(e_mean)
    return(print(" Error :",error))
error(y,y_predict)    


