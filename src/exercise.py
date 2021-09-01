def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())
    if (num1 > num2):
        print(str(num1) + " is greater than " + str(num2) + ".")
    elif (num1 < num2):
        print(str(num1) + " is smaller than " + str(num2) + ".")
    else:
        print(str(num1) + " is equal to " + str(num2) + ".")

if __name__ == '__main__':
    main()
