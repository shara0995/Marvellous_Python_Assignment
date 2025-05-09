def CalculatePercentage(obtaine,total=500):
    output=((obtaine/total)*100)
    return output

def main():
    

    print("Enter obtain mark:")
    value2=int(input())

    result=CalculatePercentage(value1,value2)#default arguments
    print("Percentage:", result)

if __name__=="__main__":
    main()