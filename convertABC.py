from music21 import *

songName = raw_input("Please enter the name of the song: ")
musicFile = open("textfiles\\" + songName + ".txt", 'w+')
abcScore = converter.parse("abcfiles\\" + songName + ".abc")
flat = abcScore.flat
measures = abcScore.getElementsByClass(stream.Part)[0].getElementsByClass(stream.Measure)
if(len(measures) != 0):
    print("We have measures")
    for measure in measures:
        measureNotes = ""
        for note in measure.notes:
            measureNotes = measureNotes + str(note.name) + str(note.octave) + " "
        musicFile.write(measureNotes + "\n")
else:#we will just use the chords
    print("No measures")
    flat = abcScore.flat
    chords = abcScore.getElementsByClass(stream.Part)[0].getElementsByClass(chord.Chord)
    for chord in chords:
        musicFile.write(str(chord)[21:len(str(chord))-1] + "\n")
musicFile.close();
