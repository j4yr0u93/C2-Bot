import asyncio
import discord

from C2_Bot import __version__, discon, mod_list

for sublibrary in mod_list:
    functions_list = []
    try:
        exec("from C2_Bot.mods.{s} import *".format(s=sublibrary))
        exec("from C2_Bot.mods.{s} import allowed_functions".format(s=sublibrary))
        functions_list.append(allowed_functions)
    except Exception as e:
        print(e)

def main():
    return

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



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
#elif message.content.startswith(discon['options']['PREFIX']) & message.content[len(discon['options']['PREFIX']):].split[0] in mod_list:
#        return


client.run(discon['secure']['TOKEN'])
