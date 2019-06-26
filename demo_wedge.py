from psychopy import visual, core, event
import time

mywin = visual.Window([1200,1200],monitor="testMonitor", units="deg", winType = 'glfw',)


wedge = visual.RadialStim(win = mywin, size =(30, 30),
                          radialCycles = 0,
                          angularCycles = 4)

counter_win = visual.Window([300,300],monitor="testMonitor", units="cm", winType = 'glfw',)
counter = visual.TextStim(counter_win, text = str(0), height = 8)
counter.autoDraw = True

start_time = time.time()
direction = 1

dir_time = 2
dir_change_number = 0

while True:

    time.sleep(0.0001)
    
    if time.time() - (start_time + ((dir_change_number + 1) * dir_time)) > 0:
        dir_change_number += 1
        direction *= -1
        counter.setText(str(dir_change_number))
    
    wedge.angularPhase += direction *.005
    wedge.draw()
    mywin.flip()
    counter_win.flip()

    if len(event.getKeys())>0:
        break
    event.clearEvents()
    
mywin.close()
core.quit()
