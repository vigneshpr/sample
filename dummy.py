from name_revr import *

na()



''' 

def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b
divide(10,2)


   Here I make use of LIST for implementation.Here the address be the index values and the value be the actual data
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




from llist import dllist, dllistnode
lst1=[]
def create(size):
    size=size
    
    for i in range(0,size):
        lst1.append(raw_input("Enter value for {}\t:".format(i)))
    print lst1

        

def inser():
    print("---------------------------------------------------------------------------")
    print("Select Your Option:\n---------------------------------------------------------------------------")
    print("1.Insert at begin.|\t2.Insert at Last.|\t3.Insert in Between.\n---------------------------------------------------------------------------")
    lst = dllist(lst1)
    sam=int(raw_input("Enter your option:"))
    if(sam==1):
        a=input("Enter the Value to insert:")
        print("Before Insert:")
        lst.appendleft(a)
        print(lst)
        #dis()()
        #proceed()()
    elif(sam==2):
        a=input("Enter the Value to insert:")
        print("Before Insert:")        
        lst.appendright(a)
        print(lst)
            
        #dis()()
        #proceed()()
    elif(sam==3):
        b=input("Enter the position to insert:")
        a=input("Enter the Value to insert:")
        nod=lst.nodeat(b)
        print("Before Insert:")
        lst.insert(a,nod)
        print(lst)
        
        #print("After Insert:")
        #dis()()
        #proceed()()
    else:
        print("Invalid Option")
        #proceed()()

create(5)
inser()

 Sheet2 c RegNo Name    Team    Emailid Title 1 111713104001    ABHINAYA R  16  abhi13101.cs@rmkec.ac.in 2  111713104003    ABIRAMI B   16 abir13103.cs@rmkec.ac.in 3   111713104004    ABIRAMI G   16  abir13104.cs@rmkec.ac.in 4  111713104005    AISHWARYA S 12 aishu.koteeswaran@gmail.com 5    111713104008    AKSHAYA R   15  aksh13108.cs@rmkec.ac.in 6  111713104009    ALLWIN R    17 allw13109.cs@rmkec.ac.in 7   111713104013    ASHIKA S    15  ashi13113.cs@rmkec.ac.in 8  111713104015    ASVITHA JANANI S    11 asvithaj@gmail.com 9 111713104016    ASWINI A    11  aswi13116@rmkec.ac.in 10    111713104017    ATMAKURI SRINIVASA SAI SAKETH   19  Atma13117.cs@rmkec.ac.in 11 111713104018    BALAJI M    17  balajimvl@gmail.com 12  111713104019    BEN SHINY T 15  Shinyben10@gmail.com 13 111713104020    BHARGAV KOLLI   2   Bhargav.kolli@gmail.com 14  111713104022    BOLLA MARUTHI KUMAR 19  bollamaruthikumar@gmail.com 15  111713104023    CHANDRAGIRI RAVITEJA    19  Raviteja.chandragiri@gmail.com 16 111713104025  CHINNI MANIDEEP 17  mdeep385@gmail.com 17   111713104026    CHRISILLA V 12  chrisilla7@gmail.com 18 111713104027    DANDAMUDI AKHIL 18  akhil.dandamudi2@gmail.com 19   111713104028    DEVABATTINI SUSHMA  12 sushmadevabattini@gmail.com 20   111713104029    DHARANI MOZHI R 11  dharanimozhi@gmail.com 21   111713104031    DHIVYA K    15  dhivyakrishnamurthy5@gmail.com 22   111713104032    ELAKIA P S  13  pselakia@gmail.com 23   111713104039    INDHU S 13 indhusivakkumar@gmail.com 24 111713104042    JAYANTH KUMAR VARAM 1   Jayanthkmr717@gmail.com 25  111713104043 JAYASHREE G    14  jayashreemalini@gmail.com 26    111713104045    JAYASRI S   6   Sindhujaya333@gmail.com 27  111713104047 JEEVIDHA R 14  jeeviravi.janababu@gmail.com 28 111713104049    KANUMURU GOWTHAM VARMA  2   kanumurug@yahoo.com 29  111713104051    KAVERI G    5   Mgkaveri1994@gmail.com 30   111713104052    KEERTHANA S B   14  keerthusb@gmail.com 31 111713104053 KODALI AKHIL    18  Kodaliakhil118@gmail.com 32 111713104054    LAKSHMIPRIYA J  6   Jl.priya95@gmail.com 33 111713104058    MAHALAKSHMI D   6   Maha13218.cs@rmkec.ac.in 34 111713104060    MANDAVILLI SARVESWARA SRI HARSHA 18 Harshamandavilli786@gmail.com 35    111713104061    MEENA K 6   Meen13221.cs@rmkec.ac.in 36 111713104062    MEENA PRIYA A   20  meenapriya1151@gmail.com 37 111713104063    MEESALA SINDHU  4   meesalasindhu.96@gmail.com 38 111713104065  MOHAMMED SAYEED AHMED   19  sayeednote2@gmail.com 39    111713104066    MONICA SHREE S  20 monicashreesugumar@gmail.com 40  111713104067    MUDUNDI CHAITANYA VARMA 2   mcvbooogmail.com 41 111713104070 NALLAMOTHU DHARANI KRISHNA 4   dharani.n96@gmail.com 42    111713104071    NALLAMOTHU VARUN    1 Varunchowdary1996@gmail.com 43    111713104072    NANDHINI R  7   nandhiniravikumar41@gmail.com 44    111713104073 NANDHINI S 7   Nandhini1627@gmail.com 45   111713104078    NIROSHA S   7   Nirosha2395@gmail.com 46    111713104079 NIVEDHA M  20  nivedha.muralidharan@gmail.com 47   111713104080    NUVVURU VENKATA KALYAN KUMAR REDDY  1 Kalyan.nuvvuru@gmail.com 48   111713104083    PALAKOLANU CHARISHMA    10  Charishmareddy.172@gmail.com 49 111713104084    PALLAMPARTHI GEETHIKA REDDY 10  geethikareddypallamparthi@gmail.com 50  111713104086 PARVATHAREDDY SAITEJA  10  saitejaparvathareddy@gmail.com 51   111713104088    PODAPATI GEETANJALI 9 geethanjalipodapati@gmail.com 52  111713104089    POOJA N B   4   npoojabhaskar@gmail.com 53  111713104090 PRAKADHISVARI R K  4   prakadhiravi@gmail.com 54   111713104091    PRASANNA G  3   Prasanajake26@gmail.com 55 111713104098 REDDIVARI SOWMYA    8   sowmyareddivari@gmail.com 56    111713104100    SABIRA SHANAAZ K S  8 Shanaazshanu.ks@gmail.com 57  111713104102    SANDHIYA P  8   sandhiyapanneer1508@gmail.com 58    111713104103    SASI PRIYA C    8   sasipriyacg@gmail.com 59    111713104107    SRAVANTHI V M   10  sravanthivmurali@gmail.com 60   111713104111 TALLURI LEKHANA    9   tallurilekhana11@gmail.com 61   111713104117    VIJAY P 3   Vijaywatto95@gmail.com 62   111713104119 YASODA DEVARAJ 3   Devaraj.yasodha567@gmail.com 63 111713104308    R.LAKSHMI NARAYANAN 3   Rdilip95@gmail.com 64 111713104311  M.PRIYANKA  5   Priyabala426@gmail.com 65   111713104314    USHA S  5   Ushasree215@yahoo.com Sheet3 Status of Project  Status of SRS submission Team 1 Ms.S.Selvi 111713104042 JAYANTH KUMAR VARAM Not started Not submitted 111713104071  NALLAMOTHU VARUN 111713104080   NUVVURU VENKATA KALYAN KUMAR REDDY Team 2 Mr.D.Kirubakaran 111713104020 BHARGAV KOLLI   Not started Not submitted 111713104049  KANUMURU GOWTHAM VARMA 111713104067 MUDUNDI CHAITANYA VARMA Team 3 Ms.R.Bhavani 111713104091    PRASANNA G  Not started Not submitted 111713104117 VIJAY P 111713104119 YASODA DEVARAJ 111713104308 R.LAKSHMI NARAYANAN Team 4 Mr.B.Jaison 111713104063 MEESALA SINDHU  Not started Not submitted 111713104070  NALLAMOTHU DHARANI KRISHNA 111713104089 POOJA N B 111713104090  PRAKADHISVARI R K Team 5 Ms.M.Hemalatha 111713104051    KAVERI G    Not started Submitted 111713104311 M.PRIYANKA 111713104314  USHA S Team 6 Ms.R.Dhanalakshmi 111713104045    JAYASRI S   Only front end completed Oracle Resource person ask to include events and Database management   Submitted 111713104054  LAKSHMIPRIYA J 111713104058 MAHALAKSHMI D 111713104061  MEENA K Team 7 Ms.S.Radhika 111713104072    NANDHINI R  Not present Submitted 111713104073  NANDHINI S 111713104078 NIROSHA S Team 8 Ms.S.Srijayanthi Sheet4
'''