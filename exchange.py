# 
# exchange.py - an application to retrieve currency rates
# 
# Exchange JSON API Credit - fixer.io
#



# external modules

import requests
import json



# variables

source_curr = None

target_curr = None

value = None

response = None

curr_dict = None

unofficial_currencies = {}

result = None

supported_currencies = json.loads(requests.get("http://api.fixer.io/latest?base=EUR").text)["rates"].keys()

supported_currencies.sort()



# helper functions

def src_to_tgt_currency(source, target, value):

    # hard-coded exchange rates for
    # currencies not found in fixer.io

    if source == "USD" and target == "QAR":

        return value * 3.65

    elif source == "QAR" and target == "USD":

        return value * 0.27

    response = requests.get("http://api.fixer.io/latest?base=" + source)

    rates_dict = json.loads(response.text)

    return value * rates_dict["rates"][target]



# sample user interface

def main():

    print

    print "Supported currencies are..."

    print

    for curr in supported_currencies:

        print curr

    print

    source_curr = str(raw_input("Source currency: "))

    target_curr = str(raw_input("Target currency: "))

    print

    value = float(raw_input("Value in " + source_curr + ": "))

    result = src_to_tgt_currency(source_curr, target_curr, value)

    print

    print str(value) + " " + source_curr + " --> " + str(result) + " " + target_curr + "\n"

