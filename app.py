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
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)