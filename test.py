#!/usr/bin/env python
# Connects PUSH socket to PULL socket at tcp://localhost:5558
# Pushes network updates to that socket

import random
import struct
import sys
import time

import zmq

context = zmq.Context()

# Socket to receive messages on
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

while True:
    a = random.randint(0, 2**31)
    sender.send(struct.pack("!i", a))
    sys.stdout.write('sent integer {0}\n'.format(a))
    sys.stdout.flush()
    time.sleep(1)

