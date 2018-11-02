from pygame import *
from math import *
from pygame import *
from tkFileDialog import * #used for saving and opening
from tkColorChooser import * #used for color choosing
from Tkinter import * #used for Tkinter stuff
from time import *
from random import *
from collections import *
################################################################################
################################Initialization##################################
################################################################################
screen =display.set_mode((1010,692)) #my display
display.set_caption("Street Art Creator V1.0")
x=980
y=588
mx=0
my=0
canvasx=0
canvasy=0
gridx=0
gridx=0
seed()
canvas=Surface((980,588))
visiblecanvas=canvas
font.init()
font12=font.SysFont("Times New Roman",12)
font16=font.SysFont("Times New Roman",16)
screen.blit(image.load("updown.jpg"),(980,588))
screen.blit(image.load("backgrad.jpg"),(0,618))
screen.blit(image.load("wider.jpg"),(980,606))
screen.blit(image.load("paintbrush.jpg"),(5,623))
screen.blit(image.load("drop.jpg"),(65,623))
screen.blit(image.load("spray.jpg"),(125,623))
screen.blit(image.load("paintball.jpg"),(185,623))
screen.blit(image.load("stamp.jpg"),(245,623))
screen.blit(image.load("pencil.jpg"),(305,623))
screen.blit(image.load("paintbucket.jpg"),(365,623))
screen.blit(image.load("brush.jpg"),(425,623))
screen.blit(image.load("replace.jpg"),(945,618))
screen.blit(image.load("undo.jpg"),(945,639))
screen.blit(image.load("redo.jpg"),(967,639))
screen.blit(image.load("save.jpg"),(989,639))
screen.blit(image.load("grid.jpg"),(902,618))
screen.blit(image.load("color.jpg"),(859,618))
screen.blit(image.load("shapes.jpg"),(775,618))
screen.blit(image.load("polygon.jpg"),(741,618))
screen.blit(image.load("line.jpg"),(717,652))
screen.blit(image.load("cut.jpg"),(717,618))
temp=Surface((25,5))
temp.fill((0,0,0))
screen.blit(temp,(989,661))
temp=Surface((25,22))
temp.fill((255,255,255))
screen.blit(temp,(986,618))
screen.blit(image.load("open.jpg"),(987,618))
grid=Surface((990,600))
grid.fill((255,255,255))
grid.set_colorkey((255,255,255))
for i in range(9,989,10):
    draw.line(grid,(0,0,0),(i-1,0),(i-1,599))
for i in range(9,599,10):
    draw.line(grid,(0,0,0),(0,i-1),(989,i-1))
################################################################################
##############################Color Functions###################################
################################################################################
colorpallet=Surface((100,40))
for i in range(5):
    colorpallet.fill((255,255,255),Rect(i*20+1,1,18,18))
    colorpallet.fill((255,255,255),Rect(i*20+1,21,18,18))
colorqueue=[(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,128,0),(255,255,0),(255,0,255),(0,255,255),(128,128,128)]
def recolorpallet():
    colorpallet.fill(colorqueue[0],Rect(2,2,16,16))
    colorpallet.fill(colorqueue[1],Rect(22,2,16,16))
    colorpallet.fill(colorqueue[2],Rect(42,2,16,16))
    colorpallet.fill(colorqueue[3],Rect(62,2,16,16))
    colorpallet.fill(colorqueue[4],Rect(82,2,16,16))
    colorpallet.fill(colorqueue[5],Rect(2,22,16,16))
    colorpallet.fill(colorqueue[6],Rect(22,22,16,16))
    colorpallet.fill(colorqueue[7],Rect(42,22,16,16))
    colorpallet.fill(colorqueue[8],Rect(62,22,16,16))
    colorpallet.fill(colorqueue[9],Rect(82,22,16,16))
    screen.blit(colorpallet,(759,652))
def changecolor(tempcolor):
    if colorqueue.count(tempcolor)==0:
        colorqueue.pop()
    else:
        colorqueue.remove(tempcolor)
    colorqueue.insert(0,tempcolor)
    recolorpallet()
recolorpallet()
useless=Tk()
useless.withdraw()
def colormenu():
    tempr=askcolor(parent=useless)
    if tempr=="":
        return
    changecolor(tempr[0])
def colorchooser():
   while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                changecolor(visiblecanvas.get_at((mx,my)))
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def colorreplacer():
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==5 and evnt.button==1 and mx<x and my<y:
                pixelreplace=PixelArray(canvas)
                pixelreplace.replace(visiblecanvas.get_at((mx,my)),colorqueue[0])
                del pixelreplace
                canvasload(canvas,1)
                trackaction()
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def notincolor():
    for i in range(256):
        if colorqueue.count((i,i,i))==0:
            return (i,i,i)
################################################################################
##########################miscellaneous functions###############################
################################################################################
largey=False
largex=False
gridshow=True
cordtemp=Rect(930,661,48,31)
screen.fill((0,0,0),cordtemp)
temp=font16.render("Y:",True,(255,0,0),(0,0,0))
screen.blit(temp,(965-temp.get_width(),676))
temp=font16.render("X:",True,(255,0,0),(0,0,0))
screen.blit(temp,(965-temp.get_width(),661))
temp=font12.render("This message is a test. If you can read this properly, the program is working!",True,(255,255,255),(0,0,0))
screen.blit(temp,(0,675))
screen.blit(image.load("rotate.jpg"),(859,659))
screen.blit(image.load("ro360.jpg"),(883,659))
screen.blit(image.load("flip.jpg"),(900,659))
temp=font16.render("Tool size:",True,(255,0,0),(0,0,0))
fit=Rect(922,676,3,2)
screen.fill((0,0,0),fit)
screen.blit(temp,(859,676))
cordrefresh=Rect(964,661,48,31)
toolrefresh=Rect(923,676,27,16)
undostack=[]
redostack=[]
def trackaction():
    global temporarycanvas
    global redostack
    undostack.append(temporarycanvas)
    temporarycanvas=canvas
    redostack=[]
def updatecord():
    if mx<980 and my<588:
        screen.fill((0,0,0),cordrefresh)
        screen.blit(transform.rotate(sliderbasey,270),(980,0))
        draw.line(screen,(0,255,0),(980,my),(994,my))
        temp=font16.render("%5d"%(canvasy+my),True,(0,255,0),(0,0,0))
        screen.blit(temp,(964,676))
        screen.blit(sliderbasex,(0,588))
        draw.line(screen,(0,255,0),(mx,588),(mx,602))
        temp=font16.render("%5d"%(canvasx+mx),True,(0,255,0),(0,0,0))
        screen.blit(temp,(964,661))
toolsizelist=[5,5,5,5,5,1,5]
def toolsize(toolnum):
    screen.fill((0,0,0),toolrefresh)
    tempsize=toolsizelist[toolnum]
    if tempsize>0:
        temp=font16.render("%3d"%tempsize,True,(0,255,0),(0,0,0))
        screen.blit(temp,(923,676))
