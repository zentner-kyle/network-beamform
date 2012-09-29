#!/usr/bin/env python2

import alsaaudio as audio

input = audio.PCM(audio.PCM_CAPTURE, audio.PCM_NONBLOCK)
output = audio.PCM(audio.PCM_PLAYBACK, audio.PCM_NONBLOCK)
# input = audio.PCM(audio.PCM_CAPTURE, audio.PCM_NORMAL)
# output = audio.PCM(audio.PCM_PLAYBACK, audio.PCM_NORMAL)
# input.setperiodsize(32)
# output.setperiodsize(32)
input.dumpinfo()
output.dumpinfo()

while True:
    output.write(input.read()[1])
