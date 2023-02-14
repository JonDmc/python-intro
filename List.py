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

print(my_list)