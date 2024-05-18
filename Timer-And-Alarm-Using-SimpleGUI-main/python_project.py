import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import datetime

#global
mode = 0
# ---- for timer------------
timer_hour = 0
timer_minutes = 0
timer_seconds = 0
time_for_timer = 0
timer_on_off = False
# ---------for alarm-----------
current_time = ''
alarm_hour = 0
alarm_minutes = 0
alarm_seconds = 0
am_pm = 'AM'
# ------------for alarm and timer-------------------
sound = simplegui.load_sound('http://commondatastorage.googleapis.com/codeskulptor-assets/Evillaugh.ogg')
p_sound = False
# -------- for stopwatch --------------
stopwatch_hour = 00
stopwatch_minutes = 00
stopwatch_seconds = 00
stopwatch_miliseconds = 00
stopwatch_time = "00 : 00 : 00 : 00"
stopwatch_pause_resume = 'Pause'
# helper function

# classes


# event handler
# -----------------------------------------TIMER------------------------------------------------------
def mouse_handler_for_timer(pos):
    global timer_hour,timer_minutes,timer_seconds,timer_on_off
    clicked_pos = list(pos)
# decrement timer
    if clicked_pos[0]>66 and clicked_pos[0]<168:
        if clicked_pos[1]>49 and clicked_pos[1]<121:
            if timer_hour==0:
                timer_hour=12
            else:
                timer_hour-=1
    if clicked_pos[0]>200 and clicked_pos[0]<302:
        if clicked_pos[1]>49 and clicked_pos[1]<121:
            if timer_minutes==0:
                timer_minutes=59
            else:
                timer_minutes-=1
    if clicked_pos[0]>334 and clicked_pos[0]<436:
        if clicked_pos[1]>49 and clicked_pos[1]<121:
            if timer_seconds==0:
                timer_seconds=59
            else:
                timer_seconds-=1
                
# increment the timer
    if clicked_pos[0]>66 and clicked_pos[0]<168:
        if clicked_pos[1]>219 and clicked_pos[1]<291:
            if timer_hour==12:
                timer_hour=0
            else:
                timer_hour+=1
    if clicked_pos[0]>200 and clicked_pos[0]<302:
        if clicked_pos[1]>219 and clicked_pos[1]<291:
            if timer_minutes==59:
                timer_minutes=0
            else:
                timer_minutes+=1
    if clicked_pos[0]>334 and clicked_pos[0]<436:
        if clicked_pos[1]>219 and clicked_pos[1]<291:
            if timer_seconds==59:
                timer_seconds=0
            else:
                timer_seconds+=1
    if clicked_pos[0]>200 and clicked_pos[0]<312: #start timer
        if clicked_pos[1]>399 and clicked_pos[1]<451:
            start_timer()
            timer_on_off = True
    if clicked_pos[0]>109 and clicked_pos[0]<231: #cancle timer
        if clicked_pos[1]>399 and clicked_pos[1]<451:
            stop_timer()
            timer_on_off = False
            timer_mode()
    if clicked_pos[0]>279 and clicked_pos[0]<391: #pause timer
        if clicked_pos[1]>399 and clicked_pos[1]<451:
            timer_on_off = True
            if timer.is_running():
                stop_timer()
            else:
                start_timer()
            
def timer_control():
    global timer_hour,timer_minutes,timer_seconds
    if timer_seconds==0:
        if timer_minutes == 0:
            if timer_hour!=0:
                timer_hour-=1
                timer_minutes = 59
                timer_seconds = 59
        else:
            timer_minutes -= 1
            timer_seconds=59
    else:
        timer_seconds -= 1
    if timer_hour == 0 and timer_minutes == 0 and timer_seconds == 0:
        stop_timer()
        play_sound()
def start_timer():
    global p_sound 
    p_sound = False
    timer.start()
def pause_resume_timer():
    if timer.is_running():
        stop_timer()
    else:
        start_timer()
def stop_timer():
    timer.stop()
def play_sound():
    global p_sound 
    p_sound = not p_sound
    sound.play()
    timer_mode()
def timer_mode():
    global mode,stopwatch_hour,stopwatch_minutes,stopwatch_seconds,stopwatch_miliseconds,stopwatch_time,stopwatch_pause_resume,timer_stopwatch_stopwatch_hour,timer_minutes,timer_seconds,p_sound,timer_on_off
    timer_on_off = False
    mode = 1
    p_sound = False
    stopwatch_hour = 00
    stopwatch_minutes = 00
    stopwatch_seconds = 00
    stopwatch_miliseconds = 00
    stopwatch_time = "00 : 00 : 00 : 00"
    stopwatch_pause_resume = 'Pause'
    frame.set_mouseclick_handler(mouse_handler_for_timer)
    timer_hour = 0
    timer_minutes = 0
    timer_seconds = 0
    time_for_timer = 0
