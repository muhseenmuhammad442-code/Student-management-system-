students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. kara dalibi")
    print("2. rage dalibi")
    print("3. nemo dalibi")
    print("4. goge dalibi")
    print("5. fita")
    
    choice = input("zabi: ")
    
    if choice == "1":
        suna = input("shigar da sunan dalibi: ")
        maki = float(input("shigar da maki: "))
        
        students.append([suna, maki])
        
        print("an kara dalibi cikin nasara!")
        
    elif choice == "2":
        if len(students) == 0:
            print("babu dalibi cikin tsarin.")
        else:
            print("\njerin dalibai:")
            for student in students:
                print("suna:", student[0])
                print("maki:", student[1])
                print("--------------------")
                
    elif choice == "3":
        nema = input("shigar da sunan dalibi: ")
        an_samu = False
        
        for student in students:
            if student[0].lower() == nema.lower():
                print("\nAn samu dalibi!")
                print("suna:", student[0])
                print("maki:", student[1])
                an_samu = True
                break
            
            if not an_samu:
                print("ba a samu dalibin ba.")
                
    elif choice == "4":
        suna = input("shigar da sunan dalibin da za a goge: ")
        an_samu = False
        
        for student in students:
            if student[0].lower() == suna.lower():
                students.remove(student)
                print("an goge dalibi.")
                an_samu = True
                break
            
        if not an_samu:
            print("ba a samu dalibin ba.")
                
    elif choice == "5":
            print("sai anjima!")
            break
    else:
            print("zabi bai dace ba.")
        
else:
    print("ka zabi abin da bai dace ba.")