toolsize(0)
toolinfolist=["<<Draw rectangles>> Right click to cancel. Scroll to change border width. Shift for filled rectangles.",
              "<<Draw ovals>> Right click to cancel. Scroll to change border width. Shift for filled ovals.",
              "<<Draw lines>> Right click to cancel. Scroll to change line width.",
              "<<Paintbrush>> Right click to cancel. Scroll to change brush size.",
              "<<Eraser>> Right click to cancel. Scroll to change eraser size. Number keys to change color.",
              "<<Paintball>> Scroll to change ammo size.",
              "<<Spray paint>> Right click to cancel. Scroll to change nozzle size.",
              "<<Stamps>> Scroll to change stamp size.",
              "Did you know you can perform these operations anytime? Number keys=Change color. Ctrl+s=Save,Ctrl+z=Undo,Ctrl+y=Redo",
              "<<Crop Canvas>> Draw a box around the area you want to keep.",
              "<<Pencil>>Right click to cancel.",
              "<<Paint bucket>>Good ol' Paintbucket.",
              "<<Color chooser>> Left click on the Canvas to grab your color.",
              "<<Draw polygons>>Press Enter key to close your Polygon. Shift for filled polygons.",
              "<<Canvas Cleaner>> Wipes your canvas clean!",
              "<<Save as>> To use quicksave just press Ctrl+s anytime",
              "<<Open image>> Now you can doodle on any image!",
              "<<Undo>> No more silly mistakes! Ctrl+z anytime.",
              "<<Redo>> Bad undo? No problem for the Redo! Ctrl+y anytime.",
              "<<Scroll bar>> Click and drag the bar to view those big pictures.",
              "<<Canvas Resize>> Hold left mouse button and scroll to resize. Scroll Up-smaller canvas.Scroll Down-larger canvas",
              "<<Grid display>> Want to draw accurately? Click to toggle grid on or off.",
              "<<Color Pallet>> Click on the color you want to change it to that color.",
              "<<Advanced color chooser>> Want more colors? You've comed to the right place.",
              "<<Rotate 90 degrees>> It spins clockwise.",
              "<<Advanced rotate>> Scroll down to rotate image clockwise, Scroll up to rotate image counter-clockwise.",
              "<<Horizontal mirror>> Reversed your canvas horizontally.",
              "<<Vertical mirror>> Reversed your canvas vertically.",
              "<<Color swap>> Swap any color on your canvas for your chosen color."
              ]
def toolinfo(a):
    return
def canvascheckx():#a function that changes a x axis variable based on canvas size
    global largex
    if x>980:
        largex=True
    else:
        largex=False
def canvaschecky():#a function that changes a y axis variable based on canvas size
    global largey
    if y>588:
        largey=True
    else:
        largey=False
def emquit():
    global font12
    global font16
    del font12
    del font16
    font.quit()
    if ifsave==False:
        backupsave()
    quit()
def undo():
    global temporarycanvas
    if len(undostack)!=0:
        redostack.append(temporarycanvas)
        temporarycanvas=undostack.pop()
        canvasload(temporarycanvas,1)
def redo():
    global temporarycanvas
    if len(redostack)!=0:
        undostack.append(temporarycanvas)
        temporarycanvas=redostack.pop()
        canvasload(temporarycanvas,1)
def cleaner():
    canvas.fill((255,255,255))
    visiblescreenrefresh()
    trackaction()
def canvascheck():
    tx,ty=visiblecanvas.get_size()
    if mx<tx and my<ty:
        return True
    return False
mouselayer=Surface((980,588))
mouselayer.set_colorkey((128,128,128))
def rangedisplay(toolnum):
    if toolnum==3:
        mouselayer.fill((128,128,128))
        draw.circle(mouselayer,(255,255,255),(mx,my),toolsizelist[3]+1,1)
        draw.circle(mouselayer,(0,0,0),(mx,my),toolsizelist[3]+2,1)
    if toolnum==6:
        mouselayer.fill((128,128,128))
        draw.circle(mouselayer,(255,255,255),(mx,my),toolsizelist[6]+1,1)
        draw.circle(mouselayer,(0,0,0),(mx,my),toolsizelist[6]+2,1)
    if toolnum==4:
        mouselayer.fill((128,128,128))
        temprad=toolsizelist[4]*2+4
        mouselayer.fill((0,0,0),Rect(mx-toolsizelist[4]-2,my-toolsizelist[4]-2,temprad,temprad))
        temprad-=2
        mouselayer.fill((255,255,255),Rect(mx-toolsizelist[4]-1,my-toolsizelist[4]-1,temprad,temprad))
        temprad-=2
        mouselayer.fill((128,128,128),Rect(mx-toolsizelist[4],my-toolsizelist[4],temprad,temprad))
