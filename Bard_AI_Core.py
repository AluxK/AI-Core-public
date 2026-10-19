from bardapi import Bard
import os


def get_cookie(**kwargs):
    if os.environ['BARD_API_KEY']:
        cookie = Bard(token = os.environ['BARD_API_KEY'])

    if kwargs.get("auto_cookie"):
        cookie = Bard(token_from_browser=True)
