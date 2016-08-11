#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Tiny Syslog Server in Python.
##
## This is a tiny syslog server that is able to receive UDP based syslog
## entries on a specified port and save them to a file.
## That's it... it does nothing else...
## There are a few configuration parameters.

import json
import logging
import SocketServer
from textwrap import dedent
from spark.rooms import Room
from spark.session import Session

LOG_FILE = 'org-syslog.log'
HOST, PORT = "0.0.0.0", 2514

#
# NO USER SERVICEABLE PARTS BELOW HERE...
#
SPARK_KEY='MThlYWMyZjUtZmU2Yy00NDk5LTk0OGMtOGU0Nzk4MzI3ODc2OWIzOWM3M2MtY2Vk'
SPARK_ROOM='SysNoti'



logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

class SyslogUDPHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		data = bytes.decode(self.request[0].strip())
		socket = self.request[1]
		print( "%s : " % self.client_address[0], str(data))
		logging.info(str(data))
		room.send_message(ss, str(data))

if __name__ == "__main__":
	try:
		server = SocketServer.UDPServer((HOST,PORT), SyslogUDPHandler)


		print "Authenticating with Spark"
        
		try:
			ss = Session('https://api.ciscospark.com', SPARK_KEY)
			room = Room.get(ss, SPARK_ROOM)
			room.send_message(ss, '자 시작합니다.!!')
		except ValueError:
			exit("  Exiting as I failed to authenticate your Spark API key")

		server.serve_forever(poll_interval=0.5)

	except (IOError, SystemExit):
		raise
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")
