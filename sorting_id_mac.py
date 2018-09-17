import re
from prettytable import PrettyTable
x = PrettyTable(["id", "ethernet mac id","wifi mac id"])
test2=open('demotest.txt','r')
demotest=test2.readlines()

for i in demotest:
	a=str(i)
	b=a.split()
	x.add_row([b[0],b[1],b[2]])
print x
