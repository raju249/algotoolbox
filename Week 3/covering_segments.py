# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def getEnd(segment):
    return segment[1]

def inSegment(point,segment):
    if point <= segment[1] and point >= segment[0]:
        return True
    return False

def optimal_points(segments):
    points = []
    #write your code here
    sorted_segments = sorted(segments,key=lambda x:x[1])
    lastPt = getEnd(sorted_segments[0])
    points.append(lastPt)

    for i in range(1,len(sorted_segments)):
        seg = sorted_segments[i]
        if not inSegment(lastPt,seg):
            lastPt = getEnd(seg)
            points.append(lastPt)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')