# --------------------------------ALARM CLOCK---------------------------------------------------------------
def alarm_mode():
    global mode,current_time
    mode = 2
    current_time = datetime.datetime.now()
# -----------------------------------------------------STOPWATCH--------------------------------------------
def stopwatch_mode():
    global mode,timer_hour,timer_minutes,timer_seconds
    timer_hour = 0
    timer_minutes = 0
    timer_seconds = 0
    time_for_timer = 0
    mode = 3
    frame.set_mouseclick_handler(mouse_handler_for_stopwatch)
def mouse_handler_for_stopwatch(pos): # to check the mouse pointer and performe the task
    clicked_pos = list(pos)
    if clicked_pos[0]>49 and clicked_pos[0]<121:
        if clicked_pos[1]>429 and clicked_pos[1]<471:
            start_stopwatch_time()
    if clicked_pos[0]>149 and clicked_pos[0]<221:
        if clicked_pos[1]>429 and clicked_pos[1]<471:
            stop_stopwatch_time()
    if clicked_pos[0]>249 and clicked_pos[0]<356:
        if clicked_pos[1]>429 and clicked_pos[1]<471:
            pause_stopwatch_time()
    if clicked_pos[0]>389 and clicked_pos[0]<461:
        if clicked_pos[1]>429 and clicked_pos[1]<471:
            reset_stopwatch_time()
def start_stopwatch_time(): #to start the stopwatch and the stopwatch
    stopwatch.start()
def stop_stopwatch_time(): # to stop the stopwatch and the stopwatch
    stopwatch.stop()
def stopwatch_control(): # to count the time and upadate it
    global stopwatch_hour,stopwatch_minutes,stopwatch_seconds,stopwatch_miliseconds,stopwatch_time
    if stopwatch_miliseconds ==10:
        stopwatch_seconds+=1
        stopwatch_miliseconds=0
    if stopwatch_seconds ==60:
        stopwatch_minutes+=1
        stopwatch_seconds=0
    if stopwatch_minutes == 60:
        stopwatch_hours +=1
        stopwatch_minutes=0
    
    stopwatch_miliseconds+=1
    if stopwatch_hour<10:
        stopwatch_time="0"+str(stopwatch_hour)+" : "
    else:
        stopwatch_time=str(stopwatch_hour) + " : "
    if stopwatch_minutes<10:
        stopwatch_time+="0"+str(stopwatch_minutes)+" : "
    else:
        stopwatch_time+=(str(stopwatch_minutes))+" : "
    if stopwatch_seconds<10:
        stopwatch_time+="0"+str(stopwatch_seconds) + ' : '
    else:
        stopwatch_time+=str(stopwatch_seconds) + ' : '
    if stopwatch_miliseconds<10:
        stopwatch_time+="0" + str(stopwatch_miliseconds)
    else:
        stopwatch_time+=str(stopwatch_miliseconds)
    # stopwatch_time = str(stopwatch_hour) + ' : ' + str(stopwatch_minutes) + ' : ' + str(stopwatch_seconds)
    # print(stopwatch_time)
def pause_stopwatch_time(): #to pause the time 
    global stopwatch_pause_resume
    if stopwatch.is_running(): #if stopwatch is running than stop it and visa versa
        stop_stopwatch_time()
        stopwatch_pause_resume="Resume"
    else:
        start_stopwatch_time()
        stopwatch_pause_resume="Pause"
def reset_stopwatch_time(): #to reset the stopwatch
    global stopwatch_hour,stopwatch_miliseconds,stopwatch_minutes,stopwatch_seconds,stopwatch_time
    stopwatch_hour = stopwatch_minutes = stopwatch_seconds = stopwatch_miliseconds = 00
    stopwatch_time = "00 : 00 : 00 : 00"
# ------------------------------------DRAW CANVAS----------------------------------------------------
def draw(canvas):
# to display timer
    if mode==1:
        canvas.draw_polyline([(117,55),(77,110),(157,110),(117,55)],5,'white')
        canvas.draw_polyline([(251,55),(211,110),(291,110),(251,55)],5,'white')
        canvas.draw_polyline([(385,55),(345,110),(425,110),(385,55)],5,'white')
        canvas.draw_polygon([(67,50),(167,50),(167,120),(67,120)],5,'red')
        canvas.draw_polygon([(201,50),(301,50),(301,120),(201,120)],5,'red')
        canvas.draw_polygon([(335,50),(435,50),(435,120),(335,120)],5,'red')
        if timer_hour<10:
            canvas.draw_text('0'+str(timer_hour),(70,200),100,'pink')
        else:
            canvas.draw_text(str(timer_hour),(70,200),100,'pink')
        if timer_minutes<10:
            canvas.draw_text('0'+str(timer_minutes),(205,200),100,'pink')
        else:
            canvas.draw_text(str(timer_minutes),(205,200),100,'pink')
        if timer_seconds<10:
            canvas.draw_text('0'+str(timer_seconds),(340,200),100,'pink')
        else:
            canvas.draw_text(str(timer_seconds),(340,200),100,'pink')
        canvas.draw_polyline([(77,228),(157,228),(117,285),(77,228)],5,'white')
        canvas.draw_polyline([(211,228),(291,228),(251,285),(211,228)],5,'white')
        canvas.draw_polyline([(345,228),(425,228),(385,285),(345,228)],5,'white')
        canvas.draw_polygon([(67,220),(167,220),(167,290),(67,290)],5,'red')
        canvas.draw_polygon([(201,220),(301,220),(301,290),(201,290)],5,'red')
        canvas.draw_polygon([(335,220),(435,220),(435,290),(335,290)],5,'red')
        if timer_on_off:
            canvas.draw_polygon([(110,400),(230,400),(230,450),(110,450)],5,'red')
            canvas.draw_text('Cancle',(117,438),38,'white') #cancle timer
            canvas.draw_polygon([(280,400),(390,400),(390,450),(280,450)],5,'red')
            canvas.draw_text('Pause',(287,438),40,'white') #pause timer
        else:
            canvas.draw_polygon([(201,400),(311,400),(311,450),(201,450)],5,'red')
            canvas.draw_text('Start',(207,438),50,'white') #start timer
