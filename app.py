import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '396751364:AAEVQ_HrqYu1xH0H_zlZTdhgLkqKjQql6KY'
WEBHOOK_URL = 'https://c16ccd0d.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'animalia','chordata','mammalia','primates','hominidae',
        'homo','sapiens',
        'plantae','angiosperms','sapindales','mangifera','indica',
        'bacteria','firmicutes','bacilli','lactobacillales',
        'lactobacillaceae','lactobacillus','acidophilus'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'animalia',
            'conditions': 'to_animalia'
        },
        {
            'trigger': 'advance',
            'source': 'animalia',
            'dest': 'chordata',
            'conditions': 'to_chordata'
        },
        {
            'trigger': 'advance',
            'source': 'chordata',
            'dest': 'mammalia',
            'conditions': 'to_mammalia'
        },
        {
            'trigger': 'advance',
            'source': 'mammalia',
            'dest': 'primates',
            'conditions': 'to_primates'
        },
        {
            'trigger': 'advance',
            'source': 'primates',
            'dest': 'hominidae',
            'conditions': 'to_hominidae'
        },
        {
            'trigger': 'advance',
            'source': 'hominidae',
            'dest': 'homo',
            'conditions': 'to_homo'
        },
        {
            'trigger': 'advance',
            'source': 'homo',
            'dest': 'sapiens',
            'conditions': 'to_sapiens'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'plantae',
            'conditions': 'to_plantae'
        },
        {
            'trigger': 'advance',
            'source': 'plantae',
            'dest': 'angiosperms',
            'conditions': 'to_angiosperms'
        },
        {
            'trigger': 'advance',
            'source': 'angiosperms',
            'dest': 'sapindales',
            'conditions': 'to_sapindales'
        },
        {
            'trigger': 'advance',
            'source': 'sapindales',
            'dest': 'mangifera',
            'conditions': 'to_mangifera'
        },
        {
            'trigger': 'advance',
            'source': 'mangifera',
            'dest': 'indica',
            'conditions': 'to_indica'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'bacteria',
            'conditions': 'to_bacteria'
        },
        {
            'trigger': 'advance',
            'source': 'bacteria',
            'dest': 'firmicutes',
            'conditions': 'to_firmicutes'
        },
        {
            'trigger': 'advance',
            'source': 'firmicutes',
            'dest': 'bacilli',
            'conditions': 'to_bacilli'
        },
        {
            'trigger': 'advance',
            'source': 'bacilli',
            'dest': 'lactobacillales',
            'conditions': 'to_lactobacillales'
        },
        {
            'trigger': 'advance',
            'source': 'lactobacillales',
            'dest': 'lactobacillaceae',
            'conditions': 'to_lactobacillaceae'
        },
        {
            'trigger': 'advance',
            'source': 'lactobacillaceae',
            'dest': 'lactobacillus',
            'conditions': 'to_lactobacillus'
        },
        {
            'trigger': 'advance',
            'source': 'lactobacillus',
            'dest': 'acidophilus',
            'conditions': 'to_acidophilus'
        },
        {
            'trigger': 'go_back',
            'source': [
                's1',
                'state2'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
