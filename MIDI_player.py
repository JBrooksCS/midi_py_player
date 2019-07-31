#################################################################
####This code listens for an input on a port and plays a specific MIDI file depending on the input


import mido
from mido import MidiFile, MetaMessage
from mido.ports import MultiPort
#Open Input
port = mido.open_input('nanoKEY2 0')
#Open Output
outport = mido.open_output('Microsoft GS Wavetable Synth 0')
#Load MIDI Files
SMF_1 = MidiFile("Bee_Gees_-_Stayin_Alive-Voice.mid")
SMF_2 = MidiFile("Movie_Themes_-_Jurassic_Park.mid")


#Handler definition
def play_SMF(SMF_file):
    print('Made it to play_SMF')
    global outport
    outport.close()
    outport = mido.open_output('Microsoft GS Wavetable Synth 0')    
    #for msg in MidiFile("Bee_Gees_-_Stayin_Alive-Voice.mid").play():
    for msg in SMF_file.play():
        outport.send(msg)

#Callback definition
def route_midi(message):
    if message.type == 'note_on':
        if message.note == 72:
            print('Key 72')
            play_SMF(SMF_1)
        elif message.note == 71:
            print('Key 71')
            play_SMF(SMF_2)
        
           

 
port.callback = route_midi

        




#CRAP
for msg in SMF_1.play():
        outport.send(msg)


#SCRAP
def route_midi(message):
    if message.type == 'note_on':
        if message.note == 72:
            print(message.note)