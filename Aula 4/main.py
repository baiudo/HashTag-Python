# título
# input do chat
# a cada msg enviada:
    # mostrar a mensagem do usuário
    # enviar a mensagem para a IA
    # aparece na tela a resposta da IA

#streamlit -> frontend e backend

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key = 'sua_chave_api_aqui')
#Este código deveria funcionar, porém não possuo créditos na OpenAI para testar. O código está correto e deve funcionar com uma chave de API válida.

st.write('ChatBot com IA')

# session_state para armazenar o histórico de mensagens
if not 'lista_msg' in st.session_state:
    st.session_state['lista_msg'] = []

for txt in st.session_state['lista_msg']:
    # Verifica o papel da mensagem (usuário ou assistente) e exibe na interface
    st.chat_message(txt['role']).write(txt['content'])

msg_usuario = st.chat_input('Digite sua mensagem aqui')
#cria o campo de mensagem
if msg_usuario:
    #exibe user
    st.chat_message('user').write(msg_usuario)
    msg_user = {'role': 'user', 'content': msg_usuario}
    st.session_state['lista_msg'].append(msg_user)

    # Resposta da IA
    resp_modelo = modelo.chat.completions.create(
        messages=st.session_state['lista_msg'],
        model='gpt-3.5-turbo')
    resp_ia = resp_modelo.choices[0].message.content
    #exibe ia
    st.chat_message('assistant').write(resp_ia)
    msg_ia = {'role': 'assistant', 'content': resp_ia}
    st.session_state['lista_msg'].append(msg_ia)
