import logging
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(logging.StreamHandler())

import slixmpp
import asyncio

class XMPPclient(slixmpp.ClientXMPP):
    def __init__(self, jid, password) -> None:
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.start)
        self.add_event_handler("message", self.message)

    async def start(self, event):
        self.send_presence()
        await self.get_roster()

        logger.info('XMPP client started')

    async def message_recived(self, msg):
        if msg['type'] in ('chat', 'normal'):
            logging.info(f"Message from {msg['from']} : {msg['body']}")
    
    async def message_send(self,recipient_jid, message):
        self.send_message(mto=recipient_jid, mbody=message, mtype='chat')

def login_xmpp():
    xmpp_client = XMPPclient(os.getenv('XMPP_USER'), os.getenv('XMPP_PASSWORD'))
    xmpp_client.connect()
    xmpp_client.process()
    return xmpp_client

