#loop
for i in range(5):#counting down
    print "COUNT DOWN"
    print i
#end loop

name1 = raw_input("First name")
name2 = raw_input("Last name")


#array---
array = []

array.append(name1)
array.append(name2)
#pushing into the array

weight = raw_input("Weight")


#if statement
if weight > 200:
    print "OverWeight"
else:
    print "Perfect"
#end if

#function
def area(l, w):
    area = l*w
    return area

#end funciton
#length and width that will be pushed into the function
length = int(raw_input("Lenght"))
width = int(raw_input("Width"))


#dictionary
food = dict()
foods = {"1":'Pizza','2':'Hamburgers'}
selection = raw_input("Enter number 1 or 2")
#end dict

#printing the completed "madlib"
print name1, name2, "weighed",weight, "lbs. The area of his house was ",area(length, width),"he liked ",foods[selection]







