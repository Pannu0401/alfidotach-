def simple_calc():
        choice=str(input("Select operation:\n*********************\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n=> "))
        if(choice=='1'):
            print("\nAddition~")
            a=int(input("Enter value 1: "))
            b=int(input("Enter value 2: "))
            result = a+b
            print("Outcome:",result)

        elif(choice=='2'):
            print("\nSubtraction~")
            a=int(input("Enter value 1: "))
            b=int(input("Enter value 2: "))
            result = a-b
            print("Outcome:",result)

        elif(choice=='3'):
            print("\nMultiplication~")
            var1=float(input("Enter value 1: "))
            var2=float(input("Enter value 2: "))
            print("Product =>", var1*var2)

        elif(choice=='4'):
            print("\nDivision~")
            var1=float(input("Enter value 1: "))
            var2=float(input("Enter value 2: "))
            print("Product =>", var1/var2)
                

        else:
            print("\nInvalid choice.\nPress any key to continue...")
            m.getch()
            simple_calc()


def main():
    print("================ CALCULATOR =================\n")
    simple_calc()
    

if __name__=='__main__':
    main()