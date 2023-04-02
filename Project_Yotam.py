import random
import cmath
from PIL import Image

#Send me comments - Email: yotamelharar13@gmail.com  

#------------Flags-------------

def flags(n): 
    print('\n---Flags--- ')
    if len(n)>1:
       if str(n[0])!=str(n[1]):
          print('Overflow - 1')
       else: print('Overflow - 0')
    if str(n).find('0')==-1:
        print('Zero - 1')
    else: print('Zero - 0')
    if str(n[0])=='1':
        print('Sign - 1')
    else: print('Sign - 0')
    if str(n).count('1')%2==0:
        print('Parity - 1')
    else: print('Parity - 0')

#-------Conversions functions--------

def check_bin(n): #check - Is binary number?
    c=set(n)
    d={'1','0'}
    if d==c or c=={'0'} or c=={'1'}:
        return True
    return False
    
def check_octal(n): #check - Is the number in octal base?
  for i in n:
    if int(i)>=8:
        return False
  return True

def check_hex(s): #check - Is the number in hexadecimal base?
   a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
   n=s.upper()
   count=0
   for i in n:
      for j in a:
         if i==j:
            count+=1
      if count==0:
         return False
      count=0
   return True

def bin_to_dec(n): #Convert binary to decimal
    l=len(n)
    sum=0
    for i in range(l):
        sum+=int(n[i])*2**(l-1-i)
    return sum

def dec_to_bin(n): #Convert decimal to binary
    s=''
    num=1
    while num!=0:
        num=int(n/2)
        s+=str(n-2*num)
        n=num
    return s[::-1]

def bin_to_octal(n): #Convert binary to octal
    l=len(n)
    j=0
    s=''
    for i in range(2):
        if l%3!=0:
            n='0'+n
            l=len(n)
        else: break
    for i in range(0,l,3):
        s+=str(bin_to_dec(n[i:i+3]))
    return s

def oct_to_bin(oct): #Convert octal to binary
    s0=''
    s=''
    n=str(oct)
    l=len(n)
    for i in range(l):
        s0=dec_to_bin(int(n[i]))
        for k in range(2):
          if len(s0)<3:
            s0='0'+s0
        s+=s0
    return s

def bin_to_hex(n): #Convert binary to hexadecimal
    l=len(n)
    s=''
    s0=''
    for i in range(4):
        if l%4!=0:
            n='0'+n
            l=len(n)
        else: break
    for i in range(0,l,4):
        s0=str(bin_to_dec(n[i:i+4]))
        if s0=='10':
            s0='A'
        elif s0=='11':
            s0='B'
        elif s0=='12':
            s0='C'
        elif s0=='13':
            s0='D'
        elif s0=='14':
            s0='E'
        elif s0=='15':
            s0='F'
        s+=s0
    return s

def hex_to_bin(h): #convert hexadecimal to binary
    n=h.upper()
    a=[]
    s=''
    st=''
    l=len(n)  
    for i in range(l):
        if n[i]=='A': #string is immuable
            a.append('10')
        elif n[i]=='B':
            a.append('11')
        elif n[i]=='C':
            a.append('12')
        elif n[i]=='D':
            a.append('13')
        elif n[i]=='E':
            a.append('14')
        elif n[i]=='F':
            a.append('15')
        else: a.append(n[i])
        st=dec_to_bin(int(a[i]))
        l1=len(st)
        if l1<4:
            for j in range(l1,4):
                st='0'+st
        s+=st
        st=''
    return s

#-------Operations functions--------

def b_and(x,y): #AND operation
    s=''
    l1=len(x)
    l2=len(y)
    if l1<l2:
        for i in range(l1,l2,1):
            x='0'+x
    elif l1>l2:
        for i in range(l2,l1,1):
            y='0'+y
    for i in range(l1):
        s+=str(int(x[i])*int(y[i]))
    return s