################################################################################
################################Shape functions#################################
################################################################################
def recttool():
    global mx
    global my
    altfunction=False
    colorfill=False
    clicked=False
    toolsize(0)
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    screen.set_clip(Rect(0,0,980,588))
                    minx=min(startx,mx)
                    maxx=max(startx,mx)
                    miny=min(starty,my)
                    maxy=max(starty,my)
                    mindist=min((maxx-minx),(maxy-miny))+1
                    if altfunction==False:
                        if colorfill==False:
                            if toolsizelist[0]<mindist:
                                mindist=toolsizelist[0]
                            tempx=maxx-mindist+1
                            tempy=maxy-mindist+1
                            xdist=maxx-minx+1
                            ydist=maxy-miny+1
                            visiblescreenrefresh()
                            screen.fill(colorqueue[0],Rect(minx,miny,xdist,mindist))
                            screen.fill(colorqueue[0],Rect(minx,tempy,xdist,mindist))
                            screen.fill(colorqueue[0],Rect(minx,miny,mindist,ydist))
                            screen.fill(colorqueue[0],Rect(tempx,miny,mindist,ydist))
                        else:
                            visiblescreenrefresh()
                            screen.fill((colorqueue[0]),Rect(minx,miny,maxx-minx+1,maxy-miny+1))
                    else:
                        if colorfill==False:
                            square=mindist
                            if toolsizelist[0]<mindist:
                                mindist=toolsizelist[0]
                            cornery=miny+square-1
                            cornerx=minx+square-1
                            tempx=cornerx-mindist+1
                            tempy=cornery-mindist+1
                            visiblescreenrefresh()
                            screen.fill(colorqueue[0],Rect(minx,miny,square,mindist))
                            screen.fill(colorqueue[0],Rect(minx,tempy,square,mindist))
                            screen.fill(colorqueue[0],Rect(minx,miny,mindist,square))
                            screen.fill(colorqueue[0],Rect(tempx,miny,mindist,square))
                        else:
                            visiblescreenrefresh()
                            screen.fill((colorqueue[0]),Rect(minx,miny,mindist,mindist))
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                startx=mx
                starty=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                minx=min(startx,mx)
                maxx=max(startx,mx)
                miny=min(starty,my)
                maxy=max(starty,my)
                mindist=min((maxx-minx),(maxy-miny))+1
                if altfunction==False:
                    if colorfill==False:
                        if toolsizelist[0]<mindist:
                            mindist=toolsizelist[0]
                        tempx=maxx-mindist+1
                        tempy=maxy-mindist+1
                        xdist=maxx-minx+1
                        ydist=maxy-miny+1
                        visiblecanvas.fill(colorqueue[0],Rect(minx,miny,xdist,mindist))
                        visiblecanvas.fill(colorqueue[0],Rect(minx,tempy,xdist,mindist))
                        visiblecanvas.fill(colorqueue[0],Rect(minx,miny,mindist,ydist))
                        visiblecanvas.fill(colorqueue[0],Rect(tempx,miny,mindist,ydist))
                    else:
                        visiblecanvas.fill((colorqueue[0]),Rect(minx,miny,maxx-minx+1,maxy-miny+1))
                else:
                    if colorfill==False:
                        square=mindist
                        if toolsizelist[0]<mindist:
                            mindist=toolsizelist[0]
                        cornery=miny+square-1
                        cornerx=minx+square-1
                        tempx=cornerx-mindist+1
                        tempy=cornery-mindist+1
                        visiblecanvas.fill(colorqueue[0],Rect(minx,miny,square,mindist))
                        visiblecanvas.fill(colorqueue[0],Rect(minx,tempy,square,mindist))
                        visiblecanvas.fill(colorqueue[0],Rect(minx,miny,mindist,square))
                        visiblecanvas.fill(colorqueue[0],Rect(tempx,miny,mindist,square))
                    else:
                        visiblecanvas.fill((colorqueue[0]),Rect(minx,miny,mindist,mindist))
                visiblescreenrefresh()
                trackaction()
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[0]>1:
                    toolsizelist[0]-=1
                    toolsize(0)
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[0]<295:
                    toolsizelist[0]+=1
                    toolsize(0)
            elif evnt.type==5 and evnt.button==2:
                colorfill=True
            elif evnt.type==6 and evnt.button==2:
                colorfill=False
            elif evnt.type==2 and evnt.key==304:
                altfunction=True
            elif evnt.type==3 and evnt.key==304:
                altfunction=False
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def cut():
    global mx
    global my
    clicked=False
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    screen.set_clip(Rect(0,0,980,588))
                    minx=min(startx,mx)
                    maxx=max(startx,mx)
                    miny=min(starty,my)
                    maxy=max(starty,my)
                    visiblescreenrefresh()
                    draw.aaline(screen,(255,255,255),(minx,miny),(maxx,miny))
                    draw.aaline(screen,(255,255,255),(maxx,miny),(maxx,maxy))
                    draw.aaline(screen,(255,255,255),(maxx,maxy),(minx,maxy))
                    draw.aaline(screen,(255,255,255),(minx,maxy),(minx,miny))
                    maxx+=1
                    minx-=1
                    maxy+=1
                    miny-=1
                    draw.aaline(screen,(0,0,0),(minx,miny),(maxx,miny))
                    draw.aaline(screen,(0,0,0),(maxx,miny),(maxx,maxy))
                    draw.aaline(screen,(0,0,0),(maxx,maxy),(minx,maxy))
                    draw.aaline(screen,(0,0,0),(minx,maxy),(minx,miny))
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                startx=mx
                starty=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                minx=min(startx,mx)
                maxx=max(startx,mx)
                miny=min(starty,my)
                maxy=max(starty,my)
                vw,vh=visiblecanvas.get_size()
                if maxx>vw:
                    maxx=vw-1
                if maxy>vh:
                    maxy=vh-1
                canvasload(visiblecanvas.subsurface(Rect(minx,miny,maxx-minx+1,maxy-miny+1)),0)
                trackaction()
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def ovaltool():
    global mx
    global my
    altfunction=False
    colorfill=False
    clicked=False
    toolsize(1)
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    screen.set_clip(Rect(0,0,980,588))
                    minx=min(startx,mx)
                    maxx=max(startx,mx)
                    miny=min(starty,my)
                    maxy=max(starty,my)
                    mindist=min((maxx-minx),(maxy-miny))+1
                    if altfunction==False:
                        if colorfill==False:
                            fillrad=int(mindist/2)
                            if toolsizelist[1]<fillrad:
                                fillrad=toolsizelist[1]
                            visiblescreenrefresh()
                            draw.ellipse(screen,colorqueue[0],Rect(minx,miny,maxx-minx+1,maxy-miny+1),fillrad)
                        else:
                            visiblescreenrefresh()
                            draw.ellipse(screen,colorqueue[0],Rect(minx,miny,maxx-minx+1,maxy-miny+1),0)
                    else:
                        if colorfill==False:
                            fillrad=int(mindist/2)
                            if toolsizelist[1]<fillrad:
                                fillrad=toolsizelist[1]
                            visiblescreenrefresh()
                            draw.ellipse(screen,colorqueue[0],Rect(minx,miny,mindist,mindist),fillrad)
                        else:
                            visiblescreenrefresh()
                            draw.ellipse(screen,colorqueue[0],Rect(minx,miny,mindist,mindist),0)
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                startx=mx
                starty=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==6 and evnt.button==1 and clicked:
                    clicked=False
                    minx=min(startx,mx)
                    maxx=max(startx,mx)
                    miny=min(starty,my)
                    maxy=max(starty,my)
                    mindist=min((maxx-minx),(maxy-miny))+1
                    if altfunction==False:
                        if colorfill==False:
                            fillrad=int(mindist/2)
                            if toolsizelist[1]<fillrad:
                                fillrad=toolsizelist[1]

                            draw.ellipse(visiblecanvas,colorqueue[0],Rect(minx,miny,maxx-minx+1,maxy-miny+1),fillrad)
                        else:

                            draw.ellipse(visiblecanvas,colorqueue[0],Rect(minx,miny,maxx-minx+1,maxy-miny+1),0)
                    else:
                        if colorfill==False:
                            fillrad=int(mindist/2)
                            if toolsizelist[1]<toolsize:
                                fillrad=toolsizelist[1]

                            draw.ellipse(visiblecanvas,colorqueue[0],Rect(minx,miny,mindist,mindist),fillrad)
                        else:

                            draw.ellipse(visiblecanvas,colorqueue[0],Rect(minx,miny,mindist,mindist),0)
                    visiblescreenrefresh()
                    trackaction()
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[1]>1:
                    toolsizelist[1]-=1
                    toolsize(1)
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[1]<295:
                    toolsizelist[1]+=1
                    toolsize(1)
            elif evnt.type==5 and evnt.button==2:
                colorfill=True
            elif evnt.type==6 and evnt.button==2:
                colorfill=False
            elif evnt.type==2 and evnt.key==304:
                altfunction=True
            elif evnt.type==3 and evnt.key==304:
                altfunction=False
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def polygon():
    global mx
    global my
    colorfill=False
    clicked=False
    polylist=[]
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    screen.set_clip(Rect(0,0,980,588))
                    if len(polylist)>1:
                        visiblescreenrefresh()
                        draw.aalines(screen,colorqueue[0],False,polylist)
                        draw.aaline(screen,colorqueue[0],polylist[-1],(mx,my))
                    else:
                        visiblescreenrefresh()
                        draw.aaline(screen,colorqueue[0],polylist[-1],(mx,my))
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==5 and evnt.button==1 and canvascheck() and clicked:
                polylist.append((mx,my))
                visiblescreenrefresh()
                draw.aalines(screen,colorqueue[0],False,polylist)
            elif evnt.type==5 and evnt.button==1 and canvascheck() and clicked==False:
                clicked=True
                polylist=[]
                polylist.append((mx,my))

            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==2 and evnt.key==13 and clicked:
                    clicked=False
                    if len(polylist)>1:
                        polylist.append((mx,my))
                        visiblescreenrefresh()
                        if colorfill==False:
                            draw.aalines(visiblecanvas,colorqueue[0],True,polylist)
                        else:
                            draw.polygon(visiblecanvas,colorqueue[0],polylist)
                        visiblescreenrefresh()
                        trackaction()
            elif evnt.type==5 and evnt.button==2:
                colorfill=True
            elif evnt.type==6 and evnt.button==2:
                colorfill=False
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def linetool():
    global mx
    global my
    toolsize(2)
    clicked=False
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    sidedist=min(abs(979-mx),abs(0-mx),abs(0-my),abs(587-my),abs(979-px),abs(0-px),abs(0-py),abs(587-py))-1
                    if toolsizelist[2]<sidedist*2:
                        sidedist=toolsizelist[2]
                    screen.set_clip(Rect(0,0,980,588))
                    visiblescreenrefresh()
                    draw.line(screen,colorqueue[0],(px,py),(mx,my),sidedist)
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                draw.line(visiblecanvas,colorqueue[0],(px,py),(mx,my),sidedist)
                visiblescreenrefresh()
                trackaction()
            elif evnt.type==5 and evnt.button==1 and canvascheck() and clicked==False:
                clicked=True
                px=mx
                py=my
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[2]>1:
                    toolsizelist[2]-=1
                    toolsize(2)
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[2]<588:
                    toolsizelist[2]+=1
                    toolsize(2)
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
################################################################################
###############################Basic Draw Tools#################################
################################################################################
def pencil():
    global mx
    global my
    clicked=False
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if clicked:
                    screen.set_clip(Rect(0,0,980,588))
                    draw.aaline(screen,colorqueue[0],(px,py),(mx,my))
                    screen.set_clip(Rect(0,0,1010,692))
                    pointlist.append((mx,my))
                    px=mx
                    py=my
                    screen.set_clip(Rect(0,0,1010,692))
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                draw.aalines(visiblecanvas,colorqueue[0],False,pointlist)
                visiblescreenrefresh()
                trackaction()
            elif evnt.type==5 and evnt.button==1 and canvascheck() and clicked==False:
                clicked=True
                pointlist=[]
                pointlist.append((mx,my))
                px=mx
                py=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def paintbrush():
    global mx
    global my
    toolsize(3)
    showrange=False
    clicked=False
    screencopy=screen.copy()
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if showrange:
                    screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                if clicked:
                    xdist=abs(px-mx)+1
                    ydist=abs(py-my)+1
                    screen.set_clip(Rect(0,0,980,588))
                    draw.circle(screen,colorqueue[0],(px,py),toolsizelist[3])
                    circlelist.append([(px,py),toolsizelist[3],colorqueue[0]])
                    if px<=mx:
                        left=True
                    else:
                        left=False
                    if py<=my:
                        up=True
                    else:
                        up=False

                    if xdist>=ydist:
                        if left:
                            if up:
                                for i in range(1,xdist):
                                    tempy=py+((i*1.0/xdist)*ydist)
                                    tempx=px+i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                            else:
                                for i in range(1,xdist):
                                    tempy=py-((i*1.0/xdist)*ydist)
                                    tempx=px+i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                        else:
                            if up:
                                for i in range(1,xdist):
                                    tempy=py+((i*1.0/xdist)*ydist)
                                    tempx=px-i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                            else:
                                for i in range(1,xdist):
                                    tempy=py-((i*1.0/xdist)*ydist)
                                    tempx=px-i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])

                    else:
                        if left:
                            if up:
                                for i in range(1,ydist):
                                    tempx=px+((i*1.0/ydist)*xdist)
                                    tempy=py+i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                            else:
                                for i in range(1,ydist):
                                    tempx=px+((i*1.0/ydist)*xdist)
                                    tempy=py-i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                        else:
                            if up:
                                for i in range(1,ydist):
                                    tempx=px-((i*1.0/ydist)*xdist)
                                    tempy=py+i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])

                            else:
                                for i in range(1,ydist):
                                    tempx=px-((i*1.0/ydist)*xdist)
                                    tempy=py-i
                                    draw.circle(screen,colorqueue[0],(tempx,tempy),toolsizelist[3])
                                    circlelist.append([(tempx+canvasx,tempy+canvasy),toolsizelist[3],colorqueue[0]])
                    screen.set_clip(Rect(0,0,1010,692))
                    px=mx
                    py=my
                if showrange:
                    screencopy=screen.copy()
                    rangedisplay(3)
                    screen.blit(mouselayer,(0,0))

            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                circlelist=[]
                px=mx
                py=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
                if showrange:
                    screencopy=screen.copy()
                    rangedisplay(3)
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                circlelist.append([(px,py),toolsizelist[3],colorqueue[0]])
                for curcir in circlelist:
                    draw.circle(canvas,curcir[2],curcir[0],curcir[1])
                trackaction()
                visiblescreenrefresh()
                if showrange:
                    screencopy=screen.copy()
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[3]>1:
                    toolsizelist[3]-=1
                    toolsize(3)
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(3)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[3]<586:
                    toolsizelist[3]+=1
                    toolsize(3)
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(3)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==2 and evnt.key==304:
                showrange=True
                screencopy=screen.copy()
                rangedisplay(3)
                screen.blit(mouselayer,(0,0))
            elif evnt.type==3 and evnt.key==304:
                showrange=False
                screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def eraser():
    global mx
    global my
    toolsize(4)
    showrange=False
    clicked=False
    screencopy=screen.copy()
    disttocent=toolsizelist[4]*2
    changecolor((255,255,255))
    #remember to change color back when exiting function
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if showrange:
                    screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                if clicked:
                    xdist=abs(px-mx)+1
                    ydist=abs(py-my)+1
                    screen.set_clip(Rect(0,0,980,588))
                    temprect=Rect(px-toolsizelist[4],py-toolsizelist[4],disttocent,disttocent)
                    screen.fill(colorqueue[0],temprect)
                    squarelist.append([temprect,colorqueue[0]])
                    if px<=mx:
                        left=True
                    else:
                        left=False
                    if py<=my:
                        up=True
                    else:
                        up=False

                    if xdist>=ydist:
                        if left:
                            if up:
                                for i in range(1,xdist):
                                    tempy=py+((i*1.0/xdist)*ydist)
                                    tempx=px+i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])

                            else:
                                for i in range(1,xdist):
                                    tempy=py-((i*1.0/xdist)*ydist)
                                    tempx=px+i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])
                        else:
                            if up:
                                for i in range(1,xdist):
                                    tempy=py+((i*1.0/xdist)*ydist)
                                    tempx=px-i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])
                            else:
                                for i in range(1,xdist):
                                    tempy=py-((i*1.0/xdist)*ydist)
                                    tempx=px-i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])

                    else:
                        if left:
                            if up:
                                for i in range(1,ydist):
                                    tempx=px+((i*1.0/ydist)*xdist)
                                    tempy=py+i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])
                            else:
                                for i in range(1,ydist):
                                    tempx=px+((i*1.0/ydist)*xdist)
                                    tempy=py-i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])
                        else:
                            if up:
                                for i in range(1,ydist):
                                    tempx=px-((i*1.0/ydist)*xdist)
                                    tempy=py+i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])

                            else:
                                for i in range(1,ydist):
                                    tempx=px-((i*1.0/ydist)*xdist)
                                    tempy=py-i
                                    temprect=Rect(tempx-toolsizelist[4],tempy-toolsizelist[4],disttocent,disttocent)
                                    screen.fill(colorqueue[0],temprect)
                                    squarelist.append([Rect(tempx-toolsizelist[4]+canvasx,tempy-toolsizelist[4]+canvasy,disttocent,disttocent),colorqueue[0]])
                    screen.set_clip(Rect(0,0,1010,692))
                    px=mx
                    py=my
                if showrange:
                    screencopy=screen.copy()
                    rangedisplay(4)
                    screen.blit(mouselayer,(0,0))

            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                squarelist=[]
                px=mx
                py=my
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
                if showrange:
                    screencopy=screen.copy()
                    rangedisplay(4)
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                temprect=Rect(px-toolsizelist[4]+canvasx,py-toolsizelist[4]+canvasy,disttocent,disttocent)
                squarelist.append([temprect,colorqueue[0]])
                for cursquare in squarelist:
                    canvas.fill(cursquare[1],cursquare[0])
                trackaction()
                visiblescreenrefresh()
                if showrange:
                    screencopy=screen.copy()
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[4]>1:
                    toolsizelist[4]-=1
                    toolsize(4)
                    disttocent=toolsizelist[4]*2
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(4)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[4]<586:
                    toolsizelist[4]+=1
                    toolsize(4)
                    disttocent=toolsizelist[4]*2
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(4)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==2 and evnt.key==304:
                showrange=True
                screencopy=screen.copy()
                rangedisplay(4)
                screen.blit(mouselayer,(0,0))
            elif evnt.type==3 and evnt.key==304:
                showrange=False
                screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
            elif evnt.type==2 and evnt.key>48 and evnt.key<58:
                changecolor(colorqueue[evnt.key-48])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def spray():
    global mx
    global my
    showrange=False
    clicked=False
    toolsize(6)
    disttocent=toolsizelist[6]*2
    screencopy=screen.copy()
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
                if showrange:
                    screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                    rangedisplay(6)
                    screen.blit(mouselayer,(0,0))
                    #do stuff originally

            elif evnt.type==5 and evnt.button==1 and canvascheck():
                clicked=True
                tempdraw=Surface((x,y))
                transcolor=notincolor()
                tempdraw.fill(transcolor)
                tempdraw.set_colorkey(transcolor)
            elif evnt.type==5 and evnt.button==3:
                clicked=False
                visiblescreenrefresh()
                if showrange:
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==6 and evnt.button==1 and clicked:
                clicked=False
                canvas.blit(tempdraw,(0,0))
                trackaction()
                visiblescreenrefresh()
                if showrange:
                    screencopy=screen.copy()
                    screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[6]>1:
                    toolsizelist[6]-=1
                    toolsize(6)
                    disttocent=toolsizelist[6]*2
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(6)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[6]<586:
                    toolsizelist[6]+=1
                    toolsize(6)
                    disttocent=toolsizelist[6]*2
                    if showrange:
                        screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
                        rangedisplay(6)
                        screen.blit(mouselayer,(0,0))
            elif evnt.type==2 and evnt.key==304:
                showrange=True
                screencopy=screen.copy()
                rangedisplay(6)
                screen.blit(mouselayer,(0,0))
            elif evnt.type==3 and evnt.key==304:
                showrange=False
                screen.blit(screencopy.subsurface(Rect(0,0,980,588)),(0,0))
            elif evnt.type==2 and evnt.key>49 and evnt.key<58:
                changecolor(colorqueue[evnt.key-49])
            elif evnt.type==QUIT:
                emquit()
            if clicked==False:
                display.flip()
        if clicked:
            if largex==False and largey==False:
                for i in range(int(ceil(toolsizelist[6]/10.0))**3):
                    sh=randint(0,disttocent)
                    sw=randint(0,disttocent)
                    if (abs(sh-toolsizelist[6]+1)**2+abs(sw-toolsizelist[6]+1)**2)<=(toolsizelist[6])**2:
                        tempdraw.set_at((canvasx+mx-toolsizelist[6]+sw,canvasy+my-toolsizelist[6]+sh),colorqueue[0])
                        screen.blit(tempdraw.subsurface(Rect(canvasx,canvasy,x,y)),(0,0))
            elif largex and largey==False:
                for i in range(int(ceil(toolsizelist[6]/10.0))**3):
                    sh=randint(0,disttocent)
                    sw=randint(0,disttocent)
                    if (abs(sh-toolsizelist[6]+1)**2+abs(sw-toolsizelist[6]+1)**2)<=(toolsizelist[6])**2:
                        tempdraw.set_at((canvasx+mx-toolsizelist[6]+sw,canvasy+my-toolsizelist[6]+sh),colorqueue[0])
                        screen.blit(tempdraw.subsurface(Rect(canvasx,canvasy,980,y)),(0,0))
            elif largex==False and largey:
                for i in range(int(ceil(toolsizelist[6]/10.0))**3):
                    sh=randint(0,disttocent)
                    sw=randint(0,disttocent)
                    if (abs(sh-toolsizelist[6]+1)**2+abs(sw-toolsizelist[6]+1)**2)<=(toolsizelist[6])**2:
                        tempdraw.set_at((canvasx+mx-toolsizelist[6]+sw,canvasy+my-toolsizelist[6]+sh),colorqueue[0])
                        screen.blit(tempdraw.subsurface(Rect(canvasx,canvasy,x,588)),(0,0))
            else:
                for i in range(int(ceil(toolsizelist[6]/10.0))**3):
                    sh=randint(0,disttocent)
                    sw=randint(0,disttocent)
                    if (abs(sh-toolsizelist[6]+1)**2+abs(sw-toolsizelist[6]+1)**2)<=(toolsizelist[6])**2:
                        tempdraw.set_at((canvasx+mx-toolsizelist[6]+sw,canvasy+my-toolsizelist[6]+sh),colorqueue[0])
                        screen.blit(tempdraw.subsurface(Rect(canvasx,canvasy,980,588)),(0,0))
            display.flip()
