from flask_socketio import emit, Namespace
from flask_login import current_user


class Chat(Namespace):
    def on_joined(self, message):
        print(message)
        emit('status', {'data': 'Hello'})

    def on_message(self, data):
        data['user'] = current_user.username
        emit('received_message', data)
