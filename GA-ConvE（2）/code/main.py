import CAPEC_Extract
import CVE_Extract
import CWE_Extract
import IOCs_Extract
import Matrix_Concatenation
import RelationMatrix_Extract
import Triplets_Extract

def display_menu():
    print("\nPlease select the script to execute:")
    print("1. Run CAPEC_Extract.py")
    print("2. Run CVE_Extract.py")
    print("3. Run CWE_Extract.py")
    print("4. Run IOCs_Extract.py")
    print("5. Run Matrix_Concatenation.py")
    print("6. Run RelationMatrix_Extract.py")
    print("7. Run Triplets_Extract.py")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (0-7): ")

        if choice == '1':
            CAPEC_Extract.main()
        elif choice == '2':
            CVE_Extract.main()
        elif choice == '3':
            CWE_Extract.main()
        elif choice == '4':
            IOCs_Extract.main()
        elif choice == '5':
            Matrix_Concatenation.main()
        elif choice == '6':
            RelationMatrix_Extract.main()
        elif choice == '7':
            Triplets_Extract.main()
        elif choice == '0':
            print("Exiting program")
            break
        else:
            print("Invalid choice, please enter a number between 0 and 7.")

if __name__ == "__main__":
    main()
