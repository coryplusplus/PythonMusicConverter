from music21 import *

global songName
global htmlfile

COLORS = [
'850000','9C0000','B31A00','B35400','B38E00','4D8F00','009100','003C1A','000080','00004D','00001A','000000',
'850000','9C0000','B31A00','B35400','B38E00','4D8F00','009100','003C1A','000080','00004D','00001A','000000',
'9E0000','B50000','CC3300','CC6D00','CCA700','66A800','00AA00','005533','000099','000066','000033','000011',
'B80000','CF1A00','E64D09','E68708','E6C108','80C200','1AC400','096F4D','001AB3','000080','09004D','1A002B',
'd10000','E83311','ff6622','FFA021','ffda21','99DB10','33dd00','228866','1133cc','191999','220066','330044',
'EB1A1A','FF4D2B','FF803C','FFBA3B','FFF43B','B3F52A','4DF71A','3CA280','2B4DE6','3333B3','3C1A80','4D1A5E',
'FF3333','FF6644','FF9955','FFD354','FFFF54','CCFF43','66FF33','55BB99','4466FF','4C4CCC','553399','663377',
'FF4D4D','FF805E','FFB36F','FFED6E','FFFF6E','E6FF5D','80FF4D','6FD5B3','5E80FF','6666E6','6F4DB3','804D91'
]

COLOR_MAP = {'C0': '850000', 'C#0': '9C0000', 'D-0': '9C0000', 'D0': 'B31A00', 'D#0': 'B35400', 'E-0': 'B35400', 'E0': 'B38E00', 'E#0': '4D8F00', 'F0': '4D8F00', 'F#0': '009100', 'G-0': '009100', 'G0': '003C1A', 'G#0': '000080', 'A-0': '000080', 'A0': '00004D', 'A#0': '00001A', 'B-0': '00001A', 'B0': '000000', 'C1': '850000', 'C#1': '9C0000', 'D-1': '9C0000', 'D1': 'B31A00', 'D#1': 'B35400', 'E-1': 'B35400', 'E1': 'B38E00', 'E#1': '4D8F00', 'F1': '4D8F00', 'F#1': '009100', 'G-1': '009100', 'G1': '003C1A', 'G#1': '000080', 'A-1': '000080', 'A1': '00004D', 'A#1': '00001A', 'B-1': '00001A', 'B1': '000000', 'C2': '9E0000', 'C#2': 'B50000', 'D-2': 'B50000', 'D2': 'CC3300', 'D#2': 'CC6D00', 'E-2': 'CC6D00', 'E2': 'CCA700', 'E#2': '66A800', 'F2': '66A800', 'F#2': '00AA00', 'G-2': '00AA00', 'G2': '005533', 'G#2': '000099', 'A-2': '000099', 'A2': '000066', 'A#2': '000033', 'B-2': '000033', 'B2': '000011', 'C3': 'B80000', 'C#3': 'CF1A00', 'D-3': 'CF1A00', 'D3': 'E64D09', 'D#3': 'E68708', 'E-3': 'E68708', 'E3': 'E6C108', 'E#3': '80C200', 'F3': '80C200', 'F#3': '1AC400', 'G-3': '1AC400', 'G3': '096F4D', 'G#3': '001AB3', 'A-3': '001AB3', 'A3': '000080', 'A#3': '09004D', 'B-3': '09004D', 'B3': '1A002B', 'C4': 'd10000', 'C#4': 'E83311', 'D-4': 'E83311', 'D4': 'ff6622', 'D#4': 'FFA021', 'E-4': 'FFA021', 'E4': 'ffda21', 'E#4': '99DB10', 'F4': '99DB10', 'F#4': '33dd00', 'G-4': '33dd00', 'G4': '228866', 'G#4': '1133cc', 'A-4': '1133cc', 'A4': '191999', 'A#4': '220066', 'B-4': '220066', 'B4': '330044', 'C5': 'EB1A1A', 'C#5': 'FF4D2B', 'D-5': 'FF4D2B', 'D5': 'FF803C', 'D#5': 'FFBA3B', 'E-5': 'FFBA3B', 'E5': 'FFF43B', 'E#5': 'B3F52A', 'F5': 'B3F52A', 'F#5': '4DF71A', 'G-5': '4DF71A', 'G5': '3CA280', 'G#5': '2B4DE6', 'A-5': '2B4DE6', 'A5': '3333B3', 'A#5': '3C1A80', 'B-5': '3C1A80', 'B5': '4D1A5E', 'C6': 'FF3333', 'C#6': 'FF6644', 'D-6': 'FF6644', 'D6': 'FF9955', 'D#6': 'FFD354', 'E-6': 'FFD354', 'E6': 'FFFF54', 'E#6': 'CCFF43', 'F6': 'CCFF43', 'F#6': '66FF33', 'G-6': '66FF33', 'G6': '55BB99', 'G#6': '4466FF', 'A-6': '4466FF', 'A6': '4C4CCC', 'A#6': '553399', 'B-6': '553399', 'B6': '663377', 'C7': 'FF4D4D', 'C#7': 'FF805E', 'D-7': 'FF805E', 'D7': 'FFB36F', 'D#7': 'FFED6E', 'E-7': 'FFED6E', 'E7': 'FFFF6E', 'E#7': 'E6FF5D', 'F7': 'E6FF5D', 'F#7': '80FF4D', 'G-7': '80FF4D', 'G7': '6FD5B3', 'G#7': '5E80FF', 'A-7': '5E80FF', 'A7': '6666E6', 'A#7': '6F4DB3', 'B-7': '6F4DB3', 'B7': '804D91'}
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    if lv == 1:
        v = int(value, 16)*17
        return v, v, v
    if lv == 3:
        return tuple(int(value[i:i+1], 16)*17 for i in range(0, 3))
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

def getInput():
    global songName
    songName = raw_input("Please enter the name of the song: ")
    
def initHTML():
    global htmlfile
    htmlfile = open("htmlfiles\\" + songName + ".html", 'w+')
    htmlfile.write("<head>\n<link rel=\"stylesheet\" type=\"text/css\" href=\"main.css\">\n</head>")

def averageColor(colors):
    total = 0
    for color in colors:
        total = total + color
    return int(total/len(colors))

def combineColors(colors):
    red = []
    green = []
    blue = []

    for color in colors:
        red.append(color[0])
        green.append(color[1])
        blue.append(color[2])

    combinedColor = (averageColor(red), averageColor(green), averageColor(blue))
    return combinedColor

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def cleanup():
    global htmlfile
    htmlfile.close()

def readFile():
    global COLOR_MAP
    song = open("textfiles\\" + songName + ".txt",'r')
    lines = song.readlines()
    for line in lines: # For all lines in the song file
        if line.strip():
            note_colors = []
            colors_to_combine = []
            notes = str.split(line)
            for note in notes: # For all of the notes on a single line
                note_colors.append(COLOR_MAP[note])
            for color in note_colors:
                colors_to_combine.append(hex_to_rgb(color))
            combinedColor = rgb_to_hex(combineColors(colors_to_combine))
            writeToHtml(combinedColor)
    song.close()
            
            
def writeToHtml(color):
    htmlfile.write("<div class=\"foo\" style=\"background-color:" + color +  "; width:50;height:50;float:left\"></div>")

def createTextFile():
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

getInput()
createTextFile()
initHTML()
colors = COLOR_MAP.values()
readFile()
cleanup();
