# Bain Machine Learning Engineer Challenge
This repository presents my approach to the challenge proposed. The goal is to build a robust, maintainable, and scalable solution for the milk price forecasting model. I also document some flaws encountered in the source code on jupyter notebook code that were ignored here, but in a real-world scenario, would potentially be a risk factor. 

**The python version used for this project was 3.9.12. Please, run this code using any version above 3.9.**

### Running the code
To run this code, you only need to install tox (https://tox.wiki/en/latest/), a python package for testing in isolated environments.

```$ pip install tox```

With tox installed, you have to go to the source directory (the same folder where tox.ini is located) and run 

```$ tox```

To install all necessary packages and run the whole pipeline in an isolated environment
You can run the test pipeline by executing:

```$ tox -e test_package```

It is also possible to run only the train pipeline by executing the command:

```$ tox -e train```

And finally, if you want to only host the API locally:

```$ tox -e run_app```

To build and run the docker images, you have to use the following commands:

```$ docker build -t bain-ml-challenge:latest .```

```$ docker run -p 8001:8001 -e PORT=8001 bain-ml-challenge```

The **0.0.0.0:8001** might not work, but **localhost:8001** will work just fine.

When accessing the api and you will see the message: "Bain ML Challenge API Check the docs: here". By clicking on 'here' you will be sent to the Swagger UI, where you can test the API and see its inputs.

# Key points
All of the relevant code is located in the src.
- The preprocessing script is **src/pipeline.py**
- The training script is **src/train_pipeline.py**
- Prediction script is **src/predict.py**
- App script is **src/app.py**

# How I tackled this problem

First, I implemented the preprocessing pipeline using scikit-learn pipeline transformers for each dataset.

To train the model, I followed the same steps in the jupyter notebook, focusing only on the machine learning model and not on the plot.

To make the inference, I developed a data validation script to ensure data consistency across the data flow.

Finally, the application script was developed using FastAPI. The good thing about using FastAPI with pydantic is that pydantic can automatically convert data types to the correct ones when used with FastAPI. Another great advantage of using FastAPI is that it provides a swagger out of the box just by using the module.

# Potential risks found in the development

### Issue 1)
The jupyter notebook imports modules that were not present in the source code. Fortunately, the code did not utilize the module.

### Issue 2)
The Data Scientist uses TrainTestSplit to separate the training and test set. TrainTestSplit randomly samples the data, which is a good approach to develop models where observations are IID, which is not valid for time series data. Because the data scientist used TrainTestSplit to split the training and test set, there is a high risk of data leakage and inflated metric results. A simple solution for this could be using a certain period as the trainig set, and all data beyond that date as test set.

The same applies to the model used, which was ridge regression. Although this is not a big of an issue like using TrainTestSplit, using time series models might improve performance of predictions.

### Issue 3)
The source code appears to have more features than what was created in the presented jupyter notebook. The Data Scientist developed more features, such as moving averages and the actual value from the previous month.

### Issue 4)
A minor issue found is how RMSE was calculated. The source code only computes the mean squared error, but the root squared is not taken.

