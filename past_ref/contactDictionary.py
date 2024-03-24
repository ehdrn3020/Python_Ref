class Contact:
    def __init__(self, name, pnum, email, addr):
        self.name = name
        self.pnum = pnum
        self.email =email
        self.addr = addr

def set_contact():
    name=input("Name: ")
    pnum = input("Pnum: ")
    email = input("Email: ")
    addr = input("Addr: ")
    f = open("./contact_db.txt","at")
    f.write(name+" ")
    f.write(pnum + " ")
    f.write(email + " ")
    f.write(addr+'\n')
    f.close()

def delect_contact(name):
    f=open("./contact_db.txt","rt")
    list = []
    for con in f:
        find = con.split(" ")
        if find[0] != name:
            list.append(con)
    f = open("./contact_db.txt", "wt")
    for i in list:
        f.write(i)
    f.close()

def read_contact():
    f = open("./contact_db.txt", "rt")
    for str in f:
        print(str)
    f.close()

def print_menu():
    print("1. store ")
    print("2. output ")
    print("3. delete ")
    print("4. exit ")
    menu = int(input("select MENU: "))
    return menu

def run():
    while 1:
        menu = print_menu()
        print(menu)
        if menu == 1:
            con = set_contact()
        elif menu == 2:
            read_contact()
        elif menu == 3:
            name = input("Name: ")
            delect_contact(name)
        elif menu == 4:
            break
        else :
            print("Wrong number")
            continue

if __name__ == "__main__":
    run()
