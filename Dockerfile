FROM python:3.9.13

# create the user (best practice) that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/bain_ml_challenge_model

# this command copies from local to target (/opt/bain_ml_challenge_model) directory
ADD ./ /opt/bain_ml_challenge_model/ 

RUN pip install --upgrade pip
RUN pip install -r /opt/bain_ml_challenge_model/requirements.txt
RUN pip install tox

RUN chmod +x /opt/bain_ml_challenge_model/run.sh
# set the user
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

# opens the 8001 port
EXPOSE 8001

RUN tox

CMD ["bash", "./run.sh"]