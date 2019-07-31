import mido
from mido import MidiFile, MetaMessage
from mido.ports import MultiPort

import time

port = mido.open_input('nanoKEY2 0')


def counter(message):
    print('Made it to counter')
    msg = port.poll()
    print(msg)
    while(msg != 'None'):
        print('Waiting...')
        time.sleep(1)
        msg = port.poll()



#Callback definition
def route_midi(message):
    print('Made it to route midi')
    if message.type == 'note_on':
        if message.note == 72:
            print('Key 72')
            
        elif message.note == 71:
            counter(message)
            
        


port.callback = route_midi


#SCRATCH

import mido
from mido import MidiFile, MetaMessage
from mido.ports import MultiPort

port = mido.open_input('nanoKEY2 0')
outport = mido.open_output('Microsoft GS Wavetable Synth 0')


############################################################
while True:
    for msg in port.iter_pending():
        print(msg)

    do_other_stuff()
######################################################
###DIS IS IT - PLAY IT TILL I QUIT
#timeCounter = 0.0
for msg in MidiFile("Movie_Themes_-_Jurassic_Park.mid").play():
    outport.send(msg)
    incomingMsg = port.poll() 
    if (incomingMsg):
        print(incomingMsg.type)
        if incomingMsg.note == 70 and incomingMsg.type == 'note_off':
            outport.reset()           
            break




        #timeCounter += msg.time
        #print(timeCounter)

