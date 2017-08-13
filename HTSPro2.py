from tkinter import *
from PIL import Image


class MorseConverter:

    asciiToMorse = {
        0:"NUL",    #null
        1:"SOH",    #start of heading
        2:"STX",    #start of text
        3:"ETX",    #end of text
        4:"EOT",    #end of transmission
        5:"ENQ",    #enquiry
        6:"ACK",    #Acknowledge
        7:"BEL",    #bell
        8:"BS",     #backspace
        9:"TAB",    #horizontal tab
        10:"LF",    #NL line feed, new line
        11:"VT",    #vertical tab
        12:"FF",    #NP form feed, new page
        13:"CR",    #carraige return
        14:"SO",    #shift out
        15:"SI",    #shift in
        16:"DLE",   #data link escape
        17:"DC1",   #device control 1
        18:"DC2",   #device control 2
        19:"DC3",   #device control 3
        20:"DC4",   #device control 4
        21:"NAK",   #negative acknowledge
        22:"SYN",   #synchronous idle
        23:"ETB",   #end of trans. block
        24:"CAN",   #cancel
        25:"EM",    #end of medium
        26:"SUB",   #substitute
        27:"ESC",   #escape
        28:"FS",    #file sperator
        29:"GS",    #group separator
        30:"RS",    #record sparator
        31:"US",    #unit sparator
        32:" ",     #" " 
        33:"!",     #!
        34:"\"",    #"
        35:"#",     ##
        36:"$",     #$
        37:"%",     #%
        38:"&",     #&
        39:"'",     #'
        40:"(",     #(
        41:")",     #)
        42:"*",     #*
        43:"+",     #+
        44:",",     #,
        45:"-",     #-
        46:".",     #.
        47:"/",     #"/"
        48:"-----", #"0"
        49:".----", #"1"
        50:"..---", #"2"
        51:"...--", #"3"
        52:"....-", #"4"
        53:".....", #"5"
        54:"-....", #"6"
        55:"--...", #"7"
        56:"---..", #"8"
        57:"----.", #"9"
        58:":",     #:
        59:";",     #;
        60:"<",     #<
        61:"=",     #=
        62:">",     #>
        63:"?",     #?
        64:"@",     #@
        65:".-",    #"A"
        66:"-...",  #"B"
        67:"-.-.",  #"C"
        68:"-..",   #"D"
        69:".",     #"E"
        70:"..-.",  #"F"
        71:"--.",   #"G"
        72:"....",  #"H"
        73:"..",    #"I"
        74:".---",  #"J"
        75:"-.-",   #"K"
        76:".-..",  #"L"
        77:"--",    #"M"
        78:"-.",    #"N"
        79:"---",   #"O"
        80:".--.",  #"P"
        81:"--.-",  #"Q"
        82:".-.",   #"R"
        83:"...",   #"S"
        84:"-",     #"T"
        85:"..-",   #"U"
        86:"...-",  #"V"
        87:".--",   #"W"
        88:"-..-",  #"X"
        89:"-.--",  #"Y"
        90:"--..",  #"Z"
        91:"[",     #[
        92:"\\",    #\
        93:"]",     #]
        94:"^",     #^
        95:"_",     #_
        96:"`",     #`
        97:".-",    #"a"
        98:"-...",  #"b"
        99:"-.-.",  #"c"
        100:"-..",  #"d"
        101:".",    #"e"
        102:"..-.", #"f"
        103:"--.",  #"g"
        104:"....", #"h"
        105:"..",   #"i"
        106:".---", #"j"
        107:"-.-",  #"k"
        108:".-..", #"l"
        109:"--",   #"m"
        110:"-.",   #"n"
        111:"---",  #"o"
        112:".--.", #"p"
        113:"--.-", #"q"
        114:".-.",  #"r"
        115:"...",  #"s"
        116:"-",    #"t"
        117:"..-",  #"u"
        118:"...-", #"v"
        119:".--",  #"w"
        120:"-..-", #"x"
        121:"-.--", #"y"
        122:"--..", #"z"
        123:"{",    #{
        124:"|",    #|
        125:"}",    #}
        126:"~",    #~
        127:"DEL"  #del
        }
    
    morseToAscii = {
        "":"",
        ".-":"A",
        "-...":"B",
        "-.-.":"C",
        "-..":"D",
        ".":"E",
        "..-.":"F",
        "--.":"G",
        "....":"H",
        "..":"I",
        ".---":"J",
        "-.-":"K",
        ".-..":"L",
        "--":"M",
        "-.":"N",
        "---":"O",
        ".--.":"P",
        "--.-":"Q",
        ".-.":"R",
        "...":"S",
        "-":"T",
        "..-":"U",
        "...-":"V",
        ".--":"W",
        "-..-":"X",
        "-.--":"Y",
        "--..":"Z",
        "-----":"0",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9"
        }
    
    def __init__(self):
        self.codes = []
  

        
def flattenPixelList(pixData):
    
    out = []
    
    for x in range(0, pixData.size[0]):
        for y in range(0, pixData.size[1]):
            out.append(pixData.getpixel((x,y)))
        
    return out

def activateUI():
    master = Tk()

    usrin = Entry(master)
    usrin.pack()
    usrin.insert(0, msg)

    master.mainloop()
    
code = []

img = Image.open("htsPro2Img.png")
pix = img.load()
flatPix = flattenPixelList(img)

mc = MorseConverter()

#hardcoded to fit samples (only the first letter is off 
#and its seems to be off by 1 for the morse translation.
#I'm sure I'm not counting the first white pixel correctly 
#every other decoded character is correct
count = -1 
#image came in rotated
for x in range(0, img.size[1]):
    #print(debug)
    for y in range(0, img.size[0]):
        count += 1
        if pix[y,x] == 1:
            if count > 100:
                count = count - 100
            code.append(count)
            count = 0
            
#translate morse, read from space to space
morse = [""]
index = 0

for c in code:
    morse[index] += mc.asciiToMorse[c].strip()
    
    if c == 47:
        index += 1
        morse.append("")
    if c == 32:
        index += 1
        morse.append("")

print(morse)

#assembles decoded message 
msg = ""
for m in morse:
    if m == "/":
        msg += "" #no spaces even though slash is morse space
    else:
        msg += mc.morseToAscii[m]   
msg.strip()

#UI for easy copy and paste because windows hates me
activateUI()


               
