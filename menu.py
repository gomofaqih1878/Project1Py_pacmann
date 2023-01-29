from Project1Py_pacmann.supermarket import Transaction
from dataclasses import dataclass
import os
sistem_operasi = os.name

@dataclass
class Menu : 
    condition : bool
    
    def mainMenu (self) :
        
        # self.condition = True
        while self.condition :  
        #     match sistem_operasi:
        #         case "posix": os.system("clear")
        #         case "nt": os.system("cls") 

            print("SELAMAT DATANG DI PROGRAM")
            print("\tANDI MART")
            print("=========================") 

            print(f"1. Input List Item")
            print(f"2. Update List Item")
            print(f"3. Delete List Item")
            print(f"4. View List Item")
            print(f"5. Check List Item")
            print(f"6. Pay List Item")
            print(f"7. Exit\n")
            
            userInput = input("Masukan pilihan disini : ")

            if userInput == "1" :
                    print()
                    Transaction.addListItem()
            elif userInput == "2" :
                    print()
                    Transaction.updateListItem()
            elif userInput == "3" :
                    Transaction.deleteListItem()
            elif userInput == "4" :
                    print()
                    Transaction.viewListItem()
            elif userInput == "5" :
                    print()
                    Transaction.checkListItem()
            elif userInput == "6" :
                    print()
                    Transaction.payListItem()
            elif userInput == "7" :
                    self.condition = False
            else :
                    print()
                    print("Tolong masukan nomor yang sesuai")
                    Menu.mainMenu()


start = Menu(True)
start.mainMenu()