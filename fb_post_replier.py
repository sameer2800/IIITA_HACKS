import facebook
import requests
import traceback

#get token from here : https://developers.facebook.com/tools/access_token/
#or here : https://developers.facebook.com/tools/explorer/145634995501895/

token = 'EAACEdEose0cBAPSJ9lqZB9dgMtXbp8le9aU7cPirGwjaAEU12DPZB5otumb2C8bLrdZCd3ZBsGOvMFc2x9rrpAdnxIDu5T1HIY5rWoQIZA6NtSaNQZBP6a0uPW1VMeIkJ3iXyne4stV7zupypI2DDXbevUk1tGLhPT2HZBReEPIoUZAyG7ZCDO93ZB'
bday_date= "2016-09-10"

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
	if(slice_date(post) == bday_date and bday_analyse(post)):
		print "hello"
		p_id = post['id']			
		#print post
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



process_feed("me")
