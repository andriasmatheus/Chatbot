from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot do PIPE")


pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
if(float(intencao[0]['probability']) < 0.92 and intencao[0]['intent']!="despedida"):
    print("Desculpe, não entendi.")
else:
    print("Resposta:" + resposta)

while (intencao[0]['intent']!="despedida"):
    if(intencao[0]['intent'] == "saudacao" and float(intencao[0]['probability']) >= 0.92):
        pergunta = input()
    else:
        pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    if(float(intencao[0]['probability']) < 0.92):
        print("Desculpe, não entendi.")
    else:
        print("Resposta:" + resposta)

print("Foi um prazer atendê-lo")