# to display alarm clock
    if mode==2:
        canvas.draw_polyline([(117,55),(77,110),(157,110),(117,55)],5,'white')
        canvas.draw_polyline([(251,55),(211,110),(291,110),(251,55)],5,'white')
        canvas.draw_polyline([(385,55),(345,110),(425,110),(385,55)],5,'white')
        canvas.draw_polygon([(67,50),(167,50),(167,120),(67,120)],5,'red')
        canvas.draw_polygon([(201,50),(301,50),(301,120),(201,120)],5,'red')
        canvas.draw_polygon([(335,50),(435,50),(435,120),(335,120)],5,'red')
        if timer_hour<10:
            canvas.draw_text('0'+str(alarm_hour),(70,200),100,'pink')
        else:
            canvas.draw_text(str(alarm_hour),(70,200),100,'pink')
        if timer_minutes<10:
            canvas.draw_text('0'+str(alarm_minutes),(205,200),100,'pink')
        else:
            canvas.draw_text(str(alarm_minutes),(205,200),100,'pink')
        if timer_seconds<10:
            canvas.draw_text('0'+str(alarm_seconds),(340,200),100,'pink')
        else:
            canvas.draw_text(str(alarm_seconds),(340,200),100,'pink')
        canvas.draw_text(am_pm,(360,200),50,'pink')
        canvas.draw_polyline([(77,228),(157,228),(117,285),(77,228)],5,'white')
        canvas.draw_polyline([(211,228),(291,228),(251,285),(211,228)],5,'white')
        canvas.draw_polyline([(345,228),(425,228),(385,285),(345,228)],5,'white')
        canvas.draw_polygon([(67,220),(167,220),(167,290),(67,290)],5,'red')
        canvas.draw_polygon([(201,220),(301,220),(301,290),(201,290)],5,'red')
        canvas.draw_polygon([(335,220),(435,220),(435,290),(335,290)],5,'red')
# to display stopwatch
    if mode==3:
        canvas.draw_text(stopwatch_time,(100,100),50,'red')
        canvas.draw_text('Start',(56,458),30,'white')
        canvas.draw_text('Stop',(156,458),30,'white')
        canvas.draw_text(stopwatch_pause_resume,(256,458),30,'white')
        canvas.draw_text('Reset',(396,458),28,'white')
        canvas.draw_polygon([(50,430),(120,430),(120,470),(50,470)],5,'red') #start button
        canvas.draw_polygon([(150,430),(220,430),(220,470),(150,470)],5,'red') #stop button
        canvas.draw_polygon([(250,430),(355,430),(355,470),(250,470)],5,'red') #pause button
        canvas.draw_polygon([(390,430),(460,430),(460,470),(390,470)],5,'red') # reset button
# create frame and timer
frame = simplegui.create_frame('StopWatch',500,500)
stopwatch = simplegui.create_timer(10,stopwatch_control)
timer = simplegui.create_timer(1000,timer_control)
# register event handler
frame.set_draw_handler(draw)
# frame.add_button('Start',start_stopwatch_time)
# frame.add_button('Stop',stop_stopwatch_time)
# frame.add_button('Pause',pause_stopwatch_time)
# frame.add_button('Reset',reset_stopwatch_time)
frame.add_button('Timer',timer_mode)
frame.add_button('Alarm Clock',alarm_mode) #to set mode to timer mode
frame.add_button('Stopwatch',stopwatch_mode) # to set mode to alarm clock
# frame.set_mouseclick_handler(mouse_handler_for_stopwatch) # to set mode to stopwatch
# frame.set_mouseclick_handler(mouse_handler_for_timer) # to set mode to stopwatch
# start frame and timer
frame.start()
# timer.start()