import pygame.midi
from pygame import mixer
import winsound
from random import randint
from pygame import mixer

def number_to_note(number):
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    return notes[number%12]

def readInput(input_device):
    if input_device.poll():
        event = input_device.read(1)[0]
        data = event[0]
        timestamp = event[1]
        note_number = data[1]
        velocity = data[2]
        print(note_number, number_to_note(note_number), velocity)
        return note_number, velocity

def play(songname):
    mixer.music.load(songname)
    mixer.music.set_volume(0.7)
    mixer.music.play()




def check(n, v):
    dic = {36: 'a.mp3',
       38: 'b.mp3',
       40: 'c.mp3',
       42: 'd.mp3',
       59: 'e.mp3'}

    try:
        s = dic[n] #s for song
    except KeyError:
        return
        
    if v == 100: #pressed
        print(s)
        play(s)


    if v == 64: #released
        if note != None:
            mixer.music.stop()
            print(f"Stopped {s}")
    
    return

    

    
            

        


if __name__ == '__main__':
    pygame.midi.init()
    mixer.init()
    my_input = pygame.midi.Input(1) #casio piano

    while True:
        try:
            note, v = readInput(my_input)
            check(note, v)
            
                
        
        except TypeError: #no note returned
            continue