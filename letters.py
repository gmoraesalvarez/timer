# uncomment to demo at https://micropython.org/unicorn/

#import machine
#import framebuf

#i2c = machine.I2C('X')

#display = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

def draw_7seg_s(x,y,num_,size):

    num = abs(num_)
                        #A  B  C  D  E  F  G
    if num == 0: segs = [1, 1, 1, 0, 1, 1, 1]
    if num == 1: segs = [0, 0, 0, 0, 0, 1, 1]
    if num == 2: segs = [0, 1, 1, 1, 1, 1, 0]
    if num == 3: segs = [0, 0, 1, 1, 1, 1, 1]
    if num == 4: segs = [1, 0, 0, 1, 0, 1, 1]
    if num == 5: segs = [1, 0, 1, 1, 1, 0, 1]
    if num == 6: segs = [1, 1, 1, 1, 1, 0, 1]
    if num == 7: segs = [0, 0, 1, 0, 0, 1, 1]
    if num == 8: segs = [1, 1, 1, 1, 1, 1, 1]
    if num == 9: segs = [1, 0, 1, 1, 1, 1, 1]
    
    pad5 = (size//5)
    pad3 = (size//3)
    pad2 = (size//2)
    
    display.vline(x,y,size,segs[0])
    display.vline(x,y+pad3+size,size,segs[1])    
    display.hline(x+pad5,y-1,size,segs[2])
    display.hline(x+pad5,y+size,size,segs[3])
    display.hline(x+pad5,y+pad3+size+size,size,segs[4])
    display.vline(x+pad5+size,y,size,segs[5])
    display.vline(x+pad5+size,y+pad3+size,size,segs[6])

def draw_14seg_s(x,y,char_,size):
    
    #if char_ == "k":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                          #A  B  C  D  E  F  G  H  I  J  K  L  M  N
    if char_ == 0: segs = [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
    if char_ == 1: segs = [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
    if char_ == 2: segs = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 3: segs = [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 4: segs = [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 5: segs = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 6: segs = [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 7: segs = [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    if char_ == 8: segs = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == 9: segs = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]

    #                      |  |  -  -  _  |  |  \  |  /  -  /  |  \  
    if char_ == "a":segs= [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == "b":segs= [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    if char_ == "c":segs= [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "d":segs= [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
    if char_ == "e":segs= [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "f":segs= [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "g":segs= [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == "h":segs= [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0]
    if char_ == "i":segs= [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
    if char_ == "j":segs= [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    if char_ == 'k':segs= [1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    if char_ == "l":segs= [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "m":segs= [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
    if char_ == "n":segs= [1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1]
    if char_ == "o":segs= [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "p":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "q":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "r":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "s":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "t":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "u":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "v":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "x":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "y":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "z":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == '*':segs= [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    if char_ == ".":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "-":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "+":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "=":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == ":":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "!":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "(":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    
    if char_ == ")":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "/":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "\\":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if char_ == "?":segs= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    

    
    pad5 = (size//5)
    pad3 = (size//3)
    pad2 = (size//2)
    
    display.line(x,y,x+pad2,y+pad2+pad3+1,segs[7]) # H
    display.vline(x+pad2+1,y,size,segs[8])     # I
    display.line(x+pad2+1,y+size,x+size,y+1,segs[9]) # J
    display.hline(x+pad2+1,y+size,pad2,segs[10]) # K
    display.line(x+1,y+size+size,x+pad2+1,y+pad2+4,segs[11]) # L
    display.vline(x+pad2+1,y+size+1,size,segs[12]) # M
    display.line(x+pad2+1,y+size+1,x+size,y+size+size,segs[13]) # N
    
    display.vline(x,y,size,segs[0]) # A
    display.vline(x,y+pad3+size,size,segs[1])    # B
    display.hline(x+pad5,y-1,size,segs[2])    # C
    display.hline(x+pad5,y+size,pad2-1,segs[3])    # D
    display.hline(x+pad5,y+pad3+size+size,size,segs[4]) # E
    display.vline(x+pad5+size,y,size,segs[5]) # F
    display.vline(x+pad5+size,y+pad3+size,size,segs[6]) # G
    
#draw_7seg_s(1,2,1,5)
#draw_7seg_s(13,2,2,5)
#draw_7seg_s(24,2,3,5)
#draw_7seg_s(36,2,4,5)
#draw_7seg_s(48,2,5,5)

#draw_7seg_s(1,18,6,5)
#draw_7seg_s(13,18,7,5)
#draw_7seg_s(24,18,8,5)
#draw_7seg_s(36,18,9,5)
#draw_7seg_s(48,18,0,5)
    
#i2c.writeto(8, display)
