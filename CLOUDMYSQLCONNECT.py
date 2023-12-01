"""
import mysql.connector as C
CON=C.connect(host='sql6.freemysqlhosting.net',user='sql6431189',passwd='DGK7qJ8gsG',database='sql6431189')
if CON.is_connected():
    print("success")
    cursor=CON.cursor()
    #cursor.execute("CREATE TABLE SUBJECT( SCODE char(2) ,SNAME char(30),PRIMARY KEY (SCODE,SNAME))")
    cursor.execute("INSERT INTO SUBJECT  values('S1','Physics'),('S3','Chemistry')")
    CON.commit()
    cursor.execute("select * from SUBJECT")
    rows=cursor.fetchall()
    print('#'*30)
    print('**************MENU**************')
    for i in rows:
         print(i)
    print('#'*30)
    CON.close()
    
else:
    print("un successful")
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
A=np.arange(2,20,2)
'''B=np.log(A)
plt.plot(A*1.2,B)
plt.plot(A,B)

plt.show()

S=pd.Series(A,index=['i','ii','iii','iv','v','vi','vii','viii','ix'])
for l,v in S.iteritems():
    print(l,'-',v)
    S.at[l]=v*2
print(S)'''
G=pd.DataFrame()
print(G)
G=pd.DataFrame(columns=['p','q','r'])
print(G)
G=pd.DataFrame(dict())
print(G)
# Define a dictionary containing employee data
#data = {'Age':[27, 14, 12, 32,42,35,23,12,11,10,5,17,18,19,21,23,27,32,33,30],
#        'Rank':[1,2,4,5,3,2,4,6,7,3,7,8,2,4,4,8,9,7,9,8] }
#df = pd.DataFrame(data)
#df.plot(kind='hist',bins=5)
# Convert the dictionary into DataFrame 

#df.plot(kind='hist',y='Age')

#df['Age'].plot.hist(histtype='step')
#plt.hist(df.Age)
