from flask_socketio import Namespace, join_room, leave_room, send
from flask_login import current_user


class Chat(Namespace):
    def on_joined(self, message):
        print(current_user.username + message)

    def on_message(self, data):
        data['user'] = current_user.username
        room = data['room']
        send(data, room=room)

    def on_join_room(self, data):
        data['user'] = current_user.username
        room = data['room']
        data['message'] = 'Joined the room'
        join_room(room)
        send(data, room=room)

    def on_leave_room(self, data):
        data['user'] = current_user.username
        room = data['room']
        data['message'] = 'Left the room'
        leave_room(room)
        send(data, room=room)
