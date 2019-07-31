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
    print('Playing MIDI File. . . ')
    global outport
    if(outport.closed):
        outport = mido.open_output('Microsoft GS Wavetable Synth 0')    
    #for msg in MidiFile("Bee_Gees_-_Stayin_Alive-Voice.mid").play():
    for msg in SMF_file.play():
        print(msg)
        outport.send(msg)
        incomingMsg = port.poll() 
        if (incomingMsg):
            #print(incomingMsg.type)
            if incomingMsg.note == 70 and incomingMsg.type == 'note_off':
                outport.reset()           
                break

#Callback definition
def route_midi(message):
    if message.type == 'note_on':
        if message.note == 72:
            print('Key 72')
            play_SMF(SMF_1)
        elif message.note == 71:
            print('Key 71')
            play_SMF(SMF_2)
#Maybe put the callback here?
def forward_while_reading(message)


#Set the ports callback function
#port.callback = route_midi


#Twiddle your thumbs while you wait for a note
while True:
    #print ('Twiddlin')
    msg_seeker = port.poll()
    if(msg_seeker):
        route_midi(msg_seeker)


# ##################SCRAP
# Calling receive(), __iter__(), or iter_pending() on a port with a callback will raise an exception:

# ValueError: a callback is set for this port
# To clear the callback:

# port.callback = None

# for msg in MidiFile('Movie_Themes_-_Jurassic_Park.mid'):
#     if(msg.is_meta):
#         if msg.type == 'set_tempo':
#             print(msg.tempo)

#             tempo2bpm()

# mid = MidiFile('Movie_Themes_-_Jurassic_Park.mid')