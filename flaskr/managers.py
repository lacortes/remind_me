import os
from twilio.rest import Client


class TwilioManager(object):
    _instance = None

    def __init__(self):
        if TwilioManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_TOKEN'))
            self._from = '+13239486279'
            TwilioManager._instance = self

    @staticmethod
    def get_instance():
        if TwilioManager._instance is None:
            TwilioManager()
        return TwilioManager._instance

    def send_txt_message(self, msg, number):
        try:
            self._client.messages.create(
                from_=self._from,
                body=msg,
                to=number
            )
        except Exception as e:
            print('Error: ', e)
