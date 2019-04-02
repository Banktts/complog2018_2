def distance(p,q):
    # return distance between tuple p and q
    return ( (p[0]-q[0])**2 + (p[1]-q[1])**2 )**0.5
def perimeter(points):
    return sum(list(map(lambda x: distance(points[x],points[x+1]),range(-1,len(points)-1))))
s = input().strip().split()
p = [(float(t[1:t.find(',')]),float(t[t.find(',')+1:-1])) for t in s]
print(perimeter(p))
