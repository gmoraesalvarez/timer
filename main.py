from machine import Pin, I2C
import machine
import ssd1306
#import ssd1306big
import random
from time import sleep
from time import sleep_ms
from time import ticks_ms
from time import ticks_diff
from time import time
import os
import framebuf
import network

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

p12 = Pin(12, Pin.IN, Pin.PULL_UP)
p13 = Pin(13, Pin.IN, Pin.PULL_UP)
p14 = Pin(14, Pin.IN, Pin.PULL_UP)
p2 = Pin(2, Pin.IN, Pin.PULL_UP)
p0 = Pin(0, Pin.OUT)
buzz = machine.PWM(p0)
buzz.freq(900)
buzz.duty(0)

die_size = [4,4,4,4,4,4]
die_index = 0

timepast = 0
pausetime = 0

starttime = time()
running = False
text = ""
index_str = "A"
buzzstart = True
tock = 0
line_pos = -5
buzz_ms = ticks_ms()
buzz_tock = 0
sleeptimer = time()
due = False

def gotobed(p):
    display.fill(0)
    display.text('BYE',56,28,1)
    display.show()
    sleep(2)
    display.fill(0)
    display.show()
    machine.deepsleep()

def startpause():
    global running 
    global starttime
    global pausetime
    global line_pos
    global sleeptimer
    line_pos = -5
    starttime = time()
    buzz.duty(0)
    if running:
        running = False
        pausetime = timepast
    else:
        running = True
        starttime -= pausetime
            
def cycleTimer():
    global die_index
    global pausetime
    global remain
    global due
    if pausetime > 0:
        pausetime = 0
        due = False
    else:
        die_index += 1
        if die_index >= 6: die_index = 0
        set_index_str()
        save_cfg()
    remain = die_size[die_index]
    

def set_index_str():
    global index_str
    if die_index == 0:
            index_str = "A"
    if die_index == 1:
            index_str = " B"
    if die_index == 2:
            index_str = "  C"
    if die_index == 3:
            index_str = "   D"
    if die_index == 4: 
            index_str = "    E"
    if die_index == 5:
            index_str = "     F"
        
def silence():
    buzz.duty(0)


def scream(ms):
    buzz.duty(0)
    
    if ms in [1,2,3,31,32,33]:
        buzz.freq(600)
        buzz.duty(512)
    if ms in [7,8,37,38]:
        buzz.freq(800)
        buzz.duty(512)
    if ms in [11,12,41,42]:
        buzz.freq(900)
        buzz.duty(512)
    
    
    
def inc():
    die_size[die_index] += 30
    if die_size[die_index] >= 3600: die_size[die_index] = 0
    
    
def dec():
    die_size[die_index] -= 30
    if die_size[die_index] < 0: die_size[die_index] = 3600

    
def time_to_str(seconds):
    min = seconds // 60
    sec = seconds % 60
    string = "%02d" % min
    string += ":"
    string += "%02d" % sec
    return string


def time_to_7seg(seconds):
    min = seconds // 60
    sec = seconds % 60

    min_0 = min // 10
    draw_7seg(4, 32, min_0)

    min_1 = min % 10
    draw_7seg(24, 32, min_1)

    display.vline(42,40,2,1)
    display.vline(42,44,2,1)
    
    sec_0 = sec // 10
    draw_7seg(46, 32, sec_0)
        
    sec_1 = sec % 10
    draw_7seg(66, 32, sec_1)
        
    
    
def draw_7seg(x,y,num_):

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
    
    display.vline(x,y,8,segs[0])
    display.vline(x,y+12,8,segs[1])    
    display.hline(x+3,y-1,8,segs[2])
    display.hline(x+3,y+10,8,segs[3])
    display.hline(x+3,y+20,8,segs[4])
    display.vline(x+12,y,8,segs[5])
    display.vline(x+12,y+12,8,segs[6])

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
    
    display.vline(x,y,size,segs[0])
    display.vline(x,y+2+size,size,segs[1])    
    display.hline(x+(size//4),y-1,size,segs[2])
    display.hline(x+(size//4),y+2+size,size,segs[3])
    display.hline(x+(size//4),y+4+size+size,size,segs[4])
    display.vline(x+(size//2)+size,y,size,segs[5])
    display.vline(x+(size//2)+size,y+4+size,size,segs[6])

    
def save_cfg():
    file = open("cfg.txt", "w")
    cfg = ','.join(str(x) for x in die_size)
    file.write(cfg)
    file.close()

def show():
    display.fill(0)
    timer_time_str = ""
    timer_time_str += time_to_str(die_size[die_index])
    #timer_time_str += "|"
       
    display.text(timer_time_str,82,2,1)
    display.text(index_str,2,2,1)
    #if buzzstart: display.text("***",110,56,1)
    time_to_7seg(remain)
    
    display.hline(line_pos,60,4,1)
    display.show()
    
###################################################
###################################################
#file.write(str(die_size[0]))
print("loading config")
file = open("cfg.txt", "r")
cfg = file.read()
file.close()
die_size_str = cfg.split(',', 6)
die_size[0] = int(die_size_str[0])
die_size[1] = int(die_size_str[1])
die_size[2] = int(die_size_str[2])
die_size[3] = int(die_size_str[3])
die_size[4] = int(die_size_str[4])
die_size[5] = int(die_size_str[5])
remain = die_size[die_index] - timepast
set_index_str()


sta_if = network.WLAN(network.STA_IF)
sta_if.active(False)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)


display.fill(0)
display.text('HELLO',56,28,1)
display.show()

while True:
    #print("running")
    if p12.value() == 0:
        startpause()
        print("startpause")
        sleep(0.15)
    if p13.value() == 0:
        cycleTimer()
        print("cycleDieSides")
        sleep(0.1)
    if p14.value() == 0:
        inc()
        print("more")
        sleep(0.1)
    if p2.value() == 0:
        dec()
        print("less")
        sleep(0.1)
    if running:
        sleeptimer = time()
        if ticks_diff(ticks_ms(), tock) > 16:
            line_pos += 8
            tock = ticks_ms()
        if line_pos > 127:
            line_pos = 0
        timepast = time() - starttime
        remain = die_size[die_index] - timepast
        if remain == 0:
            buzzstart = True
            due = True
            starttime = time()      
        if buzzstart:
            if ticks_diff(ticks_ms(), buzz_ms) > 16:
                buzz_tock += 1
                buzz_ms = ticks_ms()
            if buzz_tock > 60:
                buzz_tock = 0
            scream(buzz_tock)
        if due:
            remain = timepast
    else:
        silence()
        buzzstart = False
        if pausetime == 0:
            #if ((time() - sleeptimer) % 2) == 0: print("counting down to sleep")
            if (time() - sleeptimer) > 60:
                gotobed(0)
                
    show()
    
