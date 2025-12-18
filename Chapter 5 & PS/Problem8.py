s = {8,7,12, "Asmet", [1,2]}

# The list [1, 2] is a mutable object, and Python does not allow mutable objects inside a set.
# When you try to execute s = {8, 7, 12, "Asmet", [1, 2]}, you’ll get a TypeError, because Python is trying to hash (make immutable) a list, but lists can change their contents.