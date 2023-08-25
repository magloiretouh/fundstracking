# TripFundsTracker
Trip Funds Tracker Project
# Create database before execute below commands

flask db init
flask db migrate -m "Initial migration." ||||||||||||||||||| flask db migrate
flask db upgrade
flask run --host=0.0.0.0


# To update db schema
flask db migrate
flask db upgrade

# To delete migrations created using flask db migrate
Go to migrations folder and deleted generated text file in versions folder

# To delete last upgrade
flask db downgrade