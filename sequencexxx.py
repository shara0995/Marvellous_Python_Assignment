
def CircleArea(rad,PI=3.14):
     Area=PI* rad*rad
     return Area

def main():
    print("enter radiaus:")
    radius=float(input())
    result=CircleArea(radius)
    print("area of circle",result)
if __name__=="__main__":
    main()