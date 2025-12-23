#Control Statements:iteration purpuse
#Types:for loop and while loop
'''for loop syntax:
for var in seq:
    #Statements
seq:list,tuple,set,dict,str,range'''
# seq in list
''''l=['sai shree','sai swetha','vinod kumar', 'suma raj']
for name in l:
    print(name.title())'''
#----------------------------------------------
#tuple of items
'''l=['sai shree','sai swetha','vinod kumar', 'suma raj']
for name in l:
    print(name.titile())'''
#------------------------------------------------
#set of items
'''l={'sai shree','sai swetha','vinod kumar', 'suma raj'}
for name in l:
    print(name.title())'''
#---------------------------------------------------
#dictionary of items
'''products={
    'Airpods':3200,
    'Headset':4000,
    'Samrtwatch':12000,
    'Ipone':20000,
}
for i in products:
   print(f'{i}:${products[i]}')'''
 #----------------------------------------------------
'''s='Python Programming'
for i in s:
  print(i)'''
  #----------------------------------------------------
'''s='Python Programming'
vol='aeiouAEIOU'
for i in s:
    if i in vol:
        print (f'{i}--V)
    else:
        print(f'{i}**C')'''
 #-------------------------------------------------------
 #Range function:genarte numeric number fron one range to another range
for i in range(1,11):
    print(i)
 #----------------------------------------------------
 #genarete the table:
table=int(input('enter the table:'))
for i in range(1,21): 
    print(f'{table}*{i}={table*i}')
 #----------------------------------------------------