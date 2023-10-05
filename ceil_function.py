"""Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

Sample output
How many students on the course? 8
Desired group size? 4
Number of groups formed: 2

Sample output
How many students on the course? 11
Desired group size? 3
Number of groups formed: 4 """
students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
#number of 
full_groups = students // desired_group_size
"""if a//b  then (a+b-1) //b=a//b+(b-1)b
because a//b+b-1//b b-1//b=0
if a !// b 
a=cb+r
a+b-1=cb+r+b-1=cb+(r+b-1)
a//b+ int+b-1 then 2b>b-1>=b
c+b-1<2b
all devided by b
2>b-1/b >=1 
"""
full_groups += (students % desired_group_size + desired_group_size - 1) // desired_group_size
print(f"Number of groups formed: {full_groups}")