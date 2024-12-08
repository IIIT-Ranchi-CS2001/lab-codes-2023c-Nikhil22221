# 1. Find the number of palindrome words in the given sentence without defining any new function (feel free to use python’s in-built functions).
sentence= [x for x in input().split()]
count_palindrome=0
for word in sentence:
    rev_word = word[::-1]
    if word == rev_word:
        count_palindrome=count_palindrome+1

print(f"Number of palindromes : {count_palindrome}")

#2. Create a list of int using list comprehension [multiple input from keyboard].  
# Find the mean, median, and mode of the given list (usage of specific modules such as statistics is strictly prohibited. Lab problems are for you to build-up logic and strengthen your understanding of the topic & its concepts).
numbers=[int(x) for x in input().split()]
mean, median, mode = 0, 0, 0
numbers.sort()
sum_numbers = sum(numbers)
mean = sum_numbers / len(numbers)
print(f"Mean : {mean}")

if len(numbers) % 2 == 0:
    median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
else:
    median = numbers[len(numbers) // 2]

print(f"Median : {median}")

max_count = 0
for i in numbers:
    if numbers.count(i) > max_count:
        max_count = numbers.count(i)
        mode = i

print(f"Mode : {mode}")

# 3. Generate 2 lists (course code and course name). create a new list with both course code and name like["CS1001:Python",...]
l1 = ['CS2001', 'MA2001', 'CS2003', 'EC2001', 'EC2003']
l2 = ['Python Programming', 'Mathematics', 'Computer Organisation and Architechure', 'Analog and Linear IC', 'Circuit Analysis and Synthesis']
list_zipped = list(zip(l1, l2))
print(list_zipped)


# 4. Generate two sets – first for all singers and second for all dancers of the class using set comprehension. Perform set operations to generate the following sets of 
# a. all artists of the class
# b. allrounders of the class
# c. dancers but not singers
# d. singers but not dancers
# e. dancers but not singers cum singers but not dancers

singers = { x for x in input("Enter Singers").split()}
dancers = { x for x in input("Enter Dancers").split()}

print(f"All Artists : {singers | dancers}")
print(f"Alrounders : {singers & dancers}")
print(f"Singers only : {singers - dancers}")
print(f"Dancers only : {dancers - singers}")
print(f"Dancers but not Singers cum Singers but not Dancers: {singers ^ dancers}")