listBarng = {}

def mainMenu () :
    condition = True
    while condition :    
        print()
        print("""            #=== Wellcome to Andimart===

            Pilih apa yang ingin dilakukan :

                1. Input List Item
                2. Update List Item
                3. Delete List Item
                4. View List Item
                5. Check List Item
                6. Pay List Item
                7. Exit

            """)
        userInput = input("Masukan pilihan disini : ")

        if userInput == "1" :
                print()
                addListItem()
        elif userInput == "2" :
                print()
                updateListItem()
        elif userInput == "3" :
                deleteListItem()
        elif userInput == "4" :
                print()
                viewListItem()
        elif userInput == "5" :
                print()
                checkListItem()
        elif userInput == "6" :
                print()
                diskon()
        elif userInput == "7" :
            condition = False
        else :
                print()
                print("Tolong masukan nomor yang sesuai")
                mainMenu()

#function Add List Item Yang Dibeli
def addListItem () :
    barang = input("Masukan nama barang yang ingin dibeli : ")
    harga = int(input("Masukan harga barang : "))
    jumlah = int(input("Masukan jumlah barang : "))
    listBarng[barang] = [jumlah,harga] #Dict of lists
    #print(listBarng)

#function Update List Item Yang Dibeli
def updateListItem () :
    userUpdateInput = input("Masukan barang apa yang ingin diUpdate : ")
    for key,value in listBarng.items() :
        if userUpdateInput in key :
            print(f"Nama barang : {key}")
            print(f"Jumlah barang : {value[0]}")
            print(f"Harga barang : {value[1]}")
            print()
            updateJumlah = int(input("Masukan jumlah yang ingin diupdate : "))
            updateHarga = int(input("Masukan harga yang ingin diupdate : "))
            listBarng[userUpdateInput] = [updateJumlah,updateHarga]
            print(listBarng)
       

#function view List Item Yang Dibeli
def viewListItem () :
    for key,value in listBarng.items() :
        if len(listBarng) > 1 :
            print(f"Nama barang : {key}")
            print(f"Jumlah barang : {value[0]}")
            print(f"Harga barang : {value[1]}")
            print()
        else :
            print(f"Nama barang : {key}")
            print(f"Jumlah barang : {value[0]}")
            print(f"Harga barang : {value[1]}")

#Function Check Item Yang Sudah Dibeli
def checkListItem() :
    for key,value in listBarng.items() :
            if len(value)  * 1 == 2 :
                print("DATA BENAR")
            else :
                print("Data Salah : ")
#Function check apakah user dapat diskon ?
def diskon () :
    for key,value in listBarng.items() :
        total = value[0] * value[1]
        if total >= 500000 :
                counter = total - (total - (total * 90/100) )
                print()
                print("Anda Mendapatkan Diskon 1")
                print(f"Nama barang : {key}")
                print(f"Jumlah barang : {value[0]}")
                print(f"Harga barang : Rp{counter}")
        elif total >= 300000 :
                counter = total - (total - (total * 92/100) )
                print()
                print("Anda Mendapatkan Diskon 2")
                print(f"Nama barang : {key}")
                print(f"Jumlah barang : {value[0]}")
                print(f"Harga barang : Rp{counter}")
        elif total >= 200000 :
                counter = total - (total - (total * 95/100) )
                print()
                print("Anda Mendapatkan Diskon 3")
                print(f"Nama barang : {key}")
                print(f"Jumlah barang : {value[0]}")
                print(f"Harga barang : Rp{counter}")
        else :
                print()
                print("Anda Belum Mendapatkan Diskon")
                print(f"Nama barang : {key}")
                print(f"Jumlah barang : {value[0]}")
                print(f"Harga barang : {total}")

#Function Delete Item Belanjaan
def deleteListItem () :
    print("""

        Pilih apa yang ingin dilakukan :

            1. Delete All List Item
            2. Delete List Item

        """)
    deleteInput = input("Pilihanmu : ")
    if deleteInput == "1" :
        listBarng.clear()
        print("Delete All List Item Succes")
    elif deleteInput == "2" :
        inputListDel = input("Item apa yang ingin dihhapus : ")
        # for key,value in listBarng.items() :
        #     if key in inputListDel :
        #         try :
        del listBarng[inputListDel]
        print("Delete List Item Succes")
        # except : 
        #     mainMenu()       
    else :
        print("Mohon masukan list item yang benar untuk dihapus !!!")
        print("Masukan 1-2 opsi yang tersedia !!!")
        deleteListItem()
# def checkListItem () :

    
mainMenu()