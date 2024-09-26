from dotenv import load_dotenv


import subprocess
import os
import logging

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(logging.StreamHandler())


def add_user(username, passw):
    logger.info('Adding user')
    try:
        command = ['sudo prosodyctl', 'register', f'{username}', os.getenv('XMPP_DOMAIN'), f'{passw}']
        subprocess.run(command, shell=True)

    except Exception as e:
        logger.error(f'Error adding user: {e}')
        return False
    except Exception as e:
        logger.error(f'Error adding user: {e}')
        return False

    return True