################################################################################
###############################Transform functions##############################
################################################################################
def left90():
    canvasload(transform.rotate(canvas,270),0)
    trackaction()
def freerotate():
    counter=0
    while True:
        for evnt in event.get():
            if evnt.type==5:
                if counter==360:
                    counter=0
                elif counter==-360:
                    counter=0
                if evnt.button==4:
                    counter+=1
                    canvasload(transform.rotate(temporarycanvas,counter),1)
                elif evnt.button==5:
                    counter-=1
                    canvasload(transform.rotate(temporarycanvas,counter),1)
            elif evnt.type==6 and evnt.button==1:
                trackaction()
                return normalstate
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def sideflip():
    reverse=PixelArray(canvas)
    newreverse=reverse[::-1,:]
    canvasload(newreverse.make_surface(),0)
    del newreverse
    del reverse
    trackaction()
def verticleflip():
    reverse=PixelArray(canvas)
    newreverse=reverse[:,::-1]
    canvasload(newreverse.make_surface(),0)
    del newreverse
    del reverse
    trackaction()
################################################################################
#################################File functions#################################
################################################################################
def picopen():#opens a picture
    global x
    global y
    tempimg=askopenfilename(defaultextension=".jpg",filetypes=[("Bitmap","*.bmp"),("PNG","*.png"),("JPEG","*.jpg")],parent=useless)
    if tempimg=="":
        return
    loadimage=image.load(tempimg)
    canvasload(loadimage,0)
    trackaction()
