
global notes
COLORS = [
'F00','F10','F20','F30','F40','F50','F60','F70','F80','F90','FA0','FB0',
'FC0','FD0','FE0','FF0','FF0','EF0','DF0','CF0','BF0','AF0','9F0','8F0',
'7F0','6F0','5F0','4F0','3F0','2F0','1F0','0F0','0F0','0F1','0F2','0F3',
'0F4','0F5','0F6','0F7','0F8','0F9','0FA','0FB','0FC','0FD','0FE','0FF',
'0FF','0EF','0DF','0CF','0BF','0AF','09F','08F','07F','06F','05F','04F',
'03F','02F','01F','00F','00F','10F','20F','30F','40F','50F','60F','70F',
'80F','90F','A0F','B0F','C0F','D0F','E0F','F0F','F0F','F0E','F0D','F0C',
'F0B','F0A','F09','F08','F07','F06','F05','F04','F03','F02','F01','F00'
]

NOTES = ['C','C#','D-','D','D#','E-','E','E#','F','F#','G-','G','G#','A-','A','A#','B-','B']


notes = open("notes.txt",'w+')
notes.write("NOTES = [")
for x in range(10):
    for note in NOTES:
        notes.write("'" + note + str(x) + "',")
notes.write("]")
notes.close()
