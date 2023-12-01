"""
# STACK OPERATIONS
string=input("Enter a string:")  # Palindrome
S=[]
top=None

def isEmpty(S):
  if  S==[]:
     return True
  else:
     return False
 
def Peek(S):
    if isEmpty(S):
       print( 'Underflow')
    else:
       top=len(S)-1
       print('topmost:', S[top])


def Push(S,X):
  if isFull(S):
       print( 'Overflow')
  else:
       #item=int(input('Enter Item:'))
       S.append(X)                           # Type C Q3. S.insert(0,item)
       top=len(S) - 1                        # Type C Q3. top=0
        
def isFull(S):
   if top==len(S) -1:
     return True
   else:
      return False
  
def Display(S):
    if isEmpty(S):
       print( 'Underflow')
    else:
       top=len(S)-1 
       print(S[top],'<=top')
       for i in range(top-1,-1,-1):
                print(S[i])
                
def  Pop(S):
   if isEmpty(S):
            print( 'Underflow')
   else:
     print('Item=',S.pop())              #Type C Q3. No need of isEmpty(S)
     if len(S) == 0:                      #  Type C Q3   print('Item=',S.pop(0))
        top=None
     else:
        top=len(S) - 1  

#while True:
    # print ('STACK        OPERATIONS\n1.Push \n 2.Pop \n 3. Peek \n 4. Display Stack \n 5. Exit \n')

     #ch=int( input ('Enter your choice(1-5) :') )
n=3
for i in range(len(string)):
        Push(S,string[i])      # S= [e,m,o,r,d,n,i,l,a,P,

for i in range(len(string)):
    Pop(S)


  if ch==1:
            Push(S)
     elif ch==2:
            Pop(S)
     elif ch==3:
            Peek(S)
     elif  ch==4:
            Display(S)
     elif  ch==5:
             break
     else:
           print('Invalid Choice')
           

# Reverse a string using stack

def Push(S,X):
  if isFull(S):
       print( 'Overflow')
  else:
       S.append(X)
       top=len(S) - 1  
        
def isFull(S):
   if top==len(S) -1:
     return True
   else:
      return False
    
def isEmpty(S):
  if  S==[]:
     return True
  else:
     return False

def  Pop(S):
   if isEmpty(S):
            print( 'Underflow')
   else:
     print('Item=',S.pop())
     if len(S) == 0:
        top=None
     else:
        top=len(S) - 1

 # __main__       
string=input("Enter a string:")  # Palindrome
S=[]
top=None

for i in range(len(string)):
        Push(S,string[i])     

for i in range(len(string)):
    Pop(S)




# Maintain Stack to perform Insert(push), delete(pop), display operation on it.
def Push(S,X):
  if isFull(S):
       print( 'Overflow')
  else:
       S.append(X)
       top=len(S) - 1  
        
def isFull(S):
   if top==len(S) -1:
     return True
   else:
      return False
    
def isEmpty(S):
  if  S==[]:
     return True
  else:
     return False

def  Pop(S):
   if isEmpty(S):
            print( 'Underflow')
   else:
     print('Item=',S.pop())
     if len(S) == 0:
        top=None
     else:
        top=len(S) - 1

def Display(S):
    if isEmpty(S):
       print( 'Underflow')
    else:
       top=len(S)-1 
       print(S[top],'<=top')
       for i in range(top-1,-1,-1):
                print(S[i])

 # __main__       
n=int(input("Enter a sno of students:") ) 
S=[]
top=None
while True:
     print ('STACK        OPERATIONS\n1.Push \n 2.Pop \n  3. Display Stack \n 4. Exit \n')
     ch=int( input ('Enter your choice(1-4) :') )
     if ch==1:
        for i in range(n):
              rno=int(input("enter rollno:"))
              name=input("name:")
              G=input("Gender:")
              Push(S,[rno,name,G])     
   elif ch==2:
        for i in range(n):
          Pop(S)
  elif ch==3:
        display(S)
  else:
      break










# QUEUE Operations
Q=[ ]  
front=rear=None

def isEmpty(Q):
  if  Q==[]:
     return True
  else:
     return False
def Peek(Q):
    if isEmpty(S):
       return 'Underflow'
    else:
       front=0
    print('topmost:', Q[front])


def Enqueue(Q):
  if isFull(S):
       return 'Overflow'
  else:
       item=int(input('Enter Item:'))
       Q.append(item)
       if len(Q) ==1:
          front=rear=0 
       else:
           rear=len(Q)-1
                  
def isFull(Q):
  if rear==len(Q) -1:
     return True
  else:
      return False
  
def Display(Q):
    if isEmpty(Q):
       return 'Underflow'
    else:
       front=0
       rear=len(Q)-1
       print(Q[0],'<=front')
       for i in range(1,rear):
                 print(Q[i])
    print(Q[len(Q)-1],'<=rear')

      

# Tyep C Q.5
Q=[]
front=0              # initially 0
rear=len(Q)-1    # initially -1

while True:
     print ('QUEUE  OPERATIONS\n1.Enqueue \n 2.Dequeue \n 3. Display Q status \n 4. Peek \n 5. Exit \n')
     ch=int( input ('Enter your choice(1-5) :') )
    
     if ch==1:
            item=int(input("Enter  item:"))
            Q.append(item)
            rear=len(Q)-1
            #Enqueue(Q)
     elif ch==2:
             if Q==[]:
                print("Underflow")
                front=0
             else:
                print('Deleted item=',Q.pop(0))
                print('Q is',Q)
            #Dequeue(Q)
     elif ch==3:
            print('Q is',Q)
            #Display(Q)
     elif ch==4:
          print('Item at front=',Q[front])
          #Peek(Q)
     elif ch==5:
         break
     else:
         print('Invalid Choice')


# Type C Q 8, QUEUE Operations
   
def Search(item,*args):
    


def Enqueue_H(Q,item):
  if isFull(Q):
       print( 'Overflow')
  else:
       Q.append(item)
       if len(Q) ==1:
          front=rear=0 
       else:
           rear=len(Q)-1

def Enqueue_N(Q,item):
  if isFull(Q):
       print( 'Overflow')
  else:
      
       Q.append(item)
       if len(Q) ==1:
          front=rear=0 
       else:
           rear=len(Q)-1
           
def Enqueue_L(Q,item):
  if isFull(Q):
       print( 'Overflow')
  else:
      
       Q.append(item)
       if len(Q) ==1:
          front=rear=0 
       else:
           rear=len(Q)-1
  
def Display(Q):
    if isEmpty(Q):
       return 'Underflow'
    else:
       front=0
       rear=len(Q)-1
       print(Q[0],'<=front')
       for i in range(1,rear):
                 print(Q[i])
    print(Q[len(Q)-1],'<=rear')
  
def  Dequeue(Q):
   if isEmpty(Q):
            return 'Underflow'
   else:
     print('Item=',Q.pop(0))
     if len(Q) == 0:
        front=rear=None

#__main__

HQ=[]
NQ=[]
LQ=[]
#front=rear=None
while True:
     print ('QUEUE  OPERATIONS\n1.Insert \n 2.Search for an element \n 3. Change the priority \n 4. Display Queue \n 5. Exit \n')
     ch=int( input ('Enter your choice(1-5) :') )
     if ch==1:
            ele=input('Enter Element to insert:')
            prio=input('Priority (Highest/Normal/Lowest(H/N/L)): ' )
            if  (prio=='H') :
                 HQ.append(ele)
            elif  (prio=='N') :
                 NQ.append(ele)
            elif  (prio=='L') :
                 LQ.append(ele)
            else:
                print('Invalid Priority')
     elif ch==2:
           ele=input('Enter Element to Search:')
           if  ele in HQ:
                print(ele,"found in HighestPr Queue")
           elif  ele in NQ:
                print(ele,"found in NormalPr Queue")
           elif  ele in LQ:
                print(ele,"found in LowestPr Queue")
           else:
                print(ele,"Not found in Any Queue")
     elif ch==3:
           ele=input('Enter Element to change priority:')
           newprio=input("Want to Increase/Decrease (I/D) Priority :") 
           if newprio=='I' :
               if  ele in HQ:
                    print(ele,"already in Highest Priority Queue")
               elif  ele in NQ:
                    HQ.append(ele)
                    NQ.remove(ele)
               elif  ele in LQ:
                     NQ.append(ele)
                     LQ.remove(ele)
           if newprio=='D' :
                if  ele in HQ:
                      NQ.append(ele)
                      HQ.remove(ele)
                elif  ele in NQ:
                      LQ.append(ele)
                      NQ.remove(ele)
                else:
                     if  ele in LQ:
                         print(ele,"already in Lowest Priority Queue")
     elif ch==4:
            print("HighestPr:",HQ)
            print("NormalPr:",NQ)
            print("LowestPr:",LQ)
     elif ch==5:
           break
     else:
           print('Invalid Choice')

#Type C Q. 4
Q=[]
front=0              # initially 0
rear=len(Q)-1    # initially -1

while True:
     print ('QUEUE  OPERATIONS\n1.Enqueue \n 2.Dequeue \n 3. Display Q status \n 4. Peek \n 5. Exit \n')
     ch=int( input ('Enter your choice(1-5) :') )
    
     if ch==1:
            item=int(input("Enter  item:"))
            Q.append(item)
            rear=len(Q)-1
           
     elif ch==2:
             if Q==[]:
                print("Underflow")
                front=0
             else:
                if len(Q)>1:
                  print('Deleted item=',Q.pop(front))
                  del Q[front]
                  print('Q is',Q)
                  front=front+1
                else:
                  print('Deleted item=',Q.pop(0))
                  print('Q is',Q)
                  front=0
     elif ch==3:
            print('Q is',Q)
           
     elif ch==4:
          print('Item at front=',Q[front])
         
     elif ch==5:
         break
     else:
         print('Invalid Choice')
"""

#Type C Q3. top should be at index 0
def isEmpty(S):
  if  S==[]:
     return True
  else:
     return False

def Push(S,X):
 
       S.insert(0,X)                           # Type C Q3. S.insert(0,item)
       top=0    

def  Pop(S):
   if isEmpty(S):
            print( 'Underflow')
   else:
     print('Item=',S.pop(0))              #Type C Q3. No need of isEmpty(S)
     if len(S) == 0:                      #  Type C Q3   print('Item=',S.pop(0))
        top=None
     else:
        top=0 

S=[]
top=None
while True:
     print ('STACK  OPERATIONS\n1.Push \n 2.Pop \n 3.Exit \n')

     ch=int( input ('Enter your choice(1-5) :') )
     if ch==1:
         item=int(input("enter:"))
         Push(S,item)
     elif ch==2:
         Pop(S)
     else:
          break