ifsave=False
def backupsave():#saving a picture in case of accident close
    image.save(canvas,strftime("%Y_%m_%d_%A_%H_%M_%S",localtime())+".jpg")
saveaddr=" "
def choosesave():
    global saveaddr
    saveaddr=asksaveasfilename(defaultextension=".png",filetypes=[("Bitmap","*.bmp"),("JPEG","*.jpg"),("PNG","*.png")],parent=useless)
    image.save(canvas,saveaddr)
def qsave():
    if saveaddr==" ":
        return choosesave()
    image.save(canvas,saveaddr)
################################################################################
############################Stamp/Paintball function############################
################################################################################
lpaintlist=[]
mpaintlist=[]
spaintlist=[]
for i in range(1,10):
    lpaintlist.append(image.load("splatl"+str(i)+".jpg"))
    (lpaintlist[i-1]).set_colorkey((255,255,255))
for i in range(1,4):
    mpaintlist.append(image.load("splatm"+str(i)+".jpg"))
    (mpaintlist[i-1]).set_colorkey((255,255,255))
for i in range(1,6):
    spaintlist.append(image.load("splats"+str(i)+".jpg"))
    (spaintlist[i-1]).set_colorkey((255,255,255))
def paintball():
    global mx
    global my
    showrange=False
    clicked=False
    toolsize(5)
    screencopy=screen.copy()
    disttocent=toolsizelist[4]*2
    changecolor((255,255,255))
    #remember to change color back when exiting function
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                if toolsizelist[5]==1:
                    temppaint=transform.rotate(spaintlist[randint(0,4)],randint(0,359))
                    visiblecanvas.blit(temppaint,(mx-(temppaint.get_width()/2),my-(temppaint.get_height()/2)))
                    visiblescreenrefresh()
                    trackaction()
                elif toolsizelist[5]==2:
                    temppaint=transform.rotate(mpaintlist[randint(0,2)],randint(0,359))
                    visiblecanvas.blit(temppaint,(mx-(temppaint.get_width()/2),my-(temppaint.get_height()/2)))
                    visiblescreenrefresh()
                    trackaction()
                elif toolsizelist[5]==3:
                    temppaint=transform.rotate(lpaintlist[randint(0,8)],randint(0,359))
                    visiblecanvas.blit(temppaint,(mx-(temppaint.get_width()/2),my-(temppaint.get_height()/2)))
                    visiblescreenrefresh()
                    trackaction()
            elif evnt.type==5 and evnt.button==4:
                if toolsizelist[5]>1:
                    toolsizelist[5]-=1
                    toolsize(5)

            elif evnt.type==5 and evnt.button==5:
                if toolsizelist[5]<3:
                    toolsizelist[5]+=1
                    toolsize(5)

            elif evnt.type==2 and evnt.key>48 and evnt.key<58:
                changecolor(colorqueue[evnt.key-48])
            elif evnt.type==QUIT:
                emquit()
            display.flip()
