import random;
import numpy as np;

def NORGate():
    w0=random.uniform(-1,1);
    w1=random.uniform(-1,1);
    w2=random.uniform(-1,1);
    epochs=int(input("Enter the number of epochs: "));
    eta=random.random();
    x0=-1;
    inputs=np.array([[0,0],[0,1],[1,0],[1,1]]);
    test=[1,0,0,0];
    for i in range(epochs):
        weights=[];
        outputs=[];
        for j in range(4):
            sum=0;
            x1=inputs[j][0];
            x2=inputs[j][1];
            sum=w0*x0+w1*x1+w2*x2;
            if(sum>=0):
                y=1;
            else:
                y=0;
            weights.append([w0,w1,w2]);
            outputs.append(y);
            if(y!=test[j]):
                w0=w0-eta*(y-test[j])*x0;
                w1=w1-eta*(y-test[j])*x1;
                w2=w2-eta*(y-test[j])*x2;
        print("This is epoch number: ", i);
        print(" ");
        print("Eta is: ",eta);
        print(" ");
        print("Weights are: ", np.array(weights));
        print(" ");
        print("Outputs are: ", np.array(outputs));
        print("_____________________________________________________________________________");

if(__name__=="__main__"):
    NORGate();
