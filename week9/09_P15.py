def knows(R, x, y):
    if R[x] in y:
        return True
    else:
        return False
def is_celeb(R, x):  
# return True if a is celeb, otherwise return False
# return False if x knows someone who is not him/herself
# return False if there exists someone in R who don't know x
# otherwise return True


def find_celeb(R):
    for x in R:
        if is_celeb(R,x):
            break
            return x
    return None
        


def read_relations():
 # build a dictionary R from inputs
 # whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        if d[0] not in R:
            R[d[0]]={d[1]}
        else:
            R[d[0]].add(d[1])
    return R
def main():
    R=read_relations()
    c=find_celeb(R)
    #if c == None:
        #print("Not Found")
    #else:
        #print(c)
exec(input().strip())