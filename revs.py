#Reverse IP Auto Remove Duplicate Result !!! 
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#You can recode This Tools 
#But I beg you not to delete the author's name.

Get used to mutual respect for someone's work!!!

import requests,re,time,random ,os, sys, socket
from multiprocessing.dummy import Pool
from colorama import Fore

def Banner():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print "==================================================="
	print Fore.RED + "[!] Reverse IP Auto Remove Duplicate Result !!! |" + Fore.WHITE +" "+ Fore.GREEN + "PYTHON CODE" + Fore.WHITE
	print Fore.RED + "[!] Contact : " + Fore.WHITE+"ICQ : Shin403" +"|"+ "TELEGRAM : Shin_code"
	print Fore.RED + "[!] Host : " + Fore.WHITE+"Py@"+host_name
	print Fore.RED + "[!] LocalHost : " + Fore.WHITE + host_ip
	print "===================================================" 
Banner()


def filter(o):
	block = ['ico', 'png' , 'jpg', 'gif', 'displ','css','dataL','push', 'getEl','display','getElementById','dataLayer','getElementsByTagName']
	domen = ['cdnjs.cloudflare.com','db-ip.com', 'twitter.com','facebook.com',  'cdnjs.cloudflare.com']
	neko = set()
	for i in o:
		ext = i.split('.')[-1]
		if ext not in block and i not in domen:
			neko.add(i)
	return neko

def SHINREV(url):
	try:
		SHINGET = requests.get('http://sharingmyip.com/?site='+url,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
		if 'at this IP address' in SHINGET:
			REGEX = re.findall("(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z]{1,63}",SHINGET)
			SHINFIL = filter(REGEX)
			for SHIN in SHINFIL:
				SHINREP  = SHIN.replace('www.','').replace('ftp.','').replace('images.','').replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				print(Fore.GREEN + '[Geting website list --> ]' + Fore.WHITE + SHINREP)
				open('result.txt','a').write('http://'+SHINREP+'\n')
			else:
				print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
				pass

def DELETE_DUPLICATE():
	with open('result.txt', 'r') as SHINXX:
		SHINXXX = list(dict.fromkeys(SHINXX.read().splitlines()))
		with open('result.txt.tmp','a') as new:
			new.write('\n'.join(SHINXXX))
			new.close()
		SHINXX.close()
	os.remove('result.txt')
	os.rename('result.txt.tmp','result.txt')


def Main():
	try:
		list = raw_input("\n\033[91mDomain List\033[97m:~# \033[97m").replace('http://', '').replace('https://', '')
		che = open(list, 'r').read().splitlines()
		pp = Pool(50)
		pr = pp.map(SHINREV, che)
	except:
		pass

if __name__ == '__main__':
	Main()
	DELETE_DUPLICATE()