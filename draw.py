#!/usr/bin/env python
# Binds PULL socket to tcp://localhost:5558
# Collects network updates via that socket

import struct
import sys

import zmq

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

while True:
    s = receiver.recv()
    sys.stdout.write('got integer {0}\n'.format(struct.unpack("!i", s)[0]))
    sys.stdout.flush()

