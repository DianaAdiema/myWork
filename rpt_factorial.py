def main():
    print("enter the number to get its factorial")
    num = int(input())
    fact = 1
    if num < 1:
        print("The number should not be negative")
    else:
        for i in range(1, num + 1):
            fact = fact * i

    print(fact)



if __name__ == '__main__':
        main()

