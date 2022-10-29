# Bain Machine Learning Engineer Challenge
This repository presents my approach to the challenge proposed. The goal is to build a robust, maintainable, and scalable solution for the milk price forecasting model. Also, I want to document some flaws encountered in the source jupyter notebook code that were ignored but, in a real-world scenario, would potentially be a risk factor.

### TLDR Running the code
To run this code, you must install tox (https://tox.wiki/en/latest/), a python package for testing in isolated environments.

```pip install tox```

With tox installed, you can go to the source directory (the same folder where tox.ini is located) and run 

```tox```

To install all necessary packages and tests.
To only train the model, you can run:

```tox -e train```

And finally, if you want to run the API locally, you can run:

```tox -e run_app```

To build and run the docker images, you have to use the following commands:

```docker build -t bain-ml-challenge:latest .```

```docker run -p 8001:8001 -e PORT=8001 bain-ml-challenge```

### Issue 1)
The jupyter notebook imports modules that were not present in the source code. Fortunately, the code did not utilize the module.

### Issue 2)
The Data Scientist uses TrainTestSplit to separate the training and test set. TrainTestSplit randomly samples the data, assuming that the observations are independent, which is not valid for time series data. The way the model is currently developed, there is a high potential for data leakage and inflated results. A straightforward solution for this could be dividing the data by periods.

### Issue 3)
The source code appears to have more features than what was created in the presented jupyter notebook. The Data Scientist developed more features, such as moving averages and the actual value from the previous month.

### Issue 4)
A minor issue found is how RMSE was calculated. The presented code only computes the mean squared error, but the root squared is not taken.

