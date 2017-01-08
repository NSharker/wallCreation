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
    currentAngleInRadian = startingAngle
    for currentLaserReading in listOfLaserReading[::laserStride]:
        if(float(currentLaserReading) < float(maxDistOfLaser)):
            wallX = (float (currentLaserReading) * math.cos(currentAngleInRadian)) + robotXPos
            wallY = (float (currentLaserReading) * math.sin(currentAngleInRadian)) + robotYPos
            wallCoorTuple = (wallX, wallY)
            listOfCoordinates.append(wallCoorTuple)
        currentAngleInRadian = currentAngleInRadian + (laserStride * angleIncrement)
        
    return listOfCoordinates


laserDataFile = open('firstDataLaser.txt','r')

laserData = []

for item in laserDataFile.readline().split("\t"):
    laserData.append(item)

listOfWallCoordinates = wallCoordinates(9.6347360611, 20.1799144745, 25, -1.91986000538, 0.00581699982285, 1, laserData)

print(listOfWallCoordinates[0])
print (len(listOfWallCoordinates))
laserDataFile.close()