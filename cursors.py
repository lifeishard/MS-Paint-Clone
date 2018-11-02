from pygame import *
screen = display.set_mode((1010,692))
display.set_caption("Street Art Creator V1.0")
state=0
pstate=0
mouse=[0,0,0,0,0,0,0,0]
mousen=1
fname="default"
extl=[".jpg",".bmp",".tga"]
extn=0
timeli=[]
timeff=0
LI=image.load("aaa.jpg")
lix,liy=LI.get_size()

ts=LI.subsurface(Rect(0, 0, 1000, 600))
screen.blit(image.load("paintbrush.jpg"),(20,620))
screen.blit(image.load("drop.jpg"),(80,620))
screen.blit(image.load("spray.jpg"),(140,620))
screen.blit(image.load("paintball.jpg"),(200,620))
screen.blit(image.load("stamp.jpg"),(260,620))
screen.blit(image.load("pencil.jpg"),(320,620))
screen.blit(image.load("paintbucket.jpg"),(380,620))
screen.blit(image.load("brush.jpg"),(440,620))
dh=600#surface height
dw=1000#surface weight
mx=0#mouse pos
my=0#mouse pos
rad=5#radius of tool
onscr=1
db=Surface((dw,dh))
db.fill((255,255,255))
screen.blit(db,(0,0))
screen.blit(ts,(0,0))
font.init()
f=font.SysFont("Courier New",15)
def load(sur):
    sx,sy=sur.get_size()
    bar()
def bar():
    screen.fill((255,0,0),Rect(0,990,10,600))
