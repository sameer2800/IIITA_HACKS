from fb_post_replier import get_feed


feed = get_feed("me")

def post_is_read(post) :
	with open("readposts.txt","rw+") as f:
		data = f.read()
		datalist = data.split(",")
		datalist.pop()
		print datalist
		for item in datalist :
			if item == post['id'] :
				return True
		
		return False	

def append(post) :
	with open("readposts.txt","rw+") as f:
		print post['id']
		#f.write(post['id']+",")

for post in feed :
	print post
	if post_is_read(post) :
		i  =1
		print "hey"
	else :

		append(post)	
