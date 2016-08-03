from llist import dllist, dllistnode
import time
base_ls=[1,2,3,4,5,6]
lst=dllist(base_ls)
nod=lst.first
def dis():
    if(len(base_ls)==0):
        print("Empty Linked_list")
        proceed()
    else:
        print("Display Linked_list")
        for i in range(len(base_ls)):
            print("Key-->",i,"Value-->",base_ls[i])
        print(lst)
        proceed()
def inser():
    print("---------------------------------------------------------------------------")
    print("Select Your Option:\n---------------------------------------------------------------------------")
    print("1.Insert at begin.|\t2.Insert at Last.|\t3.Insert in Between.\n---------------------------------------------------------------------------")
    sam=int(raw_input("Enter your option:"))
    if(sam==1):
        a=input("Enter the Value to insert:")
        print("Before Insert:",lst)
        lst.appendleft(a)
        
        print("After Insert:",lst)
        proceed()
    elif(sam==2):
        a=input("Enter the Value to insert:")
        print("Before Insert:",lst)
        lst.appendright(a)
        
        print("After Insert:",lst)
        proceed()
    elif(sam==3):
        print(base_ls)
        b=input("Enter the position to insert:")
        a=input("Enter the Value to insert:")
        print("Before Insert:",base_ls)
        lst.insert(b,a)
        
        print("After Insert:",lst)
        proceed()
    else:
        print("Invalid Option")
        proceed()
def rem():
    print("---------------------------------------------------------------------------")
    print("Select Your Option:\n---------------------------------------------------------------------------")
    print("1.Delete at begin.|\t2.Delete at Last.|\t3.Delete in Between.\n---------------------------------------------------------------------------")
    sam=int(raw_input("Enter your option:"))
    if(sam==1):
        print("Before Insert:",lst)
        lst.popleft()
        
        print("After Insert:",(lst))
        proceed()
    elif(sam==2):
        print("Before Delete:",lst)
        lst.popright()
        
        print("After Delete:",(lst))
        proceed()
    elif(sam==3):
        
        a=input("Enter the Key_value Value to Delete:")
        node = lst.nodeat(a)
        print("Before Delete:",lst)
        lst.remove(node)
        
        print("After Delete:",lst)
        proceed()
    else:
        print("Invalid Option")
        proceed()
def disp():
    print("-------------------------Single Linked List--------------------------------")
    
    print("Select Your Option:\n---------------------------------------------------------------------------")
    
    print("1.Display List.|\t2.Insertion Operation.|\t3.Deletion Operation.\n---------------------------------------------------------------------------")
    
    opt=int(input("Enter a Option:"))
    if(opt==1):
        dis()
    elif(opt==2):
        inser()
    elif(opt==3):
        rem()
    else:
        print("Invalid Option")
        proceed()

def proceed():
    try:
        st=str(input("Want to Continue (y or n):"))
        if((st=='y') | (st=='Y')):
            disp()
        else:
    
            print("\nExiting!!!!!!!!\n")
            exit()
    except:
        proceed()
disp()

