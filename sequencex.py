PI=3.14
def CircleArea(rad):
     Area=PI* rad*rad
     return Area

def main():
    print("enter radiaus:")
    radius=float(input())
    result=CircleArea(5)
    print("area of circle",result)
if __name__=="__main__":
    main()