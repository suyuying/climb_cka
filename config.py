import os

from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
class Setting:
    tg_token:str=os.environ.get("tg_token")
    chat_id:int=os.environ.get("chat_id")
