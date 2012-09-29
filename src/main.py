#!/usr/bin/env python2
from __future__ import print_function
import jack
import numpy


def loop():
    client = jack.Client('beamform')
    client.register_port('out_L', jack.IsOutput)
    client.register_port('out_R', jack.IsOutput)
    client.register_port('in_L', jack.IsInput)
    client.register_port('in_R', jack.IsInput)
    sample_rate = client.get_sample_rate()
    seconds = 1.0 / 8
    sample_count = sample_rate / seconds
    buffer_size = client.get_buffer_size()
    loop = numpy.zeros((2, buffer_size), 'f')
    client.activate()
    client.connect('system:capture_1', 'beamform:in_L')
    client.connect('system:capture_2', 'beamform:in_R')
    client.connect('beamform:out_L', 'system:playback_1')
    client.connect('beamform:out_R', 'system:playback_2')
    try:
        while True:
            try:
                client.process(loop, loop)
            except jack.InputSyncError:
                print('Input sync.')
            except jack.OutputSyncError:
                print('Output sync.')
    except Exception:
        print("hi")
        client.deactivate()
        client.detach()

loop()
