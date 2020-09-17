import sklearn.datasets;
import numpy as np;

#Loading datasets
b_cancer=sklearn.datasets.load_breast_cancer();
X=b_cancer.data
Y=b_cancer.target

#Storing the datasets as DataFrame
import pandas as pd
data=pd.DataFrame(b_cancer.data, columns=b_cancer.feature_names)
data['class']=b_cancer.target
data['class'].value_counts()
from sklearn.model_selection import train_test_split
X=data.drop('class', axis=1)
Y=data['class']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=1)

#Ploting the graphs of the taken dataset
import matplotlib.pyplot as plt
plt.plot(X_test,'*')
plt.show()
plt.plot(X_test.T,'*')
plt.show()
plt.xticks(rotation='vertical')
plt.show()

#Converting data into Binary
testing_bin=X_test['mean area'].map(lambda x: 0 if x < 1000 else 1)
plt.plot(testing_bin,'*')
plt.show()

#Using pandas function for the converion
X_bin_train=X_train.apply(pd.cut, bins=2, labels=[1,0])
X_bin_test=X_test.apply(pd.cut, bins=2, labels=[1,0])

#COnverting into numpy arrays
X_bin_train=X_bin_train.values
X_bin_test=X_bin_test.values

#MP Neuron model
best_accuracy=0
best_theta=0

#Calculating the best value of theta with best accuracy within the provided range
from random import randint
i=randint(0,X_bin_train.shape[0])
for k in range(1,31):
    theta=k;
    print("Theta is: ",theta)
    if(np.sum(X_bin_train[i,:])>=theta):
       print("MP Neuron says: Malignant")
    else:
        print("MP Neuron says: Benign")
    if Y_train[i]==1:
        print("Reality is that patient is Malignant")
    else:
        print("Reality is that patient is Benign")
    #Finding the accuracy of the model
    y_pred_train=[]
    correct_detection=0
    for x,y in zip(X_bin_train,Y_train):
        y_pred=(np.sum(x)>=theta)
        y_pred_train.append(y_pred)
        correct_detection += (y_pred==y)
    print("Correct Detection: ",correct_detection)
    #accuracy = correct_detection/(total number of patients)
    print("Accuracy is: ", correct_detection/512)
    if(best_accuracy < correct_detection/512):
        best_theta=theta
        best_accuracy=correct_detection/512
    print(" ")

print("__________________________________________________________________")
print(" ")

#Testing the calculated best value of theta in the test conditions
print("On Test Data:")
y_pred_test=[]
correct_detection=0
for x,y in zip(X_bin_test,Y_test):
    y_pred=(np.sum(x)>=best_theta)
    y_pred_test.append(y_pred)
    correct_detection += (y_pred==y)
print("Correct Detection: ",correct_detection)
print("Accuracy is: ", correct_detection/512)