headlist=[]

################################################################################
#################################Bucket Tool#####################################
################################################################################
def bucket():
    global mx
    global my
    #remember to change color back when exiting function
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==5 and evnt.button==1 and canvascheck():
                pxcanvas=PixelArray(canvas)
                b=Surface((2,2))
                pixcolor=pxcanvas[mx][my]
                b.set_at((1,1),(colorqueue[0]))
                c=PixelArray(b)
                fillcolor=canvas.unmap_rgb(c[1][1])
                route=[[True]*(y+2) for z in xrange(x+2)]
                route[mx+1][my+1]=False
                for i in range(x+2):
                    route[i][0]=False
                    route[i][y+1]=False
                route[0]=[False]*(y+2)
                route[x+1]=route[0]
                fillqueue=deque()
                fillqueue.appendleft([mx,my])
                while len(fillqueue)>0:
                    currentpixel=fillqueue.pop()
                    if route[currentpixel[0]+2][currentpixel[1]+1] and pxcanvas[currentpixel[0]+1][currentpixel[1]]==pixcolor:
                        fillqueue.appendleft([currentpixel[0]+1,currentpixel[1]])
                        route[currentpixel[0]+2][currentpixel[1]+1]=False
                    if route[currentpixel[0]][currentpixel[1]+1] and pxcanvas[currentpixel[0]-1][currentpixel[1]]==pixcolor:
                        fillqueue.appendleft([currentpixel[0]-1,currentpixel[1]])
                        route[currentpixel[0]][currentpixel[1]+1]=False
                    if route[currentpixel[0]+1][currentpixel[1]+2] and pxcanvas[currentpixel[0]][currentpixel[1]+1]==pixcolor:
                        fillqueue.appendleft([currentpixel[0],currentpixel[1]+1])
                        route[currentpixel[0]+1][currentpixel[1]+2]=False
                    if route[currentpixel[0]+1][currentpixel[1]] and pxcanvas[currentpixel[0]][currentpixel[1]-1]==pixcolor:
                        fillqueue.appendleft([currentpixel[0],currentpixel[1]-1])
                        route[currentpixel[0]+1][currentpixel[1]]=False
                    pxcanvas[currentpixel[0]][currentpixel[1]]=fillcolor
                del pxcanvas
                visiblescreenrefresh()
                trackaction()



            elif evnt.type==2 and evnt.key>48 and evnt.key<58:
                changecolor(colorqueue[evnt.key-48])
            elif evnt.type==QUIT:
                emquit()
            display.flip()



