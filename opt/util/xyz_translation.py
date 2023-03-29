import json
import numpy as np

filepath = "/home/ccl/Datasets/NeRF/ScanNerf/airplane1/train_all.json"
framesList = []
def get_XYZ_Path(listIndex):
    string = framesList[listIndex]

    #finds indexes of starting position of matrix and path 
    pathIndex = framesList[listIndex].find(":") + 1
    matrixIndex = framesList[listIndex].find("[") + 1 

    #split the string so we have the class path and matrix seperate 
    StringLen = len(string)
    temp = slice(matrixIndex, StringLen - 2)
    matrix = string[temp]

    temp = slice(pathIndex, pathIndex+27)
    path = string[temp]

    x ,y , z = getXYZ(matrix)

    return x,y,z,path



#get the XYZ values of the matrix 
def getXYZ(newStr):
    row_splt = '], ['
    ele_splt = ","
    temp = newStr.split(row_splt)
    res = [ele.split(ele_splt) for ele in temp]
    x = float(res[0][3])
    y = float(res[1][3])
    z = float(res[2][3])

    return x , y , z 
    
def getEuclideanDistance(x1,y1,z1,x2,y2,z2):
    point_1 = np.array((x1,y1,z1))
    point_2 = np.array((x2,y2,z2))

    square = np.square(point_1 - point_2)
    sum_square = np.sum(square)
    distance = np.sqrt(sum_square)

    return distance 

def findClosestImages(filepath, num_points):

    with open(filepath , 'r') as infile:
        data = infile.read()
        obj = json.loads(data)

    #gets every json object ('frame') and put it into a list 
    for frame in obj["frames"]:
        string = str(frame)
        framesList.append(string)

    angleAdd = 360 / num_points
    angle = 0
    radius = 5
    points_list = []
    #find the different evenly spaced points on the circle 
    for i in range(num_points):
        
        x = radius * np.sin(np.pi * 2 * angle / 360)
        y = radius * np.cos(np.pi * 2 * angle / 360)
        #what should value of z be 
        z = 0 
        points_list.append(np.array((x,y,z)))
        angle += angleAdd 

    #check the closest point from the image to the points 
    minEuclideanDistance = 10000 
    
    imgList = []
    for point in points_list:
        for i in range(len(framesList)):
            x , y , z , imgPath = get_XYZ_Path(i)
            euclideanDistance = getEuclideanDistance(x,y,z,point[0],point[1],point[2]) 
            if(euclideanDistance < minEuclideanDistance):
                minEuclideanDistance = euclideanDistance
                path = imgPath
                index =i 
        imgList.append(str(framesList[index]))
        
    return imgList 


lis = findClosestImages(filepath,10)

#write to json file 
#jsonfile = "\ {"camera_angle_x": 0.8836704333486497, "camera_angle_y": 0.6819013496909203, "fl_x": 1522.1201085541113, "fl_y": 1521.954743529035, "k1": 0.0652210706564525, "k2": 0.23102137964696204, "p1": -0.0018667704274258755, "p2": -0.00035823757611365637, "cx": 727.9348613007779, "cy": 541.5426465751151, "w": 1440, "h": 1080, "aabb_scale": 1, "frames": \"
jsonfile = ''
for x in lis:
    jsonfile += x 
    jsonfile +="\n"

jsonfile+= '}'
jsonfile.replace("\'" , '"')


with open("sample.json", "w") as outfile:
    json.dump(jsonfile, outfile)

print(jsonfile)





