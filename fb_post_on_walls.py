import facebook
import requests
import traceback

#get token from here : https://developers.facebook.com/tools/access_token/
#or here : https://developers.facebook.com/tools/explorer/145634995501895/

token = 'EAACEdEose0cBABZCyndcTNWDeoUpZBAdtLODrZBi5ZAWPIHbsj5zIEuzUJYUFyepKe84oHPBAZAL7eizAs9fQgsMqwwfysgTVSoLZBwzzHyL1ITMYZCnto1ZAePqkFwZCZAln072ZCGOEOXY5PZCsqZC4C7q6ji0IuUjrzgKRBFC0sshlggZDZD'
bday_date= "2015-08-16"

def slice_date(post):
	date = post['created_time']
	return date[:10]

graph = facebook.GraphAPI(token)

friends = graph.get_connections(id='me', connection_name='friends')



graph.put_wall_post(message='hackathon is cool man ...#aanandita')