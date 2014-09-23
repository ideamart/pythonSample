pythonSample
============

*www.ideamart.lk*

## Requirement ##
- Python
- Flask - [http://flask.pocoo.org/docs/0.10/installation/](http://flask.pocoo.org/docs/0.10/installation/)
- Requests - [http://docs.python-requests.org/en/latest/](http://docs.python-requests.org/en/latest/)

you can install flask, requests,and JSON via PIP

## USSD IN ##

    {
      "message": "992",
      "ussdOperation": "mo-init",
      "requestId": "071408010207151318",
      "sessionId": "140801020715000",
      "encoding": "0",
      "applicationId": "APP_005649",
      "sourceAddress": "tel:B%3C4pbgsmEfcKETtTtCwleOTKc4HUXWhO0mkzDaMvEvxY60zs2AAGFY576MQHPFh2YUe",
      "version": "1.0"
    }

## USSD OUT ##
    {
      "message": "Welcome To Track Sri Lanka Postal Tracking Codes\r\n\r\nEnter Tracking\/Barcode of your EMS\/Parcel\/Document",
      "ussdOperation": "mt-cont",
      "applicationId": "APP_AAAAA",
      "password": "xxxxxxxxxxxxx",
      "version": "1.0",
      "sessionId": "140801020715000",
      "destinationAddress": "tel:B%3C4pbgsmEfcKETtTtCwleOTKc4HUXWhO0mkzDaMvEvxY60zs2AAGFY576MQHPFh2YUe",
      "encoding": "440",
      "chargingAmount": 0
    }


## SMS IN ##

    {
      "message": "TRACK RF007870236Lk",
      "requestId": "071408111102268264",
      "encoding": "0",
      "applicationId": "APP_AAAAA",
      "sourceAddress": "tel:B%3C4Nw4BKrMN5isVODdpmlqlHhYHpWQIgZqISKHl6cvfqocwK6Pfbpm3FrRylnai2st2",
      "version": "1.0"
    }


## SMS OUT ##
    {
      "message": "Tracking Detail for : \r\nRF007870236LK\r\nClass:LETTERS (LC\/AO)\r\nFrom:SRI LANKA\r\nDestination:AUSTRALIA\r\nState:Dispatch\/Transit (60%)\r\nLast:LOCAL(LKCMBA)\r\n2014-08-02 10:27:34",
      "applicationId": "APP_005649",
      "password": "xxxxxxxxxxxxx",
      "version": "1.0",
      "deliveryStatusRequest": 1,
      "destinationAddresses": [
    "tel:B%3C4Nw4BKrMN5isVODdpmlqlHhYHpWQIgZqISKHl6cvfqocwK6Pfbpm3FrRylnai2st2"
      ],
      "encoding": "0",
      "chargingAmount": 2
    }
    