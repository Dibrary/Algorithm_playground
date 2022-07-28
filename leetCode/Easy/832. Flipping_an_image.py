

def test(image):
    tmp = []
    for i in image:
        reverse = i[::-1]
        in_array = []
        for k in reverse:
            if k == 1: in_array.append(0)
            else: in_array.append(1)

        tmp.append(in_array)
    return tmp

if __name__=="__main__":
    print(test([[1,1,0],[1,0,1],[0,0,0]]))
    print(test([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
