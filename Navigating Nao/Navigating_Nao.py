
#import predictor as pred
import qi
import argparse
import threading
from naoqi import ALProxy
import numpy as np
import time as time
import socket
import struct







def main(IP, PORT):
    HOST = '127.0.0.1'  # The server's hostname or IP address
    tcpPort = 65432        # The port used by the server
    print ("Connecting to", IP, "with port", PORT)
    motion = ALProxy("ALMotion", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)
    tracker = ALProxy("ALTracker", IP, PORT)
    awareness = ALProxy("ALBasicAwareness", IP, PORT)
    memory = ALProxy("ALMemory", IP, PORT)
    speech = ALProxy("ALTextToSpeech", IP, PORT)
    
    # First, wake up.
    motion.wakeUp()

    fractionMaxSpeed = 0.8
    # Go to posture stand
    posture.goToPosture("StandInit", fractionMaxSpeed)
    

    awareness.pauseAwareness()


    print ("ALTracker successfully started")
    print ("Use Ctrl+c to stop this script.")

    import time
    import math
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, tcpPort))
        while True:
            data = s.recv(1024)
            data = data.encode()
            data = struct.unpack('BBBBBBBB',data)
            time.sleep(0.1)
            print(type(data), data)
            if data != None:
                if data[0] == 0:
                    speech.say("Walking forward")
                    motion.moveTo(0.5, 0.0, 0.0)
                    data = None
                elif data[0] == 1:
                    speech.say("Staying idle")
                    data = None
                elif data[0] == 2:
                    speech.say("Turning right")
                    motion.moveTo(0.0, 0.0, -math.pi/2)
                    data = None
                elif data[0] == 3:
                    speech.say("Turning left")
                    motion.moveTo(0.0, 0.0, math.pi/2)
                    data = None

    except KeyboardInterrupt:
        print()
        print ("Interrupted by user")
        print ("Stopping...")
    # Stop tracker, go to posture Sit.


    awareness.resumeAwareness()
    posture.goToPosture("Sit", fractionMaxSpeed)
    motion.rest()
    print ("ALTracker stopped.")

    

    #t1.start()
    

    def loadProxy(pName):
        print ("---------------------")
        print ("Loading proxy")
        print ("---------------------")
        proxy = ALProxy(pName, IP, PORT)
        print ("---------------------")
        print ("Starting " + pName + " Tests")
        print ("---------------------")
        return proxy



if __name__ == "__main__" :
    main("192.168.43.116",9559)