################################################################################
##################################Static Ruler##################################
################################################################################
scale=Surface((98,15))#scale to be drawn on the rulers
scale.fill((255,255,255))
draw.aaline(scale,(0,0,0),(46,3),(46,14),True)
draw.aaline(scale,(0,0,0),(23,14),(23,8),True)
draw.aaline(scale,(0,0,0),(70,14),(70,8),True)#making the scales
rulerx=Surface((980,15))#ruler on x axis
rulery=Surface((588,15))#ruler on y axis
def rulerstatx():#a function for updating the static ruler on x axis
    rulerx.fill((255,255,255))
    for i in range(0,10):
        rulerx.blit(scale,(i*98,0))#puts the scales on the ruler
    rulerx.blit(font12.render("0",True,(0,0,0),(255,255,255)),(0,0))
    if largex:#This ruler is for canvas wider than 980 pixels
        temp=font12.render(("%5d")%(x-1),True,(0,0,0))#dynamically creates the increments
        rulerx.blit(temp,(980-temp.get_width(),0))#based on the width
        for i in range(1,10):#10 increments in total
            temp=font12.render("%5d"%(i*x/10.0),True,(0,0,0),(255,255,255))
            rulerx.blit(temp,(((98*i)-(temp.get_width()/2)),0))
    else:#Default ruler for canvas width less or equal to 980 pixels
        temp=font12.render("979",True,(0,0,0))
        rulerx.blit(temp,(980-temp.get_width(),0))
        for i in range(1,10):
            temp=font12.render("%5d"%(i*98),True,(0,0,0))
            rulerx.blit(temp,(((98*i)-(temp.get_width()/2)),0))
    screen.blit(rulerx,(0,603))
def rulerstaty():#a function for updating the static ruler on y axis like the previous function
    rulery.fill((255,255,255))
    for i in range(0,6):
        rulery.blit(scale,(i*98,0))
    rulery.blit(font12.render("0",True,(0,0,0),(255,255,255)),(0,0))
    if largey:#This ruler is for canvas taller than 588 pixels
        temp=font12.render(("%5d")%(y-1),True,(0,0,0))
        rulery.blit(temp,(588-temp.get_width(),0))
        for i in range(0,6):
            temp=font12.render("%5d"%(i*y/6),True,(0,0,0),(255,255,255))
            rulery.blit(temp,(((98*i)-(temp.get_width()/2)),0))
    else:#Default ruler for canvas height less or equal to 588 pixels
        temp=font12.render("587",True,(0,0,0))
        rulery.blit(temp,(588-temp.get_width(),0))
        for i in range(1,6):
            temp=font12.render("%5d"%(i*98),True,(0,0,0))
            rulery.blit(temp,(((98*i)-(temp.get_width()/2)),0))
    screen.blit(transform.rotate(rulery,270),(995,0))#turns the ruler before putting it on screen
################################################################################
##################################Slider########################################
################################################################################
sliderx=Surface((980,15))
slidery=Surface((588,15))
sliderxwidth=980
sliderywidth=980
sliderbasex=Surface((980,15))
sliderbasey=Surface((588,15))
sliderxpos=0
sliderypos=0
def slidermakex():#a function to resize slider x.
    global sliderx
    global sliderxwidth
    if largex:
        sliderxwidth=int(ceil(980.0/x*980))
        sliderx=Surface((sliderxwidth,15))
        sliderx.fill((255,0,0))
    else:
        slidierxwidth=980
        sliderx=Surface((sliderxwidth,15))
        sliderx.fill((255,0,0))
def slidermakey():#a function to resize slider x.
    global slidery
    global sliderywidth
    if largey:
        sliderywidth=int(ceil(588.0/y*588))
        slidery=Surface((sliderywidth,15))
        slidery.fill((255,0,0))
    else:
        sliderywidth=588
        slidery=Surface((sliderywidth,15))
        slidery.fill((255,0,0))
def dynamicrulerx():#makes the dynamic ruler on the x axis scroll bar
    temp=font12.render("%-5d"%canvasx,True,(255,255,255))
    sliderbasex.blit(temp,(0,0))
    temp=font12.render("%5d"%(canvasx+979),True,(255,255,255))
    sliderbasex.blit(temp,(980-temp.get_width(),0))
    for i in range(1,10):
        temp=font12.render("%5d"%(canvasx+(i*98)),True,(255,255,255))
        sliderbasex.blit(temp,((i*98)-(temp.get_width()/2),0))
def dynamicrulery():#makes the dynamic ruler on the y axis scroll bar
    temp=font12.render("%-5d"%canvasy,True,(255,255,255))
    sliderbasey.blit(temp,(0,0))
    temp=font12.render("%5d"%(canvasy+587),True,(255,255,255))
    sliderbasey.blit(temp,(588-temp.get_width(),0))
    for i in range(1,6):
        temp=font12.render("%5d"%(canvasy+(i*98)),True,(255,255,255))
        sliderbasey.blit(temp,((i*98)-(temp.get_width()/2),0))
def sliderbasemakex():#makes the whole x axis slider
    global sliderxpos
    sliderbasex.fill((0,0,255))
    if largex:
        sliderbasex.blit(sliderx,(sliderxpos,0))
        dynamicrulerx()
    else:
        sliderxpos=0
        sliderbasex.blit(sliderx,(0,0))
    screen.blit(sliderbasex,(0,588))
def sliderbasemakey():#makes the whole y axis slider
    global sliderypos
    sliderbasey.fill((0,0,255))
    if largey:
        sliderbasey.blit(slidery,(sliderypos,0))
        dynamicrulery()
    else:
        sliderypos=0
        sliderbasey.blit(slidery,(0,0))
    screen.blit(transform.rotate(sliderbasey,270),(980,0))
################################################################################
####################################Canvas######################################
################################################################################
screenfill=Rect(0,0,980,588)
def canvasload(newcanvas,location):
    global canvas
    global x
    global y
    global gridx
    global gridy
    global canvasx
    global canvasy
    canvas=newcanvas
    x,y=canvas.get_size()
    canvascheckx()
    canvaschecky()
    if location==2:
        canvasx=x-980
        canvasy=y-588
    elif location==1:
        if canvasx+980>x:
            canvasx=x-980
        if canvasy+588>y:
            canvasy=y-588
    if canvasx<0:
        canvasx=0
    if canvasy<0:
        canvasy=0
    elif location==0:
        canvasx=0
        canvays=0
    gridx=canvasx%10
    gridy=canvasy%10
    rulerstatx()
    rulerstaty()
    slidermakex()
    slidermakey()
    sliderbasemakey()
    sliderbasemakex()
    visiblescreenrefresh()
def visiblescreenrefresh():
    global visiblecanvas
    screen.fill((128,128,128),screenfill)
    if largex==False and largey==False:
        visiblecanvas=canvas
        screen.blit(visiblecanvas,(0,0))
        if gridshow:
            screen.blit(grid.subsurface(Rect(0,0,x,y)),(0,0))
    elif largey==True and largex==False:
        visiblecanvas=canvas.subsurface(Rect(0,canvasy,x,588))
        screen.blit(visiblecanvas,(0,0))
        if gridshow:
            screen.blit(grid.subsurface(Rect(0,gridy,x,588)),(0,0))
    elif largex==True and largey==False:
        visiblecanvas=canvas.subsurface(Rect(canvasx,0,980,y))
        screen.blit(visiblecanvas,(0,0))
        if gridshow:
            screen.blit(grid.subsurface(Rect(gridx,0,980,y)),(0,0))
    else:
        visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
        screen.blit(visiblecanvas,(0,0))
        if gridshow:
            screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))

