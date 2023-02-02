my_tuple = ("boka", "doka", 'deka', 123.3)
print(type(my_tuple), my_tuple[2] )
print(my_tuple[:3])
change = list(my_tuple)
change[0] = "badBass"
my_tuple = tuple(change)
