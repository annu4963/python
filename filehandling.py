# handle=open('students.txt','w')
# handle.write('annu')

# handle=open('students.txt','a')
# handle.write('\nram')
# handle.write('\nhari')
# handle.close()

with open('students.txt','r') as  handle
    data=[]
    for line in handle:
        data.append(line.split(''))
    print(data)