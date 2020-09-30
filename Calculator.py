while True:
    print("1. Addition ")
    print("2. Substraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Exit ")
    choice = int(input("Enter your choice :"))
    if (choice >=1 and choice<=4):
        print("Enter Two Numbers")
        num1 = int(input())
        num2 = int(input())
        if (choice == 1):
            result = num1 + num2
            print("Result = :", result)
        elif(choice == 2):
            result = num1-num2
            print("Result :",result)
        elif (choice == 3):
            result = num1 * num2
            print("Result :" , result)
        else:
            try:
                result = num1 / num2
                print("Result :" , result)
            except Exception:
                print("you can't Devided a Number by Zero :")
    elif(choice == 5):
        print("exit Successfully :")
        exit()
    else:
        print("Wrong Input...!!")