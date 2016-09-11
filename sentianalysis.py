import os
import json
import subprocess


def msg(list) :
	myst =""
	for a in list:		
		myst+= a
		myst += ". "

	batcmd="curl -d 'text= " + myst + "' http://text-processing.com/api/sentiment/"
	result = subprocess.check_output(batcmd, shell=True)

	d = json.loads(result)

	negative = d['probability']['neg']
	neutral = d['probability']['neutral']
	positive = d['probability']['pos']

	cl = 0

	#print myst
	message = ""
	if negative > neutral and negative > positive : 
		message = "Thanks. God Bless You too. :) "
	elif positive > neutral and positive > negative : 
		message = "Thanks, dear. This means a lot to me. Thanks so much for making my birthday so special in the same way as You make my life special. God bless you too. :D <3" 
	else :
		message = "Thanks,friend. Thanks a lot for the good wishes. God Bless You too. :D"

	return message


print msg(["u are boring", "u dont like reading", "get out from my life"])


'''	
inp = raw_input("enter message : ")

batcmd="curl -d 'text= " + inp + "' http://text-processing.com/api/sentiment/"
result = subprocess.check_output(batcmd, shell=True)

print inp

d = json.loads(result)

negative = d['probability']['neg']
neutral = d['probability']['neutral']
positive = d['probability']['pos']

cl = 0

message = ""
if negative > neutral and negative > positive : 
	message = "Thanks. God Bless You too. :) "
elif positive > neutral and positive > negative : 
	message = "Thanks, dear. This means a lot to me. Thanks so much for making my birthday so special in the same way as You make my life special. God bless you too. :D <3" 
else :
	message = "Thanks,friend. Thanks a lot for the good wishes. God Bless You too. :D"

print message
#message1 = "Thanks, dear. This means a lot to me. Thanks so much for making my birthday so special in the same way as You make my l

os.system('curl -d "text=great" http://text-processing.com/api/sentiment/')

subprocess.call([
	'curl',
	'-d',
	'"text=great"',
	'http://text-processing.com/api/sentiment/',
]) '''