################################################################################
###################################Scrolling####################################
################################################################################
def scrollstatex():
    global sliderxpos
    global visiblecanvas
    global canvasx
    global gridx
    global mx
    lagedgex=False
    sliderdifferencex=mx-sliderxpos
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                if mx-sliderdifferencex>-1 and mx-sliderdifferencex+sliderxwidth<980:
                    lagedgex=False
                    sliderxpos=mx-sliderdifferencex
                    sliderbasemakex()
                    canvasx=int(((x-980)*sliderxpos*1.0)/(980-sliderxwidth))
                    gridx=canvasx%10
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                elif lagedgex==False and mx-sliderdifferencex<0:
                    sliderxpos=0
                    canvasx=0
                    gridx=0
                    sliderbasemakex()
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                    lagedgex=True
                elif lagedgex==False and mx-sliderdifferencex+sliderxwidth>979:
                    sliderxpos=980-sliderxwidth
                    canvasx=x-980
                    gridx=canvasx%10
                    sliderbasemakex()
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                    lagedgex=True
                updatecord()
            elif evnt.type==6 and evnt.button==1:
                return previousstate
            elif evnt.type==QUIT:
                 return emquit
            display.flip()
def scrollstatey():
    global sliderypos
    global canvasy
    global gridy
    global my
    global visiblecanvas
    lagedgey=False
    sliderdifferencey=my-sliderypos
    while True:
        for evnt in event.get():
            if evnt.type==4:
                mx,my=evnt.pos
                if my-sliderdifferencey>-1 and my-sliderdifferencey+sliderywidth<588:
                    lagedgey=False
                    sliderypos=my-sliderdifferencey
                    sliderbasemakey()
                    canvasy=int(((y-588)*sliderypos*1.0)/(588-sliderywidth))
                    gridx=canvasx%10
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                elif lagedgey==False and my-sliderdifferencey<0:
                    sliderypos=0
                    canvasy=0
                    gridx=0
                    sliderbasemakey()
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                    lagedgey=True
                elif lagedgey==False and my-sliderdifferencey+sliderywidth>587:
                    sliderypos=588-sliderywidth
                    canvasy=y-588
                    gridx=canvasx%10
                    sliderbasemakey()
                    visiblecanvas=canvas.subsurface(Rect(canvasx,canvasy,980,588))
                    screen.blit(visiblecanvas,(0,0))
                    if gridshow:
                        screen.blit(grid.subsurface(Rect(gridx,gridy,980,588)),(0,0))
                    lagedgey=True
                updatecord()
            elif evnt.type==6 and evnt.button==1:
                return previousstate
            elif evnt.type==QUIT:
                 emquit()
            display.flip()
################################################################################
###############################Canvas Resize####################################
################################################################################
def canvaschangeheight():
    while True:
        for evnt in event.get():
            if evnt.type==5:
                if evnt.button==4:
                    if y>1:
                        newsurface=Surface((x,y-1))
                        newsurface.blit(canvas,(0,0))
                        canvasload(newsurface,2)
                elif evnt.button==5:
                    newsurface=Surface((x,y+1))
                    newsurface.fill((255,255,255))
                    newsurface.blit(canvas,(0,0))
                    canvasload(newsurface,2)
            elif evnt.type==6 and evnt.button==1:
                trackaction()
                return previousstate
            elif evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==QUIT:
                emquit()
            display.flip()
def canvaschangewidth():
    while True:
        for evnt in event.get():
            if evnt.type==5:
                if evnt.button==4:
                    if x>1:
                        newsurface=Surface((x-1,y))
                        newsurface.blit(canvas,(0,0))
                        canvasload(newsurface,2)
                elif evnt.button==5:
                    newsurface=Surface((x+1,y))
                    newsurface.fill((255,255,255))
                    newsurface.blit(canvas,(0,0))
                    canvasload(newsurface,2)
            elif evnt.type==6 and evnt.button==1:
                trackaction()
                return previousstate
            elif evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            elif evnt.type==QUIT:
                emquit()
            display.flip()
################################################################################
###############################Normal State#####################################
################################################################################
def normalstate():
    global mx
    global my
    while True:
        for evnt in event.get():
            print evnt
            if mx>sliderxpos and mx < sliderxpos+sliderxwidth and my> 588 and my<603 and largex:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(19)
                elif evnt.type==5 and evnt.button==1:
                    return scrollstatex
            elif my>sliderypos and my <sliderypos+sliderywidth and mx >980 and mx <995 and largey:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(19)
                elif evnt.type==5 and evnt.button==1:
                    return scrollstatey
            elif mx>980 and mx<1010 and my>588 and my<606:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(19)
                elif evnt.type==5 and evnt.button==1:
                    return canvaschangeheight
            elif mx>980 and mx<1010 and my>606 and my<620:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(19)
                elif evnt.type==5 and evnt.button==1:
                    return canvaschangewidth
            elif mx>5 and mx<55 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(19)
                elif evnt.type==5 and evnt.button==1:
                    return paintbrush
            elif mx>65 and mx<115 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(12)
                elif evnt.type==5 and evnt.button==1:
                    return colorchooser
            elif mx>125 and mx<175 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(6)
                elif evnt.type==5 and evnt.button==1:
                    return spray
            elif mx>185 and mx<235 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(5)
                elif evnt.type==5 and evnt.button==1:
                    return paintball
            elif mx>245 and mx<295 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(7)
                elif evnt.type==5 and evnt.button==1:
                    return stamp
            elif mx>305 and mx<355 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(2)
                elif evnt.type==5 and evnt.button==1:
                    return pencil
            elif mx>365 and mx<415 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(11)
                elif evnt.type==5 and evnt.button==1:
                    return bucket
            elif mx>425 and mx<475 and my>623 and my<673:
                if evnt.type==4:
                    mx,my=evnt.pos
                    updatecord()
                    toolinfo(11)
                elif evnt.type==5 and evnt.button==1:
                    cleaner()
            """elif evnt.type==2:
                if evnt.mod==64:
                    if evnt.key==115:
                        qsave()
                    elif evnt.key==122:
                        undo()
                    elif evnt.key==121:
                        redo()
                elif evnt.key>48 and evnt.key<58:
                    changecolor(colorqueue[evnt.key-48])"""
            if evnt.type==QUIT:
                emquit()
            if evnt.type==4:
                mx,my=evnt.pos
                updatecord()
            display.flip()
################################################################################
def Q():
    return
startsurface=Surface((980,588))
startsurface.fill((255,255,255))
temporarycanvas=startsurface
picopen()
temporarycanvas=canvas
nextstate=normalstate
currentstate=normalstate
display.flip()
bucket()
