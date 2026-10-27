
# name = "shashi"  #str
# age = 29   #int
# experience = 4.3   #float
# Information = True   #bool


# scores = [90, 80, 70, 60]   #list, orderd and changeable(multiple data types, mutable)
# points = (10, 20, 30, 40)   #tuple, ordered and unchangeable(multiple data types, immutable)
# user = {"name": "shashi", "age": 29, "experience": 4.3}   #dict, unordered and changeable(multiple data types, mutable)
# tags = {"python", "java", "c++"}   #set, unordered and unchangeable(multiple data types, immutable), inique values


# squares = [x * x for x in range(4)]

# print(squares)


def average(values: list[int]) -> int:
    """Return the mean of a non-empty list."""
    return sum(values) / len(values)
print(average([2, 2, 2, 2, 2]))
        
    
        