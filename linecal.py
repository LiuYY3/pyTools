# This is made for count OrientationX's line number
import os

def allFile(path):
    pathDir = os.listdir(path)
    count = 0
    for allDir in pathDir:
        if allDir[-5:] == '.java' or allDir[-4:] == '.xml':
            count = count + cal(path + allDir)
        elif '.' in allDir:
            count = count
        elif allDir == 'channel':
            count = count
        else:
            count = count + allFile(path + allDir + "\\")
    return count

def cal(filename):
    file = open(filename, 'r', encoding = 'UTF-8')
    count = 0
    for line in file.readlines():
        if line != '\n' and line != '':
            count += 1
    file.close()
    return count

if __name__ == '__main__':
    print(allFile("D:\\xmb\\OrientationX\\app\\src\\main\\"))