def logical_shift(n,b): #Logical shift operation, left and right.
    l=len(n)
    s=''
    if b==1: #left
      for i in range(1,l):
          s+=n[i]
      return s+'0'
    for i in range(0,l-1): #right
        s+=n[i]
    return '0'+s

def arithmetic_shift(n): #Arithmetic shift right operation
    l=len(n)
    s=n[0] #keeping the sign
    for i in range(l-1):
        s+=n[i]
    return s 

def circular_shift(n,b): #Circular shift operation, left and right.
    l=len(n)
    s=''
    if b==1: #left
       for i in range(1,l):
          s+=n[i]  
       return s+n[0]
    for i in range(0,l-1): #right
        s+=n[i]
    return n[l-1]+s

#-----------------------MAIN----------------------- 
#  
num=1
while num!=0:
    print('\n1.Conversions','\n2.Operations','\n3.Implementations','\n0.Exit')
    num=input('Hello, please type a number from the menu: ')
    if num.isdigit()==False:
        raise ValueError(f"'{num}' isn't an integer, Required an integer")
  
    elif num!='1' and num!='2' and num!='3' and num!='0':
        print('Input Error, try again')
        num=input('Hello, please type a number from the menu: ')
    num=int(num)


    #----------------Conversions-------------------

    if num==1:
         print('\n1.Binary to octal','\n2.Octal to binary','\n3.Binary to decimal','\n4.Decimal to binary','\n5.Binary to hexadecimal','\n6.Hexadecimal to binary')
         n=input('What type of convert would you like to do? ')
         if n.isdigit()==False:
             raise ValueError(f"'{n}' isn't an integer, Required an integer")
         n=int(n)

         if n==1: #bin_to_octal
             bin=input('\nEnter a binary number to convert to an octal number: ')
             if check_bin(bin)==False:
                 while check_bin(bin)==False:
                      print('Required a binary number, try again')
                      bin=input('\nEnter a binary number to convert to an octal number: ')
             print(bin_to_octal(bin))

         elif n==2: #octal_to_bin 
             oct=int(input('Enter an octal number to convert to a binary number: '))
             if check_octal(str(oct))==False:
                 print('Required an octal number (a number in base less than 8), try again')
                 oct=int(input('Enter an octal number to convert to a binary number: '))
             print(oct_to_bin(oct))

         elif n==3: #bin_to_dec
             b=input('\nEnter a binary number to convert to a decimal number: ')
             if check_bin(b)==False:
                 while check_bin(b)==False:
                      print('Required a binary number, try again')
                      b=input('\nEnter a binary number to convert to a decimal number: ')
             print(bin_to_dec(b))

         elif n==4: #dec_to_bin
             dec=int(input('\nEnter a decimal number to convert to a binary number: '))
             print(dec_to_bin(dec))

         elif n==5: #bin_to_hex
             bin=input('\nEnter a binary number to convert to a hexadecimal number: ')
             if check_bin(bin)==False:
                 while check_bin(bin)==False:
                      print('Required a binary number, try again')
                      bin=input('\nEnter a binary number to convert to a hexadecimal number: ')
             print(bin_to_hex(bin))

         elif n==6: #hex_to_bin
             hex=input('\nEnter a hexadecimal number to convert to a binary number: ')
             if check_hex(hex)==False:
                 while check_hex(hex)==False:
                     print('Required a hexadecimal number, try again')
                     hex=input('\nEnter a hexadecimal number to convert to a binary number: ')
             print(hex_to_bin(hex))

     #----------------Operations------------------- 
           
    if num==2:  
         print('\n1.AND','\n2.ADD','\n3.INC','\n4.DEC','\n5.DIVISION','\n6.MULTIPLY','\n7.SHIFT')
         n=input('What type of operation would you like to do? ')
         if n.isdigit()==False:
             raise ValueError(f"'{n}' isn't an integer, Required an integer")
         n=int(n)

         if n==1: #AND
             a=input('Enter the first binary number: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('\nEnter the first binary number: ')
             b=input('Enter the secound binary number: ')
             if check_bin(b)==False:
                 while check_bin(b)==False:
                      print('Required a binary number, try again')
                      b=input('\nEnter the secound binary number: ')
             print(a,' and ',b,'=',b_and(a,b))
             flags(b_and(a,b))

         elif n==2: #ADD
             a=input('Enter a binary number: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('\nEnter a binary number: ')
             b=bin_to_dec(a)
             c=input('Enter the binary number would you like to add: ')
             if check_bin(c)==False:
                 while check_bin(c)==False:
                      print('Required a binary number, try again')
                      c=input('\nEnter the binary number would you like to add: ')
             d=bin_to_dec(c)+b
             print(a,'+',c,'=',dec_to_bin(d))
             flags(dec_to_bin(d))

         elif n==3: #INC
             a=input('Enter a binary number would you like to increment: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('Enter a binary number would you like to increment: ')
             b=bin_to_dec(a)+1
             print(a,'+ 1 =',dec_to_bin(b))
             flags(dec_to_bin(b))

         elif n==4: #DEC
             a=input('Enter a binary number would you like to decrement: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('Enter a binary number would you like to decrement: ')
             b=bin_to_dec(a)-1
             print(a,'- 1 =',dec_to_bin(b))
             flags(dec_to_bin(b))

         elif n==5: #DIVISION
             a=input('Enter a binary divisible number: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('\nEnter a binary divisible number: ')
             b=bin_to_dec(a)
             c=input('Enter a binary dividing number: ')
             if check_bin(c)==False:
                 while check_bin(c)==False:
                      print('Required a binary number, try again')
                      c=input('\nEnter a binary dividing number: ')
             if c.find('1')==-1:
                 raise ZeroDivisionError('Cannot be divided by zero')
             d=int(b/bin_to_dec(c))
             print(a,'/',c,'=',dec_to_bin(d))
             flags(dec_to_bin(d))

         elif n==6: #MULTIPLY
             a=input('Enter the first binary number: ')
             if check_bin(a)==False:
                 while check_bin(a)==False:
                      print('Required a binary number, try again')
                      a=input('\nEnter the first binary number: ')
             b=bin_to_dec(a)
             c=input('Enter the second binary number: ')
             if check_bin(c)==False:
                 while check_bin(c)==False:
                      print('Required a binary number, try again')
                      c=input('\nEnter the second binary number: ')
             d=int(b*bin_to_dec(c))
             print(a,'*',c,'=',dec_to_bin(d))
             flags(dec_to_bin(d))

         elif n==7: #SHIFT
             print('1.Arithmetic shift','\n2.Logical shift','\n3.Circular shift')
             a=input('What shift would you like to do? ')
             while a!='1' and a!='2' and a!='3':
                 print('Input Error, try again')
                 a=input('What shift would you like to do? ')
             a=int(a)
             if a==1: #arithmetic shift
                print('\n1.A arithmetic shift left','\n2.A arithmetic shift right')
                b=input('Direction: ')
                while b!='1' and b!='2':
                     print('Input error, try again')
                     b=input('Direction: ')
                b=int(b)
                h=0
                c=input('Enter the binary number: ')
                if check_bin(c)==False:
                   while check_bin(c)==False:
                      print('Required a binary number, try again')
                      c=input('\nEnter the binary number: ')
                while h==0:
                    h=int(input('How many shifts? '))
                    if h==0: 
                        print(c)
                        break
                if b==1: #left
                    for i in range(1,h):
                       c=logical_shift(c,b) # = a logical shift left
                    s=logical_shift(c,b)
                    if s[0]!=s[1] and h!=0: #A left shift operation must be checked for the overflow
                        print(s,' There is an overflow')
                    elif h!=0: print(s) 
                elif b==2: #right
                    for i in range(1,h):
                        c=arithmetic_shift(c)
                    s=arithmetic_shift(c)
                    if h!=0: print(arithmetic_shift(c))

             elif a==2: #logical shift
                print('\n1.A logical shift left','\n2.A logical shift right')
                b=input('Direction: ')
                while b!='1' and b!='2':
                     print('Input error, try again')
                     b=input('Direction: ')
                b=int(b)
                h=0
                c=input('Enter the binary number: ')
                if check_bin(c)==False:
                   while check_bin(c)==False:
                      print('Required a binary number, try again')
                      c=input('\nEnter the binary number: ')
                while h==0:
                     h=input('How many shifts? ')
                     if h=='0': 
                        print(c)
                        break
                     elif h.isnumeric()==False:
                         print('Error, a number is required')
                         h=0
                h=int(h)
                for i in range(1,h):
                    c=logical_shift(c,b)
                if h!=0:
                    print(logical_shift(c,b))

             elif a==3: #circular shift
                  print('\n1.A left circular shift','\n2.A right circular shift')
                  b=input('Direction: ')
                  while b!='1' and b!='2':
                     print('Input error, try again')
                     b=input('Direction: ')
                  b=int(b)
                  h=0
                  c=input('Enter the binary number: ')
                  if check_bin(c)==False:
                     while check_bin(c)==False:
                       print('Required a binary number, try again')
                       c=input('\nEnter the binary number: ')
                  while h==0:
                     h=input('How many shifts? ')
                     if h=='0': 
                        print(c)
                        break
                     elif h.isnumeric()==False:
                         print('Error, a number is required')
                         h=0
                  h=int(h)
                  for i in range(1,h):
                      c=circular_shift(c,b)
                  if h!=0:
                      print(circular_shift(c,b))
     
     #----------------------Implementations-------------------------- 

    if num==3:
        print('\n1.Gates','\n2.Combinational circuits','\n3.Sequential circuits')
        n=input('What type of implement you would like to do? ')
        if n.isdigit()==False:
             raise ValueError(f"'{n}' isn't an integer, Required an integer")
        n=int(n)
        if n==1: #Gates
            print('\nAll gates using:','\n1.NAND gates','\n2.NOR gates')
            a=input('Select type of gate to implement: ')
            if a.isdigit()==False:
                raise ValueError(f"'{a}' isn't an integer, Required an integer")
            a=int(a)
            if a==1: 
                img=Image.open('ALLGATES_using_NAND.jpg')
                img.show()
            if a==2:
                img=Image.open('ALLGATES_using_NOR.jpg')
                img.show()

        elif n==2: #Combinational circuits
            print('\n1.Half Adder','\n2.Full Adder','\n3.Half Subtractor','\n4.Full Subtractor','\n5.Multiplexer','\n6.Demultiplexer','\n7.Decoder','\n8.Encoder')
            a=input('Select the combinational circuit to implement: ')
            if a.isdigit()==False:
                raise ValueError(f"'{a}' isn't an integer, Required an integer")
            a=int(a)

            if a==1: #Half Adder
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND gates','\n4.Decoder 2 to 4 & OR & NOT gates','\n5.MUX 2 & NOT gate','\n6.MUX 4')
                b=input('Select the relevant components: ')
                if b.isdigit()==False:
                    raise ValueError(f"'{b}' isn't an integer, Required an integer")
                b=int(b)
                if b==1:
                    img=Image.open('HA_using_NAND.jpg')
                    img.show()
                elif b==2:
                    img=Image.open('HA_using_NOR.jpg')
                    img.show()
                elif b==3:
                    img=Image.open('HA_using_XOR_AND.jpg')
                    img.show()
                elif b==4:
                    img=Image.open('HA_using_DEC2_4.jpg')
                    img.show()
                elif b==5:
                    img=Image.open('HA_using_MUX2.jpg')
                    img.show()
                elif b==6: 
                    img=Image.open('HA_using_MUX4.jpg')
                    img.show()

            if a==2: #Full Adder
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & OR gates','\n4.Half Adder & OR gate','\n5.MUX 4 ','\n6.DEMUX 8 & OR gate')
                b=input('Select the relevant components: ')
                if b.isdigit()==False:
                    raise ValueError(f"'{b}' isn't an integer, Required an integer")
                b=int(b)
                if b==1:
                    img=Image.open('FA_using_NAND.jpg')
                    img.show()
                elif b==2:
                    img=Image.open('FA_using_NOR.jpg')
                    img.show()
                elif b==3:
                    img=Image.open('FA_using_XOR_AND_OR.jpg')
                    img.show()
                elif b==4:
                    img=Image.open('FA_using_HA.jpg')
                    img.show()
                elif b==5:
                    img=Image.open('FA_using_MUX4.jpg')
                    img.show()
                elif b==6: 
                    img=Image.open('FA_using_DEMUX8.jpg')
                    img.show()

            if a==3: #Half Subtractor
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & NOT','\n4.MUX2')
                b=input('Select the relevant components: ')
                if b.isdigit()==False:
                    raise ValueError(f"'{b}' isn't an integer, Required an integer")
                b=int(b)
                if b==1:
                    img=Image.open('HS_using_NAND.jpg')
                    img.show()
                elif b==2:
                    img=Image.open('HS_using_NOR.jpg')
                    img.show()
                elif b==3:
                    img=Image.open('HS_using_XOR_AND_NOT.jpg')
                    img.show()
                elif b==4:
                    img=Image.open('HS_using_MUX2.jpg')
                    img.show()

            if a==4: #Full Subtractor
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & OR & NOT','\n4.Half Subtractor','\n5.DEMUX8','\n6.Decoder 3 to 8')
                b=input('Select the relevant components: ')
                if b.isdigit()==False:
                    raise ValueError(f"'{b}' isn't an integer, Required an integer")
                b=int(b)
                if b==1:
                    img=Image.open('FS_using_NAND.jpg')
                    img.show()
                elif b==2:
                    img=Image.open('FS_using_NOR.jpg') 
                    img.show()
                elif b==3:
                    img=Image.open('FS_using_XOR_AND_OR_NOT.jpg')
                    img.show()
                elif b==4:
                    img=Image.open('FS_using_HS.jpg')
                    img.show()
                elif b==5:
                    img=Image.open('FS_using_DEMUX8.jpg')
                    img.show()
                elif b==6:
                    img=Image.open('FS_using_DEC3_8.jpg')
                    img.show()

            if a==5: #MUX
                print('\n1.2 to 1','\n2.4 to 1','\n3.8 to 1','\n4.16 to 1','\n5.32 to 1')
                c=input('Select type of Multiplexer to implement ')
                if c.isdigit()==False:
                    raise ValueError(f"'{c}' isn't an integer, Required an integer")
                c=int(c)
                if c==1: #MUX2
                    print('\n1.NAND gates','\n2.AND & OR & NOT gates')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                       raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('MUX2_using_NAND.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('MUX2_using_AND_OR_NOT.jpg') 
                       img.show()
                if c==2: #MUX4
                    print('\n1.NAND gates','\n2.AND & OR & NOT gates','\n3.MUX2','\n4.Decoder 2 to 4')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('MUX4_using_NAND.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('MUX4_using_AND_OR_NOT.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('MUX4_using_MUX2.jpg') 
                       img.show()
                    elif b==4:
                       img=Image.open('MUX4_using_DEC2_4.jpg') 
                       img.show()
                if c==3: #MUX8
                    print('\n1.AND & OR & NOT gates','\n2.MUX2','\n3.MUX2 & MUX4','\n4.Decoder 3 to 8')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('MUX8_using_AND_OR_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('MUX8_using_MUX2.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('MUX8_using_MUX2_MUX4.jpg') 
                       img.show()
                    elif b==4:
                       img=Image.open('MUX8_using_DEC3_8.jpg') 
                       img.show()
                if c==4: #MUX16
                    print('\n1.AND & OR & NOT gates','\n2.MUX4','\n3.MUX2 & MUX8')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('MUX16_using_AND_OR_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('MUX16_using_MUX4.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('MUX16_using_MUX2_MUX8.jpg') 
                       img.show()
                if c==5: #MUX32
                    print('\n1.MUX8')
                    b=int(input('Select the relevant components: '))
                    if b==1:
                       img=Image.open('MUX32_using_MUX8.jpg')
                       img.show()

            if a==6: #DEMUX
                print('\n1.1 to 2','\n2.1 to 4','\n3.1 to 8','\n4.1 to 16')
                c=input('Select type of Demultiplexer to implement ')
                if c.isdigit()==False:
                        raise ValueError(f"'{c}' isn't an integer, Required an integer")
                c=int(c)
                if c==1: #DEMUX2
                    print('\n1.AND & NOT gates','\n2.NAND gates','\n3.NOR gates')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEMUX2_using_AND_NOT.jpg') 
                       img.show()
                    elif b==2:
                       img=Image.open('DEMUX2_using_NAND.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEMUX2_using_NOR.jpg') 
                       img.show()
                if c==2: #DEMUX4
                    print('\n1.NAND & NOT gates','\n2.AND & NOT gates','\n3.DEMUX2')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEMUX4_using_NAND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEMUX4_using_AND_NOT.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEMUX4_using_DEMUX2.jpg') 
                       img.show()
                if c==3: #DEMUX8
                    print('\n1.AND & NOT gates','\n2.DEMUX2','\n3.DEMUX4')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEMUX8_using_AND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEMUX8_using_DEMUX2.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEMUX8_using_DEMUX4.jpg') 
                       img.show()
                if c==4: #DEMUX16
                    print('\n1.AND & NOT gates','\n2.DEMUX4','\n3.DEMUX2 & DEMUX8')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEMUX16_using_AND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEMUX16_using_DEMUX4.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEMUX16_using_DEMUX2_DEMUX8.jpg') 
                       img.show()

            if a==7: #DECODER
                print('\n1.1 to 2','\n2.2 to 4','\n3.3 to 8','\n4.4 to 16')
                c=int(input('Select type of Decoder to implement: '))
                if c==1: #DECODER 1to2
                    print('\n1.AND & NOT gates','\n2.NAND gates')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEC1_2_using_AND_NOT.jpg') 
                       img.show()
                    elif b==2:
                       img=Image.open('DEC1_2_using_NAND.jpg') 
                       img.show()
                if c==2: #DECODER 2to4
                    print('\n1.AND & NOT gates','\n2.NAND gates','\n3.NOR','\n4.Decoder 1 to 2')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEC2_4_using_AND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEC2_4_using_NAND.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEC2_4_using_NOR.jpg') 
                       img.show()
                    elif b==4:
                       img=Image.open('DEC2_4_using_DEC1_2.jpg') 
                       img.show()
                if c==3: #DECODER 3to8
                    print('\n1.AND & NOT gates','\n2.NAND','\n3.Decoder 2 to 4')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEC3_8_using_AND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEC3_8_using_NAND.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEC3_8_using_DEC2_4.jpg') 
                       img.show()
                if c==4: #DEMUX 4to16
                    print('\n1.AND & NOT gates','\n2.Decoder 2 to 4','\n3.Decoder 3 to 8')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1:
                       img=Image.open('DEC4_16_using_AND_NOT.jpg')
                       img.show()
                    elif b==2:
                       img=Image.open('DEC4_16_using_DEC2_4.jpg') 
                       img.show()
                    elif b==3:
                       img=Image.open('DEC4_16_using_DEC3_8.jpg') 
                       img.show()

            if a==8: #ENCODER
                print('\n1.2 to 1','\n2.4 to 2','\n3.8 to 3','\n4.16 to 4','\n5.Priority','\n6.Decimal to BCD')
                c=int(input('Select type of Encoder to implement: '))
                if c==1: #ENCODER 2to1
                    img=Image.open('ENC2_1_using_OR_NOT.jpg')
                    img.show()
                if c==2: #ENCODER 4to2
                    img=Image.open('ENC4_2_using_OR.jpg')
                    img.show()
                if c==3: #ENCODER 8to3
                    img=Image.open('ENC8_3_using_OR.jpg')
                    img.show()
                if c==4: #ENCODER 16to4 
                    img=Image.open('ENCPR16_4_using_OR.jpg')
                    img.show()
                if c==5: #Priority encoder 
                    print('\n1.AND & OR & NOT gates','\n2.Priority 4 to 2')
                    b=input('Select the relevant components: ')
                    if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                    b=int(b)
                    if b==1: 
                        img=Image.open('ENCPR4_2_using_AND_OR_NOT.jpg')
                        img.show()
                    if b==2:
                        img=Image.open('ENCPR8_3_using_ENCPR4_2.jpg')
                        img.show()
                if c==6: #Decimal to BCD
                    img=Image.open('ENC_DEC_BCD_using_OR.jpg')
                    img.show()

        elif n==3: #Sequntial circuit
             print('\n1.Flip-flop','\n2.Binary counter','\n3.Frequency divider')
             a=input('Select the sequential circuit to implement: ')
             if a.isdigit()==False:
                raise ValueError(f"'{a}' isn't an integer, Required an integer")
             a=int(a)

             if a==1: #Flip Flop
                 print('\n1.D-FF','\n2.T-FF','\n3.SR-FF','\n4.JK-FF')
                 b=input('Select type of Flip-Flop to implement: ')
                 if b.isdigit()==False:
                        raise ValueError(f"'{b}' isn't an integer, Required an integer")
                 b=int(b)
                 if b==1: #D-FF
                     img=Image.open('D.jpg')
                     img.show()
                 elif b==2: #T-FF
                     img=Image.open('T.jpg')
                     img.show()
                 elif b==3: #SR-FF
                     img=Image.open('SR.jpg')
                     img.show()
                 elif b==4: #JK-FF
                     img=Image.open('JK.jpg')
                     img.show()

             elif a==2: #Binary counter
                 print('\n1.Synchronous','\n2.Asynchronous')
                 b=input('Select type of 4-Bit Binary Counter to implement: ')
                 if b.isdigit()==False:
                       raise ValueError(f"'{b}' isn't an integer, Required an integer")
                 b=int(b)
                 if b==1: #syn
                     img=Image.open('4bit_binary_counter.jpg')
                     img.show()
                 elif b==2: #asyn
                     img=Image.open('4bit_binary_counter_asyn.jpg')
                     img.show()

             elif a==3: #Frequency Divider
                 print('\n1.By even','\n2.By 3 33% D.C','\n3.By 3 50% D.C','\n4.By 3 50% D.C using NOR gates','\n5.By 5 50% D.C using NAND')
                 b=input('Select type of Frequency Divider to implement:  ')
                 if b.isdigit()==False:
                       raise ValueError(f"'{b}' isn't an integer, Required an integer")
                 b=int(b)
                 if b==1:
                     img=Image.open('FD_by_even.jpg')
                     img.show()
                 elif b==2:
                     img=Image.open('FD_by_3_33DC.jpg')
                     img.show()
                 elif b==3:
                     img=Image.open('FD_by_3_50DC.jpg')
                     img.show()
                 elif b==4:
                     img=Image.open('FD_by_3_NOR_50DC.jpg')
                     img.show()
                 elif b==5:
                     img=Image.open('FD_by_5_NAND_50DC.jpg')
                     img.show()