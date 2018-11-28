import time, subprocess

COMMAND=['/home/pi/Desktop/C3PO/Bot.py']
LOGFILE='/home/pi/Desktop/C3PO/restart.txt'

def writelog(message):
    with open(LOGFILE,'a') as f:
        f.write("{0} {1}\n".format(time.asctime( time.localtime(time.time())),
                                   message))

writelog("Starting")
while True:
    rc = subprocess.call(COMMAND)
    if rc >= 0:
        writelog("Exited with {0} status".format(rc))
    else:
        writelog("Exited on signal {0}".format(0-rc))
    writelog("Restarting")
