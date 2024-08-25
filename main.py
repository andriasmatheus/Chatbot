from chatbot import ChatBot
myChatBot = ChatBot()
#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot do PIPE")


pergunta = input("Como posso te ajudar?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta)
#print(resposta + "   ["+intencao[0]['intent']+"]")

num_pergunta = 0
while (intencao[0]['intent']!="despedida"):
    if(num_pergunta == 0):
        num_pergunta += 1
        pergunta = input()
    else:
        pergunta = input("Posso lhe ajudar com algo a mais?\n")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta)

print("Foi um prazer atendê-lo")