
for i in range(10, 0):
    print i



name1 = raw_input("First name")
name2 = raw_input("Last name")

array = []

array.append(name1)
array.append(name2)


weight = raw_input("Weight")

if weight > 200:
    print "OverWeight"
else:
    print "Perfect"


def area(l, w):
    area = l*w
    return area


length = int(raw_input("Lenght"))
width = int(raw_input("Width"))

# print area(length,width)

food = dict()
foods = {"1":'Pizza','2':'Hamburgers'}
selection = raw_input("Enter number 1 or 2")


print name1, name2, "weighed",weight, "lbs. The area of his house was ",area(length, width),"he liked ",foods[selection]


     




