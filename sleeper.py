import time
import random
import os
import signal
import sys

print "Hello Mr Container Man... I was expecting you."

start = 30
stop = 60

def handler(signum, frame):
    print "Exiting on signal", signum
    sys.exit(128+signum)

signal.signal(signal.SIGTERM, handler)

if os.environ.has_key("SLEEP_START"):
    start = int(os.environ["SLEEP_START"])

if os.environ.has_key("SLEEP_STOP"):
    stop = int(os.environ["SLEEP_STOP"])

i = random.randint(start,stop)
print "Sleeping in total for %s seconds" % i
for second in range(i):
	second = second + 1;
	print "Slept for %s second%s so far..." % (second, 's' if second > 1 else '')
	time.sleep(1)
print "Completed sleep for %s seconds" % i
sys.exit(0)