display.flip()
(      
"           ####         ",
"############..#         ",
"########   ####         ",
"######      ##          ",
"#####     ######        ",
"####    ##########      ",
"###   ##############    ",
"##    #............#    ",
"#     #............#    ",
"      #............#    ",
"      #............#    ",
"      #............#    ",
"      #...######...#    ",
"      #..##....##..#    ",
"      #..##........#    ",
"      #...######...#    ",
"      #........##..#    ",
"      #..##....##..#    ",
"      #...######...#    ",
"      #............#    ",
"      #............#    ",
"      #............#    ",
"      #............#    ",
"      ##############    "
)
curstrli=[
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.#............#.#   ",
"    #.#..........#.#    ",
"     #.#........#.#     ",
"      #.#......#.#      ",
"       #.#....#.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.######.#       ",
"      #.########.#      ",
"     #.##########.#     ",
"    #.############.#    ",
"   #.##############.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.#..........#.#    ",
"     #.#........#.#     ",
"      #.#......#.#      ",
"       #.#....#.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.######.#       ",
"      #.########.#      ",
"     #.##########.#     ",
"    #.############.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.############.#    ",
"     #.#........#.#     ",
"      #.#......#.#      ",
"       #.#....#.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.######.#       ",
"      #.########.#      ",
"     #.##########.#     ",
"    #.#..........#.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.############.#    ",
"     #.##########.#     ",
"      #.#......#.#      ",
"       #.#....#.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.######.#       ",
"      #.########.#      ",
"     #.#........#.#     ",
"    #.#..........#.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.############.#    ",
"     #.##########.#     ",
"      #.########.#      ",
"       #.#....#.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.######.#       ",
"      #.#......#.#      ",
"     #.#........#.#     ",
"    #.#..........#.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.############.#    ",
"     #.##########.#     ",
"      #.########.#      ",
"       #.######.#       ",
"        #.#..#.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.####.#        ",
"       #.#....#.#       ",
"      #.#......#.#      ",
"     #.#........#.#     ",
"    #.#..........#.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),
(      
"########################",
" #....................# ",
"  #.################.#  ",
"   #.##############.#   ",
"    #.############.#    ",
"     #.##########.#     ",
"      #.########.#      ",
"       #.######.#       ",
"        #.####.#        ",
"         #.##.#         ",
"          #..#          ",
"          #..#          ",
"         #.##.#         ",
"        #.#..#.#        ",
"       #.#....#.#       ",
"      #.#......#.#      ",
"     #.#........#.#     ",
"    #.#..........#.#    ",
"   #.#............#.#   ",
"  #.################.#  ",
" #....................# ",
"########################",
"                        ",
"                        "
),(      
"          ####          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          ####          ",
"                        ",
"                        ",
"                        ",
"#######   ####   #######",
"#.....#   #..#   #.....#",
"#.....#   #..#   #.....#",
"#######   ####   #######",
"                        ",
"                        ",
"                        ",
"          ####          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          #..#          ",
"          ####          "
)
,(
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"###########.########### ",
"....................... ",
"###########.########### ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"          #.#           ",
"                        ",
)
]
curdmli=[]
a,b=cursors.compile(curstrli[0],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[1],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[2],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[3],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[4],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[5],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[6],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[7],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
a,b=cursors.compile(curstrli[8],black='#', white='.', xor='o')
curdmli.append(((24,24),(11,11),a,b))
curdmli.append(cursors.arrow)
curdmli.append(cursors.ball)
curdmli.append(cursors.broken_x)
a,b=cursors.compile(cursors.textmarker_strings,black='X', white='.', xor='o')
curdmli.append(((8,16),(3,5),a,b))
a,b=cursors.compile(cursors.sizer_x_strings,black='X', white='.', xor='o')
curdmli.append(((24,16),(8,5),a,b))
a,b=cursors.compile(cursors.sizer_y_strings,black='X', white='.', xor='o')
curdmli.append(((16,24),(5,9),a,b))
a,b=cursors.compile(cursors.sizer_xy_strings,black='X', white='.', xor='o')
curdmli.append(((24,16),(6,6),a,b))
running = True
#status 0=default
#status 1=many button
#status 2=color
#status 3=wait
#status 4=text
#status 5=paintbrush
#status 6=eraser
#status 7=pencil
#status 8=spray
#status 9=stamp
#status 10=gun
#status 11=change size
def drawr():
    draw.circle(screen,(255,255,255),(mx,my),rad-1,1)
    draw.circle(screen,(0,0,0),(mx,my),rad,1)
    draw.circle(screen,(255,255,255),(mx,my),rad+1,1)
    display.flip()
def curchang(y):
    mouse.set_cursor(*curdmli[y])
def cordout():
    global mx
    global my
    if onscr>=1:
        c=str("x: %4d, y: %4d"%(mx,my))
        screen.blit(f.render(c,True,(255,255,255),(0,0,0)),(800,670))
        display.flip()
    else:
        c=str("x:    , y:    "%(mx,my))
        screen.blit(f.render(c,True,(255,255,255),(0,0,0)),(800,670))
        display.flip()
def emquit():
    saf()
    global running
    font.quit()
    running=False
def saf():
    image.save(db,fname+extl[extn])
def copyf():
    print "copied"
def pastef():
    print "pasted"
def pt():
    print "time backward"
def ft():
    print "time forward"
def s11init():
    global status
    global pstatus
    pstatus=status
    status=11
    curchang(13)
    onscr=2
    return s11()
def s11():
    return
        
def s0():
    for evnt in event.get():
        
        if evnt.type==4:
            cordout()
        elif evnt.type==2:
            if evnt.mod==64:
                if evnt.key==115:
                    saf()
                elif evnt.key==122:
                    pt()
                elif evnt.key==118:
                    pastef()
                elif evnt.key==99:
                    copyf()
                elif evnt.key==121:
                    ft()
        elif evnt.type==Quit:
            return emquit
nfun=s0
pfun=s0
def s0init():
    global status
    global pstatus
    pstatus=status
    status=0
    curchang(9)
    return s0()
def s0():
    for evnt in event.get():
        
        if evnt.type==4:
            cordout()
        elif evnt.type==2:
            if evnt.mod==64:
                if evnt.key==115:
                    saf()
                elif evnt.key==122:
                    pt()
                elif evnt.key==118:
                    pastef()
                elif evnt.key==99:
                    copyf()
                elif evnt.key==121:
                    ft()
        elif evnt.type==Quit:
            return emquit
nfun=s0
pfun=s0
def s1init():
    global status
    global pstatus
    pstatus=status
    status=1
    curchang(10)
    return s1()
def s1():
    for evnt in event.get():
        if evnt.type==4:
            if evnt.buttons==(0,0,0):
                return pfun
            cordout(*evnt.pos)
        elif evnt.type==Quit:
            return emquit
def s2init():
    global status
    global pstatus
    pstatus=status
    curchang(11)
    status=2
    return s2()
def s3init(a):
    global status
    global pstatus
    pstatus=status
    status=3
    return s3(a)
def s4init():
    global status
    global pstatus
    pstatus=status
    status=4
    curchang(12)
    return s4()
def s4init():
    global status
    global pstatus
    pstatus=status
    status=4
    curchang(12)
    return s4()
def s5init():
    global status
    global pstatus
    pstatus=status
    status=5
    curchang(8)
    return s5()
def s6init():
    global status
    global pstatus
    pstatus=status
    status=6
    curchang(8)
    return s6()
def s7init():
    global status
    global pstatus
    pstatus=status
    status=7
    curchang(8)
    return s7()
def s8init():
    global status
    global pstatus
    pstatus=status
    status=8
    curchang(8)
    return s8()
def s9init():
    global status
    global pstatus
    pstatus=status
    status=9
    curchang(8)
    return s9()
def s10init():
    global status
    global pstatus
    pstatus=status
    status=10
    curchang(7)
    return s10()


running=True
bar()
display.flip
a=input("lol")
    
    #pygame.cursors.diamond
#pygame.cursors.broken_x
#pygame.cursors.tri_left
#pygame.cursors.tri_right
quit()
