valid=0
while True: 
        pas=input('Enter password:')
        if (len(pas)>=8 and ('@' in pas or '%' in pas or '$' in pas)):
            d=[0,1,2,3,4]
            count=0
            for i in d:
                if str(i) in pas:
                    count+=1
            else:
                if(count>0):
                    print('Valid password')
                    valid=1
        else:
            print('Password must be 8 characters long, at least one digit,and a special character(@or % or$)')
            print('Enter again')
            
        if(valid==1):
            break
            
print('success')