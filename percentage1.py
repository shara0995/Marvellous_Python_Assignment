def main():
    print("Enter total:")
    value1 = int(input())

    print("Enter obtained mark:")
    value2 = int(input())

    output = (value2 / value1) * 100
    print("Output:", output)

if __name__ == "__main__":
    main()