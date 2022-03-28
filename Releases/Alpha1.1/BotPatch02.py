import random
import discord as dc
from discord.ext import commands
import typing
# imports

# funções

def debug(debugmessage):
    print(f'{debugmessage} Passou \n')

def mensagem_vazia(mensagem):
    if len(mensagem) == 0  or mensagem == ():
        return True
    else:
        return False

def erro_comando(comando):
    return f'`Sintaxe incorreta. Usar ***>help {comando}*** para conhecer o funcionamento do comando.`'

bot = commands.Bot(command_prefix='>')

# variáveis úteis

nada = ''
espaco = ' '

# fazer a classe "bot", para configurar eventos e comandos.

try:
    banco_de_dados_read = open('data.txt', 'r')
    banco_de_dados_add = open('data.txt', 'a')
    banco_de_dados_write = open('data.txt', 'w')
# Tenta abrir o arquivo onde se vai armazenar as informações permanentes

except: print('WARNING: Arquivo data.txt não encontrado.')
# Erro se o arquivo NÃO for encontrado

# Define um evento para a classe "bot"
@bot.event
# Definir função que será disparada quando a sua condição for verdade
# Nesse caso, on_ready() aciona quando o bot estiver online
async def on_ready():
    print(f'Bot {bot.user} online.')

# Definindo um comando para o bot.
# Essa função será disparada quando, em qualquer chat, for digitado
# (prefixo)nome_da_função argumentos

@bot.command(help='Função de teste, apenas para verificar a resposta do bot.')
async def ping(ctx): # ctx = Toda a mensagem.
    await ctx.channel.send('`Pong!`')

@bot.command(help='Rolador de dados.\nUso: ">d -NUMERO"')
async def d(ctx, num_faces_dado: int):
        resultado_dado = random.randint(1, num_faces_dado)
        await ctx.channel.send(f'`{num_faces_dado} faces :`  :game_die: ||**__> {resultado_dado} <__**|| :game_die:')
        
@bot.command()
async def add(ctx, *args):
    nome = args[0]
    atributo = args[1]
    valor_atr = args[2]
    dado_completo = f'{nome}.{atributo}.{valor_atr}\n'
    banco_de_dados_add.write('\n' + dado_completo)
    await ctx.channel.send(f'{atributo.capitalize()} de {nome.capitalize()} adicionado com sucesso!')

@bot.command(help='Mostra os dados de um personagem presente no banco de dados.\nUso: ">r -NOME -ATRIBUTO(opcional)".')
async def r(ctx, *args):
    contagem_de_indexes = 0
    for i in args:
        contagem_de_indexes += 1
        
    if contagem_de_indexes <= 1:
        dados_do_personagem = f'`*** {args[0].upper()} ***\n'
        for line in banco_de_dados_read:
            if line.startswith(args[0]):
                linha_dividida = line.split('.')
                dados_do_personagem = dados_do_personagem + f' -- {linha_dividida[1]} = {linha_dividida[2]}'
        dados_do_personagem_FINAL = dados_do_personagem + '`'
        await ctx.channel.send(dados_do_personagem_FINAL)
    
    elif se > 1:
        dados_do_personagem = f'`*** {args[0].upper()} -- {args[1]} ***\n'
        for line in banco_de_dados_read:
            if line.startswith(args[0]+'.'+args[1]):
                linha_dividida = line.split('.')
                if linha_dividida[0] == args[0] and linha_dividida[1] == args[1]:
                    dados_do_personagem = dados_do_personagem + f' < {linha_dividida[2]}'
        dados_do_personagem_FINAL = dados_do_personagem + '`'
        await ctx.channel.send(dados_do_personagem_FINAL)

@bot.command()
async def criador(ctx):
    await ctx.send('`Marcola do grau`')

bot.run('OTQ3MTIxMzMwOTAwMzE2MjEx.YhopeQ.av56lMtaukInmzAJcSUwWorrEEI')
