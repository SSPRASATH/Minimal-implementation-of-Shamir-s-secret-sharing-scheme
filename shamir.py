import random
import json
import os

banner =                                                                                            """                  
   SSSSSSSSSSSSSSS hhhhhhh                                                         iiii                     
 SS:::::::::::::::Sh:::::h                                                        i::::i                    
S:::::SSSSSS::::::Sh:::::h                                                         iiii                     
S:::::S     SSSSSSSh:::::h                                                                                  
S:::::S             h::::h hhhhh         aaaaaaaaaaaaa      mmmmmmm    mmmmmmm   iiiiiiirrrrr   rrrrrrrrr   
S:::::S             h::::hh:::::hhh      a::::::::::::a   mm:::::::m  m:::::::mm i:::::ir::::rrr:::::::::r  
 S::::SSSS          h::::::::::::::hh    aaaaaaaaa:::::a m::::::::::mm::::::::::m i::::ir:::::::::::::::::r 
  SS::::::SSSSS     h:::::::hhh::::::h            a::::a m::::::::::::::::::::::m i::::irr::::::rrrrr::::::r
    SSS::::::::SS   h::::::h   h::::::h    aaaaaaa:::::a m:::::mmm::::::mmm:::::m i::::i r:::::r     r:::::r
       SSSSSS::::S  h:::::h     h:::::h  aa::::::::::::a m::::m   m::::m   m::::m i::::i r:::::r     rrrrrrr
            S:::::S h:::::h     h:::::h a::::aaaa::::::a m::::m   m::::m   m::::m i::::i r:::::r            
            S:::::S h:::::h     h:::::ha::::a    a:::::a m::::m   m::::m   m::::m i::::i r:::::r            
SSSSSSS     S:::::S h:::::h     h:::::ha::::a    a:::::a m::::m   m::::m   m::::mi::::::ir:::::r            
S::::::SSSSSS:::::S h:::::h     h:::::ha:::::aaaa::::::a m::::m   m::::m   m::::mi::::::ir:::::r            
S:::::::::::::::SS  h:::::h     h:::::h a::::::::::aa:::am::::m   m::::m   m::::mi::::::ir:::::r            
 SSSSSSSSSSSSSSS    hhhhhhh     hhhhhhh  aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmmiiiiiiiirrrrrrr      Secret Sharing"""

#part 1 Shamir
def gen():
    file = open("./keyvalue.txt","a")
    key_value = {}
    Secret = 1234
    N = raw_input("Enter the Total number of shares >")
    for x in range(1,int(N)+1):
        result = 0
        for y in range(1,int(N)+1):
            a = random.randint(1,9999)
            result = result + a*pow(x,y)
        result = result +Secret
        kvalue ={x : result}
        key_value.update(kvalue)
    file.write(json.dumps(key_value))
    file.close
    print key_value

#part 2
def decrypt():
    N = raw_input("Enter the Total Number of share >")
    a =[]
    for c in range(int(N)):
        j = raw_input("Enter input >")
        a.append(j)
    res = []
    for x in range(int(N)):
        p = 1
        for y in range(int(N)):
            if x != y:
                k = int(a[y])/float(int(a[x]) - int(a[y]))
                p = p * k
        res.append(p)
    print res
    value =[]
    for o in range(int(N)):
        l = raw_input("enter the value ")
        value.append(l)
    sums = 0
    for r in range(int(N)):
        sec = float(res[r])*float(value[r])
        sums = sums+sec
    print int(sums)

if __name__ == "__main__":
    os.system('clear')
    print banner
    print ""
    print "----------------------------------------------------------------------------------------------------------------------   "
    print "OPTIONS"
    print "\n 1. CREATE SECRETE"
    print "\n 2. DECRYPT SECRETE"
    option = raw_input("\n Enter the option > ")
    if option == "1":
        gen()
    elif option == "2":
        decrypt()
    