from flask import Flask

import sys
from card.logger import logging
from card.exception import HousingException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        card = HousingException(e,sys)
        logging.info(card.error_message)
        logging.info("We are testing logging module")
    return " hi sir, im sadish 1year of M.Sc.,, i complete all the machine learning pipeline but i facing some issuse in it (model evalution part)
            incomplete  app.py file and html page.
            
            
            i done the beatifully EDA and MODEL and make the best accuracy using the bar plot 
            that link is   https://github.com/sadishpitchandi/PYTHON-BASIC-PROGRAM/blob/main/Eda%2C%20models.ipynb 
            
            i fresher it take the lot of time sir 
            
            and i trying to solve the errors "

if __name__=="__main__":
    app.run(debug=True)