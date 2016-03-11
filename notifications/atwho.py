import re, sys
from notifications.signals import notify
from accounts.models import MyUser
reload(sys)
sys.setdefaultencoding( "utf-8" )

def atwho(text, sender, targetcomment):
	commmentdecode = text.decode("utf8")
	pattern = re.compile(u'@([\u4e00-\u9fa5\w\-]+)')  
	results =  pattern.findall(commmentdecode) 
	userlist = []
	for item in results:
		user = MyUser.objects.filter(username = item.encode('utf8'))
		if user:
			user = MyUser.objects.get(username = item.encode('utf8'))
			notify.send(sender=sender, target_object=targetcomment, recipient = user, verb="@", text=text)
			userlist.append(item.encode('utf8'))
	return userlist


def atwhononoti(text):
	commmentdecode = text.decode("utf8")
	pattern = re.compile(u'@([\u4e00-\u9fa5\w\-]+)')  
	results =  pattern.findall(commmentdecode) 
	userlist = []
	for item in results:
		user = MyUser.objects.filter(username = item.encode('utf8'))
		if user:
			user = MyUser.objects.get(username = item.encode('utf8'))
			#notify.send(sender=sender, target_object=targetcomment, recipient = user, verb="@", text=text)
			userlist.append('@'+item.encode('utf8')+' ')
	return userlist