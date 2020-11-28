from mailjet_rest import Client
import os
api_key = 'dd29eeea3790ebe7cb2c776d1ff81afa'
api_secret = '9d7f73a0755756b22071fdade12d89a6'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "dylannguyen1000@gmail.com",
        "Name": "Dylan"
      },
      "To": [
        {
          "Email": "dylannguyen1000@gmail.com",
          "Name": "Dylan"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
