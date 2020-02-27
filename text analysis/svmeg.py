__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.02, C=1.5)

print(len(digits.data))

x, y = digits.data[0:1438], digits.target[0:1438]
classifier.fit(x, y)

print('Prediction:', classifier.predict(digits.data[1787:1797]))
# for i in range(1788,1797):
predice = classifier.predict(digits.data[1787:1797])
target = digits.target[1787:1797]
plt.imshow(digits.images[1795], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
same_count = 0
for i in range(len(target)):
    if target[i] == predice[i]:
        same_count = same_count+1
accuracy = same_count/10
print(accuracy)