#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on April 23, 2021, at 16:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division
import sys
import socket
from time import time, sleep
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import pandas as pd;

from psychopy.hardware import keyboard


# host and port of tcp tagging server
HOST = '10.5.50.166'
PORT = 15361

# Event identifier (See stimulation codes in OpenVibe documentation)
EVENT_ID = 5+0x8100

# Artificial delay (ms). It may need to be increased if the time to send the tag is too long and causes tag loss.
DELAY=0

# transform a value into an array of byte values in little-endian order.
def to_byte(value, length):
    for x in range(length):
        yield value%256
        value//=256

# connect 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected")

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'FirstExperiment'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\atace\\OneDrive\\Documents\\FirstExperiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "EOG_eyes_open"
EOG_eyes_openClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
tel = visual.TextStim(win=win, name='tel',
    text='Wait',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('250', secs=2.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "EOG_eyes_closed"
EOG_eyes_closedClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Closed',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_1 = sound.Sound('440', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)

# Initialize components for Routine "Wait"
WaitClock = core.Clock()
tel = visual.TextStim(win=win, name='tel',
    text='Wait',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('250', secs=2.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)

# Initialize components for Routine "trial_R"
trial_RClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Right = visual.TextStim(win=win, name='Right',
    text='➔',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Black = visual.TextStim(win=win, name='Black',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial_L"
trial_LClock = core.Clock()
Fixation2 = visual.TextStim(win=win, name='Fixation2',
    text='+\n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Left = visual.TextStim(win=win, name='Left',
    text='←',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Black2 = visual.TextStim(win=win, name='Black2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial_walk"
trial_walkClock = core.Clock()
Fixation3 = visual.TextStim(win=win, name='Fixation3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Walk = visual.TextStim(win=win, name='Walk',
    text='↑',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Black3 = visual.TextStim(win=win, name='Black3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial_stop"
trial_stopClock = core.Clock()
Fixation4 = visual.TextStim(win=win, name='Fixation4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Idle = visual.TextStim(win=win, name='Idle',
    text='X',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Black4 = visual.TextStim(win=win, name='Black4',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "EOG_eyes_open"-------
continueRoutine = True
routineTimer.add(60.000000)
routineTimer.add(60.000000)
# update component parameters for each repeat
# keep track of which components have finished
EOG_eyes_openComponents = [text]
for thisComponent in EOG_eyes_openComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EOG_eyes_openClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# create the three pieces of the tag, padding, event_id and timestamp
padding=[0]*8
event_id=list(to_byte(EVENT_ID, 8))

# timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
timestamp=list(to_byte(0, 8))

# send tag and sleep
s.sendall(bytearray(padding+event_id+timestamp))

# -------Run Routine "EOG_eyes_open"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EOG_eyes_openClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EOG_eyes_openClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 120.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EOG_eyes_openComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# create the three pieces of the tag, padding, event_id and timestamp
padding=[0]*8
event_id=list(to_byte(EVENT_ID, 8))

# timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
timestamp=list(to_byte(0, 8))

# send tag and sleep
s.sendall(bytearray(padding+event_id+timestamp))

# -------Ending Routine "EOG_eyes_open"-------
for thisComponent in EOG_eyes_openComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "Wait"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
sound_2.setSound('250', secs=2.0, hamming=True)
sound_2.setVolume(1.0, log=False)
# keep track of which components have finished
WaitComponents = [tel, sound_2]
for thisComponent in WaitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = WaitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *tel* updates
    if tel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tel.frameNStart = frameN  # exact frame index
        tel.tStart = t  # local t and not account for scr refresh
        tel.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tel, 'tStartRefresh')  # time at next scr refresh
        tel.setAutoDraw(True)
    if tel.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tel.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            tel.tStop = t  # not accounting for scr refresh
            tel.frameNStop = frameN  # exact frame index
            win.timeOnFlip(tel, 'tStopRefresh')  # time at next scr refresh
            tel.setAutoDraw(False)
    # start/stop sound_2
    if sound_2.status == NOT_STARTED and tThisFlip >= 18.0-frameTolerance:
        # keep track of start time/frame for later
        sound_2.frameNStart = frameN  # exact frame index
        sound_2.tStart = t  # local t and not account for scr refresh
        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
        sound_2.play(when=win)  # sync with win flip
    if sound_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_2.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            sound_2.tStop = t  # not accounting for scr refresh
            sound_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
            sound_2.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait"-------
for thisComponent in WaitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('tel.started', tel.tStartRefresh)
thisExp.addData('tel.stopped', tel.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)

# ------Prepare to start Routine "EOG_eyes_closed"-------
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
sound_1.setSound('440', secs=1.0, hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
EOG_eyes_closedComponents = [text_2, sound_1]
for thisComponent in EOG_eyes_closedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EOG_eyes_closedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# create the three pieces of the tag, padding, event_id and timestamp
padding=[0]*8
event_id=list(to_byte(EVENT_ID, 8))

# timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
timestamp=list(to_byte(0, 8))

# send tag and sleep
s.sendall(bytearray(padding+event_id+timestamp))

# -------Run Routine "EOG_eyes_closed"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EOG_eyes_closedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EOG_eyes_closedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 60.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 59.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
            sound_1.stop()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EOG_eyes_closedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# create the three pieces of the tag, padding, event_id and timestamp
padding=[0]*8
event_id=list(to_byte(EVENT_ID, 8))

# timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
timestamp=list(to_byte(0, 8))

# send tag and sleep
s.sendall(bytearray(padding+event_id+timestamp))

# -------Ending Routine "EOG_eyes_closed"-------
for thisComponent in EOG_eyes_closedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=32.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

i=0

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    f = open(r"C:\Users\atace\eegnet-based-embedded-bci-master\PresentationrunS6_{}.txt".format(i), "x")
    # ------Prepare to start Routine "Wait"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    sound_2.setSound('250', secs=2.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    # keep track of which components have finished
    WaitComponents = [tel, sound_2]
    for thisComponent in WaitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WaitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Wait"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WaitClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WaitClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tel* updates
        if tel.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tel.frameNStart = frameN  # exact frame index
            tel.tStart = t  # local t and not account for scr refresh
            tel.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tel, 'tStartRefresh')  # time at next scr refresh
            tel.setAutoDraw(True)
        if tel.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tel.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                tel.tStop = t  # not accounting for scr refresh
                tel.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tel, 'tStopRefresh')  # time at next scr refresh
                tel.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 18.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Wait"-------
    for thisComponent in WaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('tel.started', tel.tStartRefresh)
    trials_2.addData('tel.stopped', tel.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('sound_2.started', sound_2.tStartRefresh)
    trials_2.addData('sound_2.stopped', sound_2.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Mappe1.xlsx'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # create the three pieces of the tag, padding, event_id and timestamp
    padding=[0]*8
    event_id=list(to_byte(EVENT_ID, 8))

    # timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
    timestamp=list(to_byte(0, 8))

    # send tag and sleep
    s.sendall(bytearray(padding+event_id+timestamp))

    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=asarray(nRepsRight), method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial_R"-------
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trial_RComponents = [Fixation, Right, Black]
            for thisComponent in trial_RComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trial_RClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial_R"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_RClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trial_RClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation* updates
                if Fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation.frameNStart = frameN  # exact frame index
                    Fixation.tStart = t  # local t and not account for scr refresh
                    Fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation, 'tStartRefresh')  # time at next scr refresh
                    Fixation.setAutoDraw(True)
                if Fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation.tStop = t  # not accounting for scr refresh
                        Fixation.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Fixation, 'tStopRefresh')  # time at next scr refresh
                        Fixation.setAutoDraw(False)
                
                # *Right* updates
                if Right.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    Right.frameNStart = frameN  # exact frame index
                    Right.tStart = t  # local t and not account for scr refresh
                    Right.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Right, 'tStartRefresh')  # time at next scr refresh
                    Right.setAutoDraw(True)
                if Right.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Right.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Right.tStop = t  # not accounting for scr refresh
                        Right.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Right, 'tStopRefresh')  # time at next scr refresh
                        Right.setAutoDraw(False)
                
                # *Black* updates
                if Black.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                    # keep track of start time/frame for later
                    Black.frameNStart = frameN  # exact frame index
                    Black.tStart = t  # local t and not account for scr refresh
                    Black.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Black, 'tStartRefresh')  # time at next scr refresh
                    Black.setAutoDraw(True)
                if Black.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Black.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Black.tStop = t  # not accounting for scr refresh
                        Black.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Black, 'tStopRefresh')  # time at next scr refresh
                        Black.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_RComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_R"-------
            for thisComponent in trial_RComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_3.addData('Fixation.started', Fixation.tStartRefresh)
            trials_3.addData('Fixation.stopped', Fixation.tStopRefresh)
            trials_3.addData('Right.started', Right.tStartRefresh)
            trials_3.addData('Right.stopped', Right.tStopRefresh)
            trials_3.addData('Black.started', Black.tStartRefresh)
            trials_3.addData('Black.stopped', Black.tStopRefresh)
            f.write("2")
            f.write("\n")
            thisExp.nextEntry()
            
        # completed asarray(nRepsRight) repeats of 'trials_3'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_4 = data.TrialHandler(nReps=asarray(nRepsLeft), method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_4')
        thisExp.addLoop(trials_4)  # add the loop to the experiment
        thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
        if thisTrial_4 != None:
            for paramName in thisTrial_4:
                exec('{} = thisTrial_4[paramName]'.format(paramName))
        
        for thisTrial_4 in trials_4:
            currentLoop = trials_4
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial_L"-------
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trial_LComponents = [Fixation2, Left, Black2]
            for thisComponent in trial_LComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trial_LClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial_L"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_LClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trial_LClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation2* updates
                if Fixation2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation2.frameNStart = frameN  # exact frame index
                    Fixation2.tStart = t  # local t and not account for scr refresh
                    Fixation2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation2, 'tStartRefresh')  # time at next scr refresh
                    Fixation2.setAutoDraw(True)
                if Fixation2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation2.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation2.tStop = t  # not accounting for scr refresh
                        Fixation2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Fixation2, 'tStopRefresh')  # time at next scr refresh
                        Fixation2.setAutoDraw(False)
                
                # *Left* updates
                if Left.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    Left.frameNStart = frameN  # exact frame index
                    Left.tStart = t  # local t and not account for scr refresh
                    Left.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Left, 'tStartRefresh')  # time at next scr refresh
                    Left.setAutoDraw(True)
                if Left.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Left.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Left.tStop = t  # not accounting for scr refresh
                        Left.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Left, 'tStopRefresh')  # time at next scr refresh
                        Left.setAutoDraw(False)
                
                # *Black2* updates
                if Black2.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                    # keep track of start time/frame for later
                    Black2.frameNStart = frameN  # exact frame index
                    Black2.tStart = t  # local t and not account for scr refresh
                    Black2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Black2, 'tStartRefresh')  # time at next scr refresh
                    Black2.setAutoDraw(True)
                if Black2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Black2.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Black2.tStop = t  # not accounting for scr refresh
                        Black2.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Black2, 'tStopRefresh')  # time at next scr refresh
                        Black2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_LComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_L"-------
            for thisComponent in trial_LComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_4.addData('Fixation2.started', Fixation2.tStartRefresh)
            trials_4.addData('Fixation2.stopped', Fixation2.tStopRefresh)
            trials_4.addData('Left.started', Left.tStartRefresh)
            trials_4.addData('Left.stopped', Left.tStopRefresh)
            trials_4.addData('Black2.started', Black2.tStartRefresh)
            trials_4.addData('Black2.stopped', Black2.tStopRefresh)
            f.write("3")
            f.write("\n")
            thisExp.nextEntry()
            
        # completed asarray(nRepsLeft) repeats of 'trials_4'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_5 = data.TrialHandler(nReps=asarray(nRepsWalk), method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_5')
        thisExp.addLoop(trials_5)  # add the loop to the experiment
        thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
        for thisTrial_5 in trials_5:
            currentLoop = trials_5
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
            if thisTrial_5 != None:
                for paramName in thisTrial_5:
                    exec('{} = thisTrial_5[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial_walk"-------
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trial_walkComponents = [Fixation3, Walk, Black3]
            for thisComponent in trial_walkComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trial_walkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial_walk"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_walkClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trial_walkClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation3* updates
                if Fixation3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation3.frameNStart = frameN  # exact frame index
                    Fixation3.tStart = t  # local t and not account for scr refresh
                    Fixation3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation3, 'tStartRefresh')  # time at next scr refresh
                    Fixation3.setAutoDraw(True)
                if Fixation3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation3.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation3.tStop = t  # not accounting for scr refresh
                        Fixation3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Fixation3, 'tStopRefresh')  # time at next scr refresh
                        Fixation3.setAutoDraw(False)
                
                # *Walk* updates
                if Walk.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    Walk.frameNStart = frameN  # exact frame index
                    Walk.tStart = t  # local t and not account for scr refresh
                    Walk.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Walk, 'tStartRefresh')  # time at next scr refresh
                    Walk.setAutoDraw(True)
                if Walk.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Walk.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Walk.tStop = t  # not accounting for scr refresh
                        Walk.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Walk, 'tStopRefresh')  # time at next scr refresh
                        Walk.setAutoDraw(False)
                
                # *Black3* updates
                if Black3.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                    # keep track of start time/frame for later
                    Black3.frameNStart = frameN  # exact frame index
                    Black3.tStart = t  # local t and not account for scr refresh
                    Black3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Black3, 'tStartRefresh')  # time at next scr refresh
                    Black3.setAutoDraw(True)
                if Black3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Black3.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Black3.tStop = t  # not accounting for scr refresh
                        Black3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Black3, 'tStopRefresh')  # time at next scr refresh
                        Black3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_walkComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_walk"-------
            for thisComponent in trial_walkComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_5.addData('Fixation3.started', Fixation3.tStartRefresh)
            trials_5.addData('Fixation3.stopped', Fixation3.tStopRefresh)
            trials_5.addData('Walk.started', Walk.tStartRefresh)
            trials_5.addData('Walk.stopped', Walk.tStopRefresh)
            trials_5.addData('Black3.started', Black3.tStartRefresh)
            trials_5.addData('Black3.stopped', Black3.tStopRefresh)
            f.write("0")
            f.write("\n")
            thisExp.nextEntry()
            
        # completed asarray(nRepsWalk) repeats of 'trials_5'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_6 = data.TrialHandler(nReps=asarray(nRepsIdle), method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='trials_6')
        thisExp.addLoop(trials_6)  # add the loop to the experiment
        thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                exec('{} = thisTrial_6[paramName]'.format(paramName))
        
        for thisTrial_6 in trials_6:
            currentLoop = trials_6
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
            if thisTrial_6 != None:
                for paramName in thisTrial_6:
                    exec('{} = thisTrial_6[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial_stop"-------
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            trial_stopComponents = [Fixation4, Idle, Black4]
            for thisComponent in trial_stopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            trial_stopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "trial_stop"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trial_stopClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=trial_stopClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation4* updates
                if Fixation4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation4.frameNStart = frameN  # exact frame index
                    Fixation4.tStart = t  # local t and not account for scr refresh
                    Fixation4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation4, 'tStartRefresh')  # time at next scr refresh
                    Fixation4.setAutoDraw(True)
                if Fixation4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation4.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation4.tStop = t  # not accounting for scr refresh
                        Fixation4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Fixation4, 'tStopRefresh')  # time at next scr refresh
                        Fixation4.setAutoDraw(False)
                
                # *Idle* updates
                if Idle.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
                    # keep track of start time/frame for later
                    Idle.frameNStart = frameN  # exact frame index
                    Idle.tStart = t  # local t and not account for scr refresh
                    Idle.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Idle, 'tStartRefresh')  # time at next scr refresh
                    Idle.setAutoDraw(True)
                if Idle.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Idle.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Idle.tStop = t  # not accounting for scr refresh
                        Idle.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Idle, 'tStopRefresh')  # time at next scr refresh
                        Idle.setAutoDraw(False)
                
                # *Black4* updates
                if Black4.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                    # keep track of start time/frame for later
                    Black4.frameNStart = frameN  # exact frame index
                    Black4.tStart = t  # local t and not account for scr refresh
                    Black4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Black4, 'tStartRefresh')  # time at next scr refresh
                    Black4.setAutoDraw(True)
                if Black4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Black4.tStartRefresh + 4.0-frameTolerance:
                        # keep track of stop time/frame for later
                        Black4.tStop = t  # not accounting for scr refresh
                        Black4.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(Black4, 'tStopRefresh')  # time at next scr refresh
                        Black4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_stopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial_stop"-------
            for thisComponent in trial_stopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_6.addData('Fixation4.started', Fixation4.tStartRefresh)
            trials_6.addData('Fixation4.stopped', Fixation4.tStopRefresh)
            trials_6.addData('Idle.started', Idle.tStartRefresh)
            trials_6.addData('Idle.stopped', Idle.tStopRefresh)
            trials_6.addData('Black4.started', Black4.tStartRefresh)
            trials_6.addData('Black4.stopped', Black4.tStopRefresh)
            f.write("1")
            f.write("\n")
            thisExp.nextEntry()
            
        # completed asarray(nRepsIdle) repeats of 'trials_6'
        
        thisExp.nextEntry()
    
    # create the three pieces of the tag, padding, event_id and timestamp
    padding=[0]*8
    event_id=list(to_byte(EVENT_ID, 8))

    # timestamp can be either the posix time in ms, or 0 to let the acquisition server timestamp the tag itself.
    timestamp=list(to_byte(0, 8))

    # send tag and sleep
    s.sendall(bytearray(padding+event_id+timestamp))
    
    # completed 1.0 repeats of 'trials'
    f.close()
    i += 1
    thisExp.nextEntry()

# completed 8.0 repeats of 'trials_2'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
