# Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the Euclidean distance between the two.
tuple_one = tuple([int(x) for x in input().split()])
tuple_two = tuple([int(x) for x in input().split()])
dist=0
for i in range(3):
    dist = dist + (tuple_one[i] - tuple_two[i])**2
print(dist**0.5)

point_one = tuple([int(num) for num in input("Enter x1 and y1: ").split()])
point_two = tuple([int(num) for num in input("Enter x2 and y2: ").split()])

line_equation = f'(x-{point_one[0]}) = {(point_one[0] - point_two[0]) / (point_one[1] - point_two[1])}(y-{point_one[1]})'
print(line_equation)

#  WAP to count the number of each character present in a string using the concept of a dictionary.
sentence = input("Enter a sentence: ")
dict = {}
for i in sentence:
   dict[i] = dict.get(i,0) + 1
print(dict)

# Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. Construct a list of tuples with and without using built-in function zip().
customer_name = [x for x in input("Enter customer name: ").split()]
customer_id = [x for x in input("Enter customer id: ").split()]
shopping_point = [x for x in input("Enter shopping point: ").split()]


zipped_list = list(zip(customer_name,customer_id,shopping_point))
print(zipped_list)

new_list1=[]
for i in range (min(len(customer_id),len(customer_name),len(shopping_point))):
    tup = (customer_name[i],customer_id[i],shopping_point[i])
    new_list1.append(tup)

print(new_list1)

# Sort the list of tuples constructed above with and without sorted function
new_list2= sorted(new_list1,key = lambda x: x[1])
print(f"sorted using sorted fucntion {new_list2}")

for i in range(len(new_list1)):
    for j in range(i+1,len(new_list1)):
        if new_list1[i][1] > new_list1[j][1]:
            new_list1[i],new_list1[j] = new_list1[j],new_list1[i]

print(f"sorted using bubble sort {new_list1}")


# Enter the coordinates of two points on the cartesian plane. Find the equation of the straight line passing through these points.
# Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)
coord_one = tuple(map(int, input("Enter x1 and y1: ").split()))
coord_two = tuple(map(int, input("Enter x2 and y2: ").split()))
slope = (coord_one[0] - coord_two[0]) / (coord_one[1] - coord_two[1])
line_eq = f'(x-{coord_one[0]}) = {slope}(y-{coord_one[1]})'
print(line_eq)

