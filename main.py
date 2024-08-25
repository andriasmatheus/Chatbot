from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot do PIPE")


pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
first_entry = True

while (intencao[0]['intent']!="despedida" or (intencao[0]['intent']=="despedida" and float(intencao[0]['probability']) < 0.95)):
    if(first_entry == False):
        resposta, intencao = myChatBot.chatbot_response(pergunta)
    else:
        first_entry = False
    if(float(intencao[0]['probability']) < 0.95):
        pergunta = input("Desculpe, não entendi. Pode esclarecer melhor a sua dúvida?\n")
    elif(intencao[0]['intent'] == "saudacao" and float(intencao[0]['probability']) >= 0.95):
        pergunta = input("Qual é a sua dúvida?\n")
    elif(float(intencao[0]['probability']) >= 0.95 and intencao[0]['intent']!="despedida"):
        print(resposta)
        pergunta = input("Posso lhe ajudar com algo a mais?\n")

print("Foi um prazer atendê-lo")