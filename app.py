##
## IDEAMART SAMPLE CODE
## FOR MORE 
## WWW.IDEAMART.LK
##

__author__ = 'Malinda'

from flask import Flask, render_template, request, jsonify

import requests
import json


api = "https://api.dialog.lk/"
appId = "APPID"
pw = "abc"
port = 9121

# Initialize the Flask application
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    inData = request.get_json(force=True)
    print(inData)

    msg = inData[u'message']
    user = inData[u'sourceAddress']

    out = u"Hi Welcome\n\nThank you for testing this app"

    data = {
        "message": out,
        "applicationId": appId,
        "password": pw,
        "version": "1.0",
        "deliveryStatusRequest": 0,
        "destinationAddresses": [user],
        "encoding": "440",
        "chargingAmount": 0
    }

    print json.dumps(data)
    headers = {'Content-type': 'application/json'}
    r = None
    try:
        r = requests.post(api + "sms/send", data=json.dumps(data), headers=headers)
        print(str(r.status_code) + ":" + r.content)
    except Exception, e:
        print('Failed to send: ' + str(e))

    response = {'statusCode': 'E1000', 'statusDetail': 'SUCCESS'}
    return jsonify(response)


@app.route('/ussd', methods=['POST'])
def ussd():
    inData = request.get_json(force=True)
    print(inData)
    msg = inData[u'message']
    user = inData[u'sourceAddress']
    state = inData[u'ussdOperation']
    session = inData[u'sessionId']

    out = ""
    outState = "mt-cont"

    if state == u'mo-init':
        out = "Welcome to Test Application.\r\nPlease select your feedback\r\n\r\n1. Good\r\n2. Bad"
    else:
        out = "Thank you for your feed back"
        outState = "mt-fin"

    data = {
        "message": out,
        "applicationId": appId,
        "password": pw,
        "version": "1.0",
        "destinationAddress": user,
        "encoding": "440",
        "chargingAmount": 0,
        "sessionId": session,
        "ussdOperation": outState
    }

    print json.dumps(data)
    headers = {'Content-type': 'application/json'}
    r = None
    try:
        r = requests.post(api + "ussd/send", data=json.dumps(data), headers=headers)
        print(str(r.status_code) + ":" + r.content)
    except Exception, e:
        print('Failed to send: ' + str(e))

    response = {'statusCode': 'E1000', 'statusDetail': 'SUCCESS'}
    return jsonify(response)


# Run
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=port
    )