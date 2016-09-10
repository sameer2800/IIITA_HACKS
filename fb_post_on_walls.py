import facebook
import requests
import traceback

#get token from here : https://developers.facebook.com/tools/access_token/
#or here : https://developers.facebook.com/tools/explorer/145634995501895/

token = 'EAACEdEose0cBAKiOZBeki7JcOBjZCtSCVY9UiIm1vyStcgZBTbppfL29lbgcBjFIHRP2oUjWr5x7m67x2pVUEzUc9Ozn9vHm7didfHMdcgfA3FvQIHHdolZBcmKyk4yRTH1UuEjF9BaFroVuuP8bZAtPqowNxCJeOcezApuZBa5ii5dAMrYwjy'
bday_date= "2015-08-16"

def slice_date(post):
	date = post['created_time']
	return date[:10]

graph = facebook.GraphAPI(token)

friends = graph.get_connections(id='me', connection_name='friends')

for friend in friends['data'] :
	print friend['name']
	graph.put_wall_post(message='hackathon sucks man ...#'+ friend['name'])