def CalculatePercentage(total=500,obtaine):
 Output=((obtaine/total)*100)
 return output

def main():
    result=CalculatePercentage(350,450)
    print("Result:",result)
    result=CalculatePercentage(450)
    print("Result:",result)
    result=CalculatePercentage()
    print("Result:",result)



if__name__=="__main__":
    main()