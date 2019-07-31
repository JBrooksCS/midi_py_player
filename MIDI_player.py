import mido
from mido import MidiFile, MetaMessage
from mido.ports import MultiPort

mid = MidiFile("Bee_Gees_-_Stayin_Alive-Voice.mid")
outport = mido.open_output()

#Show all MIDI Data
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

#Play all MIDI data
for msg in MidiFile("Movie_Themes_-_Jurassic_Park.mid").play():
    outport.send(msg)
    phrase = input("Is it working?")

outport.panic()




for msg in port:
    while (msg.control == 127)
        for msg in MidiFile("Movie_Themes_-_Jurassic_Park.mid").play():
        outport.send(msg)


#works
for message in port:
    print(message)
    

#works
for message in port:
    #print(message)
    if message.type == 'note_on' and message.note == 72:
        print(message)
        for msg in MidiFile("Movie_Themes_-_Jurassic_Park.mid").play():
            outport.send(msg)


for message in port:
    #print(message)
    if message.type == 'note_on' and message.note == 72:
        print(message)
        for msg in MidiFile("Movie_Themes_-_Jurassic_Park.mid").play():
            outport.send(msg)
            if (port.poll() != 'None') :
                message=port.receive()
                print(message)
           






#IO
mido.get_output_names()
mido.get_input_names()
port = mido.open_input('Midi Fighter Twister 0')
port.close()
port = mido.open_input('nanoKEY2 0')
outport = mido.open_output('Microsoft GS Wavetable Synth 0')

with mido.open_input('nanoKEY2 0') as port