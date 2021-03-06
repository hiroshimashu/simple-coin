from distutils.version import StrictVersion
import json 

PROTOCOL_NAME = 'simple_bitcoin_protocol'
MY_VERSION = '0.1.0'

MSG_ADD = 0
MSG_REMOVE = 1
MSG_CORE_LIST = 2
MSG_REQUETST_CORE_LIST = 3
MSG_PING = 4
MSG_ADD_AS_EDGE = 5
MSG_REMOVE_EDGE = 6

ERR_PROTOCOL_UNMATCH = 0
ERR_VERSION_UNMATCH = 1
OK_WITH_PAYLOAD = 2
OS_WITHOUT_PAYLOAD = 3

class MessageManager:
    def __init__(self):
        print('initializing message...')

    def build(self, msg_type, payload = None):
        message = {
            'protocol': PROTOCOL_NAME,
            'version': MY_VERSION,
            'msg_type': msg_type
        }

        if payload is not None:
            message['payload'] = payload
        
        return json.dumps(message)

    def parse(self, msg):
        msg = json.loads(msg)
        msg_version = StrictVersion(msg['version'])

        cmd = msg['msg_type']
        payload = msg['payload']

        if msg['protocol'] != PROTOCOL_NAME:
            return ('error', ERR_PROTOCOL_UNMATCH, None, None)
        elif msg_version > StrictVersion(MY_VERSION):
            return ('error', ERR_VERSION_UNMATCH, None, None)
        elif cmd == MSG_CORE_LIST:
            return ('ok', OK_WITH_PAYLOAD, cmd, payload)
        else:
            return ('ok', OK_WITH_PAYLOAD, cmd, None)
            
        

