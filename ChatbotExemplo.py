from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Novo Bot')

base = ['Oi','Olá','Como Vai ?','Bem','Gostaria de uma pizza','Qual Sabor ?']

treinar = ListTrainer(bot)
treinar.train(base)


while True:
    usuario = input('Usuario: ')
    resposta = bot.get_response(usuario)

    print(resposta.confidence)
    if float(resposta.confidence) > 0.5:
        print('Bot: ',resposta)
    else:
        print('Bot: Ainda não consigo te responder')
