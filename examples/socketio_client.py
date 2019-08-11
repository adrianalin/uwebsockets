

import usocketio.client



def hello():
    with usocketio.client.connect('http://127.0.0.1:5000/') as socketio:
        @socketio.on('message')
        def on_message(message):
            print("message", message)

        @socketio.on('alert')
        def on_alert(message):
            print("alert", message)

        socketio.run_forever()

hello()
