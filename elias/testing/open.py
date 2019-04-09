import sys
import os
file = open('/Users/elias/Desktop/Github/smart-workplace/elias/testing/file.txt','r')
coordinates = file.read()
buffer = []
for i in range(0,len(coordinates)):
    if coordinates[i] != '\n':
        buffer.append(coordinates[i])
cleanedBuffer = ''.join(buffer)
latitude = cleanedBuffer[0:9]
longtitude = cleanedBuffer[9:18]
print(latitude)
print(longtitude)
