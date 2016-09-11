import facebook
import requests
import traceback
import os
import json
import subprocess

#get token from here : https://developers.facebook.com/tools/access_token/
#or here : https://developers.facebook.com/tools/explorer/145634995501895/

token = 'EAACEdEose0cBABZCyndcTNWDeoUpZBAdtLODrZBi5ZAWPIHbsj5zIEuzUJYUFyepKe84oHPBAZAL7eizAs9fQgsMqwwfysgTVSoLZBwzzHyL1ITMYZCnto1ZAePqkFwZCZAln072ZCGOEOXY5PZCsqZC4C7q6ji0IuUjrzgKRBFC0sshlggZDZD'
bday_date= "2016-09-10"
msgs = ["Thanks, dear. This means a lot to me. Thanks so much for making my birthday so special in the same way as You make my life special. God bless you too. :D <3" ,"Thanks,friend. Thanks a lot for the good wishes. God Bless You too. :D",   "Thanks. God Bless You too." ]

def slice_date(post):
	date = post['created_time']
	return date[:10]

graph = facebook.GraphAPI(token)

friends = graph.get_connections(id='me', connection_name='friends')
#print friends

posts = graph.get_connections(id='me', connection_name='posts')
#print posts

def bday_analyse(post):
	if 'message' in post :
		print post['message']
		if "bday" in post['message'] or "birthday" in post['message'] or "hbd" in post['message'] :
			return True
		

	if 'story' in post :
		print post['story']
		if "bday" in post['story'] or "birthday" in post['story'] or "hbd" in post['story'] :
			return True
		
	return False	

def process_post(post):
	
	bday_comment = "Thank you :) #" + post['from']['name'] 
	
	print slice_date(post) + "  " + bday_date
	print post
	print bday_analyse(post)
	if(slice_date(post) == bday_date ):
		print "hello"
		p_id = post['id']			
		#print post
		p_id = "135114833609742_135157016938857"
		graph.put_like(p_id)
		graph.put_comment(p_id,bday_comment)
			
		if 'story' in post :
			print "liking & commenting " + post['from']['name'] + " post. " + post['story']

		if 'message' in post:
			print "liking & commenting " + post['from']['name'] + " post. " + post['message']






def process_feed(user) :
	
	feed = graph.get_connections(id=user, connection_name='feed')
	#print feed
	print "hello world"

	while 1 :
		try :
			for post in feed['data']:
			   process_post(post)

			feed = requests.get(feed['paging']['next']).json()			
		except Exception :
			print("exception raised: " + traceback.format_exc())
			break		   



#process_feed("me")
def post_is_read(post) :
	#print post
	with open("readposts.txt","rw+") as f:
		data = f.read()
		datalist = data.split(",")
		datalist.pop()
		#print datalist
		for item in datalist :
			if item == post['id'] :
				return True
		
		append(post)
		return False	

def append_userfile(post) :
	#print post
	with open("user_analysis.txt","rw+") as f:
		data = f.read()
		datalist = data.split(",")
		datalist.pop()
		#print datalist
		allusers = []
		for item in datalist :
			userdetails = item.split("|")
			allusers.append(userdetails[0])

def sentianalysis(list) :
	myst = list

	batcmd="curl -d 'text= " + myst + "' http://text-processing.com/api/sentiment/"
	result = subprocess.check_output(batcmd, shell=True)

	d = json.loads(result)

	negative = d['probability']['neg']
	neutral = d['probability']['neutral']
	positive = d['probability']['pos']

	cl = 0

	#print myst
	message = ""
	val = 0
	if negative > neutral and negative > positive : 
		message = "Thanks. God Bless You too. :) "
		val = 2
	elif positive > neutral and positive > negative : 
		message = "Thanks, dear. This means a lot to me. Thanks so much for making my birthday so special in the same way as You make my life special. God bless you too. :D <3" 
		val = 0
	else :
		message = "Thanks,friend. Thanks a lot for the good wishes. God Bless You too. :D"
		val = 1
	return val



def append_simply(post) :
			pr= graph.get_object(id= post['id'])
			mesg = pr['message']
			id1 = post['from']['id']

			charan =  sentianalysis(mesg)

			stri = id1 + "|" + str(charan) + "|" + mesg

			with open("user_analysis.txt","a+") as f:
				f.write(stri + ",")

def append(post) :
	with open("readposts.txt","a+") as f:
		i =1
		#print post['id']
		f.write(post['id']+",")


def gettype(userid) :
	with open("user_analysis.txt","r+") as f:
		data = f.read()
		datalist = data.split(",")
		

		print datalist	
		for item in datalist :
		
			itemlist = item.split("|")
			print itemlist
			if userid == itemlist[0] :
				return itemlist[1]


		return -1		


def analyse_feed(user) :
	feed = graph.get_connections(id=user, connection_name='feed')
	
	for post in feed['data']:
		
		if post_is_read(post) :
			i  =1
			print "hey"
		elif bday_analyse(post) :
			userid = post['from']['id']
			print "userid" +  userid
			val = gettype(userid)
			print val
			val = int(val)
			if val != -1 :
				print "bday" + str(val) #sentiment analysis

				graph.put_object(parent_object=post['id'], connection_name='comments',
                 message=msgs[val])


			else:
				graph.put_object(parent_object=post['id'], connection_name='comments',
                 message="thank you just cool frind !! ")

				print "new bday "
			
		else :

			append_simply(post)	




#append_userfile("12")
analyse_feed("me")


