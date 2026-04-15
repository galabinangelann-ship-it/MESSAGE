try:
    print("File Successfully Created.")
    with open("message.txt", "x") as file:
        file.write("====Message====")
        
    def send():
        with open("message.txt", "w") as file:
            usIn = input("Enter message to send: ")
            file.write(usIn + "\n")
            
    def view():
        with open("message.txt", "r") as file:
            print("====Message====")
            print(file.read())
            
    while True:
        print("Welcome to Messaging App")
        print("1. Send Message", "\n2. View Message", "\n3. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            
            if choice == 1:
                send()
                
            elif choice == 2:
                view()
                
            elif choice == 3:
                print("Message sent.")
                break 
            
            else:
                print("Enter only choices (1-3")
            
        except:
            print("Invalid. Please enter number only")
            
except:
    print("File already Exists.")
    