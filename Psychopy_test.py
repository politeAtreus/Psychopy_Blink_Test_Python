from psychopy import visual, core

# Parameters for the flashing section
flashDuration = 0.07  # seconds for each flash (0.5 seconds on, 0.5 seconds off)
totalDuration = 10  # total duration of the flashing in seconds
sectionSize = (800, 800)  # size of the flashing section (width, height) in pixels
sectionPos = (0, 0)  # position of the center of the flashing section (x, y) in pixels

# Setup the window (not fullscreen)
win = visual.Window([800, 800], fullscr=True, color=(0, 0, 0))

# Setup the flashing section
flashSection = visual.Rect(win, width=sectionSize[0], height=sectionSize[1], fillColor=[1, 1, 1], lineColor=None, pos=sectionPos)

# Time control
clock = core.Clock()
startTime = clock.getTime()

while clock.getTime() - startTime < totalDuration:
    # Flash on
    flashSection.fillColor = [1, 1, 1]  # White
    flashSection.draw()
    win.flip()
    core.wait(flashDuration)
    
    # Flash off
    win.flip()  # Flipping to the base window color (black)
    core.wait(flashDuration)

win.close()