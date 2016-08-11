#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spark.rooms import Room
from spark.session import Session

SPARK_KEY=''
SPARK_ROOM='NiceRoom'

if __name__ == "__main__":
	try:
		ss = Session('https://api.ciscospark.com', SPARK_KEY)
		room = Room.get(ss, SPARK_ROOM)
		room.send_message(ss, '자 시작합니다.!!')
	except ValueError:
		exit("Some errors")
