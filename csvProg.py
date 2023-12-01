r"""#What will be written inside the file test.csv using the following program import csv
import csv
D = [['Exam'],['Quarterly'],['Halfyearly']]

csv.register_dialect('M',lineterminator = '\n')

with open('File.csv', 'w') as f:

    wr = csv.writer(f,dialect='M')

    wr.writerows(D)

#f.close()
"""

#What is the output of the following program?
import csv
d=csv.reader(open('File.csv'))
next(d)

for row in d:
    print(row)
    
    
    
