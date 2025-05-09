def CalculatePercentage(total,obtaine):
    output=((obtaine/total)*100)
    return output

def main():
    print("Enter total:")
    value1=int(input())

    print("Enter obtain mark:")
    value2=int(input())

    result=CalculatePercentage(total=value1,obtaine=value2)#keyword arguments
    print("Percentage:", result)

if __name__=="__main__":
    main()