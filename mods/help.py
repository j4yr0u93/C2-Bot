import asyncio
import discord

async def test(message):
    '''This function outputs a string to confirm that seamless module integration is functioning'''
    await message.channel.send('Nice test!')

async def echo(message):
    '''This function reiterates whatever string input is read in'''
    echo_raw = message.content.split()
    echo_content = " ".join(echo_raw[1:])
    await message.channel.send(echo_content)

async def monke(message):
    '''This function is to confirm that only permitted users can run secure functions'''
    await message.channel.send('dev who made bot is monke')

#these dictionaries indicate which user level can run which functions, everyone or the designated secure roles
help_allowed = {'test' : test, 'echo' : echo}
help_secure = {'monke' : monke}
