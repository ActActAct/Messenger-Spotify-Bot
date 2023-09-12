from flask import Flask, request
import requests

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'
VERIFY_TOKEN = 'YOUR_VERIFY_TOKEN'  # This can be any random string, but must match the token you put into the Facebook webhook setup.


@app.route('/', methods=['GET'])
def handle_verification():
    if request.args.get('hub.verify_token', '') == VERIFY_TOKEN:
        return request.args.get('hub.challenge', '')
    else:
        return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']

    send_message(sender, message)  # Echoes back the message to the sender.

    return "ok"


def send_message(recipient_id, message_text):
    payload = {
        'message': {
            'text': message_text
        },
        'recipient': {
            'id': recipient_id
        },
        'notification_type': 'regular'
    }

    auth = {
        'access_token': PAGE_ACCESS_TOKEN
    }

    response = requests.post(
        'https://graph.facebook.com/v2.6/me/messages',
        params=auth,
        json=payload
    )

    return response.json()


if __name__ == '__main__':
    app.run(debug=True)
