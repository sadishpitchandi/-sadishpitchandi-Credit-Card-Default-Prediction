from flask import Flask

import sys
from card.logger import logging
from card.exception import CardException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        card = CardException(e,sys)
        logging.info(card.error_message)
        logging.info("We are testing logging module")
    return " completed the model evaultion "

if __name__=="__main__":
    app.run(debug=True)