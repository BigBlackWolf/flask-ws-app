from flask import session
from flask_socketio import Namespace, emit
import wave


class Stream(Namespace):
    def on_start_record(self, data):
        wf = wave.open('/Users/dev/PycharmProjects/messanger/app/'+'test.wav', mode='wb')
        wf.setnchannels(data.get('channels'))
        wf.setsampwidth(data.get('bps', 16) // 8)
        wf.setframerate(data.get('fps'))
        print(wf)
