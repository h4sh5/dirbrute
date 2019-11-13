#!/usr/bin/env python
import requests
import thread
import time
import sys 

tcount = 0
tmax = 20

lock = 0

if len(sys.argv) < 4:
	print "%s <url> <wordlist> <threads> [extensions]" %sys.argv[0]
	print "example:"
	print "%s http://example.com wordlist.txt 10 .php,.html" %sys.argv[0]
	exit(1)


extensions = []

if len(sys.argv) == 5:
	extensions.extend(sys.argv[4].split(","))


url = sys.argv[1]
wordlist = sys.argv[2]
tmax = int(sys.argv[3])

def trydir(d, extensions=[]):
	global tcount, url, lock
	# print "starting thread for %s:" % p, tcount

	for e in extensions:
		if not url.endswith("/"):
			testurl = url + "/" + d + e
		else:
			testurl = url + d + e


		code = 404

		r = requests.get(testurl)
		if r.status_code != 404:
			code = r.status_code

		if code != 404:
			while lock:
				pass
			lock = 1
			print code, ":", "len", len(r.content), ":",  testurl
			lock = 0
	tcount -= 1


print "bruteforcing directories in %s with %s, %i threads" % (url,wordlist,tmax)
print "extensions: ", extensions

with open(wordlist,'r') as f:
	for l in f:
		l = l.strip()
		try:
			while 1:
				# if success:
				# 	sys.exit(0)
				if tcount <= tmax:
					
					thread.start_new_thread(trydir, (l,extensions))
					tcount += 1
					break
				else: 
					pass
			
		except KeyboardInterrupt:
			print "user exit"
			exit(0)

print "DONE!"
