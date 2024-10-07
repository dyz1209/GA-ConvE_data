import CAPEC_Extract
import CVE_Extract
import CWE_Extract
import IOCs_Extract
import Matrix_Concatenation
import RelationMatrix_Extract
import Triplets_Extract

def display_menu():
    """
    Display the menu for selecting which script to execute.
    """
    print("\nPlease select the script to execute:")
    print("CAPEC_Extract. Run CAPEC_Extract.py")
    print("CVE_Extract. Run CVE_Extract.py")
    print("CWE_Extract. Run CWE_Extract.py")
    print("IOCs_Extract. Run IOCs_Extract.py")
    print("Matrix_Concatenation. Run Matrix_Concatenation.py")
    print("RelationMatrix_Extract. Run RelationMatrix_Extract.py")
    print("Triplets_Extract. Run Triplets_Extract.py")
    print("0. Exit")

def main():
    """
    Main loop that waits for user input and calls the appropriate script based on selection.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (CAPEC_Extract, CVE_Extract, CWE_Extract, IOCs_Extract, Matrix_Concatenation, RelationMatrix_Extract, Triplets_Extract, or 0 to Exit): ")

        # Try executing the selected script, and catch any errors.
        try:
            if choice == 'CAPEC_Extract':
                print("Calling CAPEC_Extract.main()")
                CAPEC_Extract.main()
                print("Run successful")
            elif choice == 'CVE_Extract':
                print("Calling CVE_Extract.main()")
                CVE_Extract.main()
                print("Run successful")
            elif choice == 'CWE_Extract':
                print("Calling CWE_Extract.main()")
                CWE_Extract.main()
                print("Run successful")
            elif choice == 'IOCs_Extract':
                print("Calling IOCs_Extract.main()")
                IOCs_Extract.main()
                print("Run successful")
            elif choice == 'Matrix_Concatenation':
                print("Calling Matrix_Concatenation.main()")
                Matrix_Concatenation.main()
                print("Run successful")
            elif choice == 'RelationMatrix_Extract':
                print("Calling RelationMatrix_Extract.main()")
                RelationMatrix_Extract.main()
                print("Run successful")
            elif choice == 'Triplets_Extract':
                print("Calling Triplets_Extract.main()")
                Triplets_Extract.main()
                print("Run successful")
            elif choice == '0':
                print("Exiting program")
                break
            else:
                print("Input error. Please enter a valid choice.")
        except Exception as e:
            # Capture any errors during script execution
            print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    main()
