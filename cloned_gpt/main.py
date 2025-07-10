import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils import  get_Chat_respnse


st.title('💬 克隆小小SwallowLook')


with st.sidebar:
    api_key = st.text_input("请输入DeepSeek APi密钥:", type="password")
    st.markdown("[获取DeepSeek API密钥](https://platform.deepseek.com)")
if'memory' not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"]=[{'role':'ai','content':'我是你的小奴AI桑呀'}]
for message in st.session_state["messages"]:
    st.chat_message(message['role']).write(message['content'])

prompt=st.chat_input()
if prompt:
    if not api_key:
        st.info('api密钥呢')
        st.stop()
    st.session_state["messages"].append({'role':'human','content':prompt})
    st.chat_message('human').write(prompt)

    with st.spinner('别急，在思考'):
        response=get_Chat_respnse(prompt,st.session_state["memory"],api_key)

    msg={'role':'ai','content':response}
    st.session_state["messages"].append(msg)
    st.chat_message('ai').write(response)