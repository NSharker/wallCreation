import math



'''
laserDataFile = open('firstDataLaser.txt','r')

wallCoordinateFile = open('wallCoordinate.txt', 'w')

#print("start printing")

#print(laserDataFile.readline().split("\t"))

#print("Done printing")

currentRobotXPos = 9.6347360611

currentRobotYPos = 20.1799144745

currentAngleInRadian = -1.91986000538

angleIncrementInRadian = 0.00581699982285

for laserDistance in laserDataFile.readline().split("\t"):
    if (laserDistance != 25):
        wallX = (float(laserDistance) * math.cos(currentAngleInRadian)) + currentRobotXPos
        wallY = (float(laserDistance) * math.sin(currentAngleInRadian)) + currentRobotYPos
        wallCoorTuple = (wallX, wallY)
        wallCoorTupleString = str(wallCoorTuple)
        wallCoordinateFile.write(wallCoorTupleString)
        wallCoordinateFile.write('\n')
    currentAngleInRadian += angleIncrementInRadian

laserDataFile.close()
wallCoordinateFile.close()
'''


def wallCoordinates(robotXPos, robotYPos, maxDistOfLaser, startingAngle, angleIncrement, laserStride, listOfLaserReading):
    """Returns a list of coordinates where the lasers hit the walls.
    
    Keyword Argumenets:
    robotXPos -- the X coordinate of the robot
    robotYPos -- the Y coordinate of the robot
    maxDistOfLaser -- the maximum distance of the laser
    startingAngle -- the starting angle in radians
    angleIncrement -- the angle increment for each laser
    laserStride -- the stride between the lasers?, 1 includes all lasers, 2 includes every other laser and so on
    listOfLaserReading -- the list of all the laser readings
    """
    
    listOfCoordinates = []
    currentAngleInRadian = float(startingAngle)
    for currentLaserReading in listOfLaserReading[::laserStride]:
        if(float(currentLaserReading) < float(maxDistOfLaser)):
            wallX = (float(currentLaserReading) * math.cos(float(currentAngleInRadian))) + float(robotXPos)
            wallY = (float(currentLaserReading) * math.sin(float(currentAngleInRadian))) + float(robotYPos)
            wallCoorTuple = (wallX, wallY)
            listOfCoordinates.append(wallCoorTuple)
        currentAngleInRadian = currentAngleInRadian + (float(laserStride) * float(angleIncrement))
        
    return listOfCoordinates

'''
PARSER SECTION
'''

laserDataFile = open('data_laser.txt','r')
robotPoseFile = open('data_pose.txt','r')

#wallCoordinateFile = open('wallCoordinates.txt', 'w')
timeStep = 0


laserStrideNumber = 1

#grabbing the header line for each file, these are not needed
#laserDataFile.readline()
#robotPoseFile.readline()
testLaser = laserDataFile.readline().split(",")
#print("startingAngle: " + str(testLaser[4]))
#print("maxDistOfLaser: " + str(testLaser[10]))
#print("angleIncrement: " + str(testLaser[6]))
testPose = robotPoseFile.readline().split(",")
#print("X coordinate: " + str(testPose[4]))
#print("Y coordinate: " + str(testPose[5]))


for laserDataLine in laserDataFile.readlines():
    poseDataLineSplit = robotPoseFile.readline().split(",")
    laserDataLineSplit = laserDataLine.split(",")
    laserReaderList = []
    for laser in laserDataLineSplit[11:]:
        laserReaderList.append(laser)
        
    wallTupleList = wallCoordinates(poseDataLineSplit[4], poseDataLineSplit[5], laserDataLineSplit[10], laserDataLineSplit[4], laserDataLineSplit[6],laserStrideNumber, laserReaderList) 
    writingCoordinateToFile = open ( str(timeStep) + '.txt', 'w')
    
    for tupleCoordinate in wallTupleList:
        writingCoordinateToFile.write(str(tupleCoordinate))
        writingCoordinateToFile.write("\n")
    writingCoordinateToFile.close()
    timeStep = timeStep + 1
    



    
laserDataFile.close()
robotPoseFile.close()
#wallCoordinateFile.close()
'''
laserData = []

for item in laserDataFile.readline().split("\t"):
    laserData.append(item)

listOfWallCoordinates = wallCoordinates(9.6347360611, 20.1799144745, 25, -1.91986000538, 0.00581699982285, 1, laserData)

print(listOfWallCoordinates[0])
print (len(listOfWallCoordinates))
laserDataFile.close()
'''

