import os

import time
from datetime import datetime 
from discord.ext import commands
import pytz 


client = commands.Bot(command_prefix="sudo ")
TOKEN = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print("Logged in as {}({})".format(client.user.name, client.user.id))

@client.command()
async def type(ctx):
	import random
	cnt=0  # no of mess have to remove 
	while(True):
		local=""
		for i in range(random.randint(3,6)):
			local+=chr(random.randint(97,122))
		cnt+=2 
		await ctx.send(local)
		msg=await client.wait_for('message')
		if(msg.content=="gatto"):
			await ctx.channel.purge(limit=cnt)
			break	
		if(msg.content!=local):
			await ctx.send("wrong")
			cnt+=1

	
@client.command()
async def fastfinger(ctx):
	import random
	cnt=0  # no of mess have to remove 
	words=['follow','feet','has','water','earth','run','these','you','girl','me','his','just','find','men','then','add','into','what','spell','important','it','her','long','may','dont','how','food','still','want','look','quite','xd','turn','so','throug','America','talk','by','into','who','haead','so','line','night','country','sometimes','no','boy','tell','high','another','change','donw','want','day','story','are','family','here','stop','each','far','seem','lol','shhe','she','never','back','different','it','io','cazzo','only','lola','halo','close','four','be','call','tree','being','now','about']
	while(True):
		local=words[random.randint(0,len(words))]
		cnt+=2 
		await ctx.send(local)
		msg=await client.wait_for('message')
		if(msg.content=="gatto"):
			await ctx.channel.purge(limit=cnt)
			break
		if(msg.content!=local):
			await ctx.send("wrong")
			cnt+=1


	
@client.command()
async def chinnie(ctx):
	await ctx.send("var message=prompt();for(var i=0;i<100;i++) {async function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}await sleep(10);document.getElementsByClassName('chatmsg')[0].value = message;document.getElementsByClassName('sendbtn')[0].click();}")


@client.command()
async def dying(ctx,amount=50):
	data=[["vic2561@yahoo.com","lakimata"],[]]
	await ctx.send("enter pass")
	msg=await client.wait_for('message')
	if(msg.content.split()[0]!="277353"):
		await ctx.channel.purge(limit=3)
	else:
		if(msg.content.split()[1]=="n"):
			await ctx.channel.purge(limit=3)
			await ctx.send(data[0][0])
			await ctx.send(data[0][1])
		time.sleep(20)
		await ctx.channel.purge(limit=3)

@client.command()
async def sins(ctx,amount=50):
	while(True):
		await ctx.channel.purge(limit=1000)
		sleep(60*5)
		
@bot.command()
async def dm_all(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("'" + args + "' sent to: " + member.name)

            except:
                print("Couldn't send '" + args + "' to: " + member.name)

    else:
        await ctx.channel.send("A message was not provided.")

if __name__ == "__main__":
    client.run(TOKEN)
