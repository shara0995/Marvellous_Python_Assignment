def displayed(*A):
    print("Inside Displayed",A)
   


def main():
    displayed(11,22,33,44)
    displayed(11,22,33,44,55)
    displayed(11,22,33)
    displayed(11)
    displayed()

if __name__=="__main__":
    main()