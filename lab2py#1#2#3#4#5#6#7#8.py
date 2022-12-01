# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:25:58 2022

@author: fawzia
"""
"""
1- create two lists then Iterate both lists simultaneously
"""
print('\n\n')
print("create two lists then Iterate both lists simultaneously::")
students = ['fawzia','ahmed', 'mohamed']
tracks   = ['AI', 'testing', 'Embaded']


for student, track in zip(students,tracks) :
    print(f"{student} study in {track}")


"""
2- Concatenate two lists index-wise 
	-> ['a','b'] , ['c','d']
	output - > ['ac' , 'bd']
""" 
print('\n\n')
print("Concatenate two lists index-wise::")
lst1= ['a','b','c','d']
lst2= ['b','c','d','e']
lst3=[]
for i in range(0,4,1):
    lst3.append(lst1[i]+lst2[i])
    
print(lst3) 



"""
3- Remove empty strings from the list of strings using filter function
"""
print('\n\n')
print("Remove empty strings from the list")
test_str = input("enter string with space::")
new_list = []
for x in test_str:
    if x != ' ':
        new_list.append(x)
print ("Modified list is : " + str(new_list))
        
        
"""
4- Compute avarge of row and column using function and select if user want row or column
"""
print("\n\n")
print("Compute avarge of row and column ::")
grades = [ [50, 33, 40, 30],
     [35, 50, 44, 17],
     [30, 35, 50, 37],
     [50, 35, 44, 22],
     [50, 44, 50, 30],
     [50, 36, 18, 50],
     [35, 30, 47, 16]  ]

def compute_row_avg(lst_of_lsts):
        col_avg = []
        for i in range(len(lst_of_lsts)):
            sum = 0
            for j in range(len(lst_of_lsts[i])):
                sum+= lst_of_lsts[i][j]
            col_avg.append(sum/len(lst_of_lsts[i]))
        return col_avg
    
    
    
def compute_col_avg(lst_of_lsts):
        col_avg = []
        for i in range(len(lst_of_lsts[0])):
            sum = 0
            for j in range(len(lst_of_lsts)):
                sum+= lst_of_lsts[j][i]
            col_avg.append(sum/len(lst_of_lsts))
        return col_avg
 
print("1- row:")
print("2- column:")
x=int(input("enter number of your choose:::>>>")) 
if x==1 :  
   print(compute_row_avg(grades))
elif x==2:    
   print(compute_col_avg(grades))


"""
5- create function take list and create new list check if it sublist from it or not
"""
print("\n\n")
print("check if it sublist from it or not::")
def check_sublist(_list,sublist):
    if sublist in _list:
        print('is sublist')
    else:
        print('is not sublist')

number = input("enter list:>")
sublist = input("enter sublist:>")
check_sublist(number, sublist)

 

"""
    
6- create function to check if string is Palindrom or not
	ex -> madam 
	      left = right
"""
print("\n\n")
print("string is Palindrom or not:::")
def palindrom(wd):
    if wd == wd[::-1]:
        print("this word is plaindrome")
    else:
        print("this word is not plaindrome")
        
wd=input("enter word:")  
palindrom(wd)      
    

"""
7- write program convert string to integer then multiplay this number *3
"""
print("\n\n")
print("convert string to integer then multiplay this number *3")
print ("multiplay this number *3:::>>>",int(input("enter number in string:"))*3)

"""

8- write program take a string then sepereate it with group 
	input ex-> aabcdde
	output ->  aa, aab, aabc, aabcdd, aabcdde
"""
print("\n\n")
print("take a string then sepereate it with group ")
_str=input("enter string:")
_list=[]
for i in range(1, len(_str), 1) :
       _list.append(_str[:i+1].lower() )
      

print(_list) 
    
  
    
          























    

