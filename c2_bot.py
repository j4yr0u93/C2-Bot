import asyncio
import discord

from C2_Bot import __version__, discon, mod_list

for sublibrary in mod_list:
    functions_list = {}
    try:
        exec("from C2_Bot.mods.{s} import *".format(s=sublibrary))
        exec("from C2_Bot.mods.{s} import allowed, secure".format(s=sublibrary))
        allowed_functions.append(allowed)
        secure_functions.append(secure)
    except Exception as e:
        print(e)

def main():
    return

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(allowed_functions)



#message user welcome message when they join server
#@client.event
#async def on_member_join(member):
#    if member.guild.id == discon['id']['SERVER']:
#        channel = client.get_channel(discon['id']['WELCOME'])
#        await channel.send(f'{member.mention}')


@client.event
async def on_message(message):
    #ignore bots
    if message.author.bot:
        return
    #run a command if prexix matches and first 'word' after prefixes is in 'commands'
    elif message.content.startswith(discon['options']['PREFIX']):
        command_string = message.content
        command_parse = command_string.split()
        command = command_parse[0][len(discon['options']['PREFIX']):]
        if command in allowed_functions:
            try:
                await allowed_functions[command](message = message)
            except Exception as e:
                print(e)
        elif message.author.id == discon['options']['OWNER']:
            try:
                await secure_functions[command](message = message)
            except Exception as e:
                print(e)

client.run(discon['secure']['TOKEN'])
