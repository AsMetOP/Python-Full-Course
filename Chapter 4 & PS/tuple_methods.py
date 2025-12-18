my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2)) #gives total count

my_tuple1 = (1, 2, 3, 4, 2)
print(my_tuple1.index(2)) #as soon as it gets the matched values returns

#minimum value in the tuple
print(min(my_tuple), min(my_tuple1))
#maximum value in the tuple
print(max(my_tuple), max(my_tuple1))
#length of the tuple
print(len(my_tuple),len(my_tuple1))
#slicing
sliced = my_tuple[1:4]
print(sliced)
#unpacking tuples into vars
a,b,c,d,e = my_tuple1
print(a,b,c,d,e)