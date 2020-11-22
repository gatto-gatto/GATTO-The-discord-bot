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

@client.command()
async def puspus(ctx):
	UTC = pytz.utc 
	timeZ_Kl = pytz.timezone('Asia/Kolkata') 
	dt_Kl = datetime.now(timeZ_Kl) 
	# finding the time aoocind to 24 hrs clock........ local time
	time1= int(dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z').split()[1].split(':')[0])
	#finding the day hdsiojd 
	day=time.ctime().split()[0]
	await ctx.send(f"{time1} , {day}")
	if(day=='Mon'):
		if(time1==1+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/htvdf4mslf")			
		elif(time1==2+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/bnd-gsza-oyf?pli=1&authuser=1")
		elif(time1==3+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==4+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==5+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/duu-uqec-tjv?authuser=0&hs=179")
			
		else:
			await ctx.send("Rn koyi class koni hjdhfjahsdfjkg")
	elif(day=='Tue'):
		if(time1==9):
			await ctx.send("IDBMS's lab")			
			await ctx.send("teacher tatti h kuch nhi krvayeag so u can sleep")			
			await ctx.send("https://meet.google.com/lookup/g232xe3juu?authuser=1&hs=179")					
		elif(time1==1+12):
			await ctx.send("doubt class h and ik u haven't seen the video so chill kr")
		else:
			await ctx.send("mje kr be !!!!!!!!!!!!!!!!")		
	elif(day=='Wed'):
		if(time1==9):
			await ctx.send("https://meet.google.com/tif-qahu-sau?authuser=0")
		elif(time1==5+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/htvdf4mslf")			
		elif(time1==1+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/bnd-gsza-oyf?pli=1&authuser=1")
		elif(time1==2+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==3+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==4+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/duu-uqec-tjv?authuser=0&hs=179")
		else:
			await ctx.send("NO calss hsadfjhsdgah")
	elif(day=='Thu'):
		if(time1==10):
			await ctx.send("AP's lab")			
			# await ctx.send("teacher tatti h kuch nhi krvayeag so u can sleep")			
			await ctx.send("https://meet.google.com/lookup/htvdf4mslf")					
		elif(time1==1+12):
			await ctx.send("doubt class h and ik u haven't seen the video so chill kr")
		else:
			await ctx.send("mje kr be !!!!!!!!!!!!!!!!")		
	elif(day=="Fri"):
		if(time1==4+12):
			await ctx.send("AP by varun")			
			await ctx.send("https://meet.google.com/lookup/frazjfw4w6?authuser=1&hs=179")			
		elif(time1==5+12):
			await ctx.send("COA")			
			await ctx.send("https://meet.google.com/bnd-gsza-oyf?pli=1&authuser=1")
		elif(time1==1+12):
			await ctx.send("IDBMS")
			await ctx.send("https://meet.google.com/lookup/evx4lzq2xa?authuser=1&hs=179")
		elif(time1==2+12):		
			await ctx.send("DCS")
			await ctx.send("https://meet.google.com/lookup/gcfpz2o5ch?authuser=1&hs=179")
		elif(time1==3+12):		
			await ctx.send("M3")
			await ctx.send("https://meet.google.com/duu-uqec-tjv?authuser=0&hs=179")
		else:
			await ctx.send("NO calss hsadfjhsdgah")
	else:
		await ctx.send("i duuno jk no class today sjkhsgd")

if __name__ == "__main__":
    client.run('NzQ3NzA3MzU3MjU3MTM4MTk2.X0SyvQ.ooCRlLqXCyLvs8RCuiUATy939Yc')
