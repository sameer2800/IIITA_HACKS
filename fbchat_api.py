import requests
import fbchat
from getpass import getpass
from urllib import urlencode

def login() :
	user = raw_input("Enter username: ")
	passw = getpass()
	user = "rajmahajan191@gmail.com"
	passw = "rajmahajan1912"
	client = fbchat.Client(user, passw)
	return client


def getmessages(client) :
	friends = client.getUsers("sam")  # return a list of names
	friend = friends[0]
	print friend
	sent = client.send(friend.uid, "hey bro ")
	print sent

client = login()
getmessages(client)