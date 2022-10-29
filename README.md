# Bain Machine Learning Engineer Challenge
This repository presents my approach to the challenge proposed. The goal is to build a robust, maintainable, and scalable solution for the milk price forecasting model. Also, I want to document some flaws encountered in the source jupyter notebook code that were ignored but, in a real-world scenario, would potentially be a risk factor. 

**The python version used for this project was 3.9.12**

### TLDR Running the code
To run this code, you must install tox (https://tox.wiki/en/latest/), a python package for testing in isolated environments.

```pip install tox```

With tox installed, you can go to the source directory (the same folder where tox.ini is located) and run 

```tox```

To install all necessary packages and run the whole pipeline.
You can run the test pipeline by executing:

```tox -e test_package```

It is also possible to run only the train pipeline by executing the command:

```tox -e train```

And finally, if you want to only host the API locally:

```tox -e run_app```

To build and run the docker images, you have to use the following commands:

```docker build -t bain-ml-challenge:latest .```

```docker run -p 8001:8001 -e PORT=8001 bain-ml-challenge```

# Potential risks found in the development

### Issue 1)
The jupyter notebook imports modules that were not present in the source code. Fortunately, the code did not utilize the module.

### Issue 2)
The Data Scientist uses TrainTestSplit to separate the training and test set. TrainTestSplit randomly samples the data, which is a good approach to develop models where observations are IID, which is not valid for time series data. Because the data scientist used TrainTestSplit to split the training and test set, there is a high risk of data leakage and inflated metric results. A simple solution for this could be using a certain period as the trainig set, and all data beyond that date as test set.

### Issue 3)
The source code appears to have more features than what was created in the presented jupyter notebook. The Data Scientist developed more features, such as moving averages and the actual value from the previous month.

### Issue 4)
A minor issue found is how RMSE was calculated. The source code only computes the mean squared error, but the root squared is not taken.

