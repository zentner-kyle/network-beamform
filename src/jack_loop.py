#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright 2003, Andrew W. Schmeder
# This source code is released under the terms of the GNU Public License.
# See LICENSE for the full text of these terms.

import numpy
import jack

jack.attach("loop")

print jack.get_ports()

jack.register_port("in_1", jack.IsInput)
jack.register_port("in_2", jack.IsInput)
jack.register_port("out_1", jack.IsOutput)
jack.register_port("out_2", jack.IsOutput)

jack.activate()

print jack.get_ports()

jack.connect("system:capture_1", "loop:in_1")
jack.connect("system:capture_2", "loop:in_2")
jack.connect("loop:out_1", "system:playback_1")
jack.connect("loop:out_2", "system:playback_2")

print jack.get_connections("loop:in_1")

N = jack.get_buffer_size()
Sr = float(jack.get_sample_rate())
print "Buffer Size:", N, "Sample Rate:", Sr
sec = 3.0

capture = numpy.zeros((2,int(Sr*sec)), 'f')
input = numpy.zeros((2,N), 'f')
output = numpy.zeros((2,N), 'f')

def loop():
    try:
        while 1:
            try:
                jack.process(input, input)
            except jack.InputSyncError:
                print "Input Sync"
                pass
            except jack.OutputSyncError:
                print "Output Sync"
                pass
            print ".",
    except Exeption:
        jack.deactivate()
        jack.detach()

jack.deactivate()
jack.detach()
