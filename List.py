# Lists and lsitt methods

my_list = ['spam', 'eggs', 'bacon', 'sausage']

# check the length of a list
print(len(my_list))

# making a list with multi
print(['spam'] * 2)

# access values with numbers counting from 0 --out of bounds is an error
print(my_list[2])

print(dir(list))

#append = push
my_list.append('spam')

# this is unshift
# list.insert(index,item)
my_list.insert(0,'spam')

# remove last item
my_list.pop()

# remove finds a value and takes it out
my_list.remove('eggs')

# if 'eggs' in my_list:
#     my_list.remove('eggs')

# print(my_list.reverse())

# ## # ## # ## # ##
# string and list slicing

# this works on strings and lists
my_nums = [0,1,2,3,4,5,6,7,8,9]
# list/str[ start index: end index : steps]

# make copy of the list
print(my_nums[::])

# remove first thing in the list
print(my_nums[1::])

# omit colon for default step by 1
print(my_nums[1:3])

# every other item in the list
print(my_nums[::2]) # start at default, end at default, count by 2

# slice off the last
print(my_nums[len(my_nums) -1::])

# reverse with a step of -1
print(my_nums[::-1])