import math

points = [(0.0, 1.0), (1.0, 2.0), (2.0, 1.0), (1.0, 0.0), (3.0, 1.0), (4.0, 2.0), (5.0, 1.0), (4.0, 0.0)]
centers = [[2.0, 1.0], [4.0, 2.0]]

def dist(pointOne, pointTwo):
    xDist = pointOne[0] - pointTwo[0]
    yDist = pointOne[1] - pointTwo[1]
    return math.sqrt(math.pow(xDist,2)+math.pow(yDist,2))

def kMeans(points, centers):
    n = 0
    while n<3:
        centerOne = 0
        centerTwo = 0
        clusterOne = []
        clusterTwo = []
        clusterOneCen = [0.0, 0.0]
        clusterTwoCen = [0.0, 0.0]
        for point in points:
            if dist(point, centers[0]) < dist(point, centers[1]):
                clusterOne.append(point)
                clusterOneCen[0] += point[0]
                clusterOneCen[1] += point[1]
                centerOne += 1
            else:
                clusterTwo.append(point)
                clusterTwoCen[0] += point[0]
                clusterTwoCen[1] += point[1]
                centerTwo += 1
        centers[0][0] = clusterOneCen[0] / centerOne
        centers[0][1] = clusterOneCen[1] / centerOne
        centers[1][0] = clusterTwoCen[0] / centerTwo
        centers[1][1] = clusterTwoCen[1] / centerTwo
        n += 1
        print "Centers: %s, Cluster One: %s, Cluster Two: %s" % (centers, clusterOne, clusterTwo)

if __name__ == '__main__':
    kMeans(points, centers)