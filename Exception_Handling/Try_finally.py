def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:  # Executed regardless of error! if the function returns
        print("I'm inside of finally")


main()
