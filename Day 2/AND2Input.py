
import random;
import numpy as np;
def ANDGate():
    inputs=np.array([[0,0],[0,1],[1,0],[1,1]]);
    test=[0,0,0,1];
    w0=random.uniform(-1,1);
    w1=random.uniform(-1,1);
    w2=random.uniform(-1,1);
    x0=-1;
    eta=random.random();
    epochs=int(input("Enter no of epochs: "));
    for i in range(epochs):
        weights=[];
        output=[];
        for j in range(4):
            sum=0;
            x1=inputs[j][0];
            x2=inputs[j][1];
            sum=w0*x0+w1*x1+w2*x2;
            if(sum >=0):
                y=1;
            else:
                y=0;
            output.append(y);
            weights.append([w0,w1,w2]);
            if(test[j]!=y):
                w0=w0-eta*(y-test[j])*x0;
                w1=w1-eta*(y-test[j])*x1;
                w2=w2-eta*(y-test[j])*x2;
        print("This is epoch number: ",i);
        print(" ");
        print("eta is: ",eta);
        print(" ");
        print("The weights are: ",np.array(weights));
        print(" ");
        print("The y caps are: ", np.array(output));
        print("_____________________________________________________________________________________________________________________________");

if(__name__=="__main__"):
    ANDGate();
