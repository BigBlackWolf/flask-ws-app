from flask_socketio import emit, Namespace, join_room, leave_room, send
from flask_login import current_user


class Chat(Namespace):
    def on_joined(self, message):
        print(current_user.username + message)
        emit('status', {'data': 'Hello'})

    def on_message(self, data):
        data['user'] = current_user.username
        send(data, room=data['room'])

    def on_join_room(self, data):
        username = current_user.username
        room = data['room']
        join_room(room)
        send(username + ' has joined the room', room=room)

    def on_leave_room(self, data):
        username = current_user.username
        room = data['room']
        leave_room(room)
        send(username + ' has left the room', room=room)
