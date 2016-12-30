import math




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
        
        
    


