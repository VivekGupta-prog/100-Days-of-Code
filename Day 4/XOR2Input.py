import random;
import numpy as np;

def XORGate():
    epochs=int(input("Enter no of epochs: "));
    w0=random.uniform(-1,1);
    w1=random.uniform(-1,1);
    w2=random.uniform(-1,1);
    eta=random.random();
    inputs=np.array([[0,0],[0,1],[1,0],[1,1]]);
    print("Inputs are: ", inputs);
    print(" ");
    test=[0,1,1,0];
    x0=-1;
    for i in range(epochs):
        weights=[];
        outputs=[];
        sum=0;
        for j in range(4):
            x1=inputs[j][0];
            x2=inputs[j][1];
            sum=w0*x0+w1*x1+w2*x2;
            weights.append([w0,w1,w2]);
            if(sum>=0):
                y=1;
            else:
                y=0;
            outputs.append(y);
            if(test[j]!=y):
                w0=w0-eta*(y-test[j])*x0;
                w1=w1-eta*(y-test[j])*x1;
                w2=w2-eta*(y-test[j])*x2;
        print("This is epoch number: ", i);
        print(" ");
        print("Eta is: ", eta);
        print(" ");
        print("Weights are: ", np.array(weights));
        print(" ");
        print("Outputs are: ", np.array(outputs));
        print("_________________________________________________________________________");

if(__name__=="__main__"):
    XORGate();
