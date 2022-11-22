import streamlit as st
import datetime
from data import Chat_messages



def set_message(message):
    if(username!="" and message!=""):
        date=str(datetime.datetime.now())
        date=date[11:19]

        msg=f'{username}\n{date}'
        Chat_messages[msg]=message
        return Chat_messages
if __name__=="__main__":
    username=st.text_input("User Id")
    message=st.text_input("Messages")
    Chat_messages=set_message(message)
    st.write(Chat_messages)


