from termcolor import colored
def main():
    letters = {"A": 0, "B":1, "C":2, "D":3, "E":4, "F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,
               "P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25,}
    print(colored(" _____       ___   _____   _____       ___   _____   __    __ ","blue"))
    print(colored("/  ___|     /   | | ____| /  ___/     /   | |  _  \\  \\ \\  / /","blue"))
    print(colored("| |        / /| | | |__   | |___     / /| | | |_| |   \\ \\/ /  ","blue"))
    print(colored("| |       / / | | |  __|  \\___  \\   / / | | |  _  /    }  {   ","blue"))
    print(colored("| |___   / /  | | | |___   ___| |  / /  | | | | \\ \\   / /\\ \\  ","blue"))
    print(colored("\\_____| /_/   |_| |_____| /_____/ /_/   |_| |_|  \\_\\ /_/  \\_\\ ","blue"))
    def encryption():
        

        message =input("Enter a message: ").upper().replace(" ","")
        print("Message: ",message)
        for x in message:
            
            key = None
            #print(x, end="")
            sum = (letters[x]+3)%26

            for k, v in letters.items():
               if  v == sum:
                  key = k
                  break
            print(key,end="")
            
        print("")    
        print("This is the Cipher Text") 

    #encryption()
    def decryption():
       message = input("Enter a message: ").upper().replace(" ","")
       print("Message: ",message)
       for x in message:
            
            key = None
            #print(x, end="")
            sum = (letters[x]-3)%26

            for k, v in letters.items():
               if  v == sum:
                  key = k
                  break
            print(key,end="")
            
       print("")    
       print("This is the Plain Text") 
    #decryption()
    k = True
    while k:
     choice=input("Encryption or Decryption: ").upper()
     if choice == "ENCRYPTION":
        encryption()
     elif choice == "DECRYPTION":
        decryption()
     elif choice == "QUIT":
        k=False
        print("Thank You")
        #break
     else:
        print("Error")

if __name__ == '__main__':
    main()