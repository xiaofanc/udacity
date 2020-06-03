List;
slicing;
in; not in; -> string
.append()
.pop() -> the last one
mutable;
ordered;

scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
scores[3] = "B"
print("scores: " + scores) -> ["B", "C", "A", "B", "B", "A"]
print("grades: " + grades) -> ["B", "C", "A", "B", "B", "A"]

print(sorted(scores, reverse = True))

name = ["A","B","C"]
print("-".join(name)) -> A-B-C (string)

Tuple;
immutable; - no add, remove, sort or replace
ordered;

dimensions = (52, 40, 100)
# tuple unpacking
length, width, height = dimensions
print("The dimensions are {}x{}x{}".format(length, width, height))

Set;
unordered;
mutable;
unique values;
in; not in;
.add()
.pop() -> random element since set is unordered!!!
set_example = {element1, element2, element3}
define a set: a = set()

dictionary;
mutable;
unordered;
Because these keys are used to index values, they must be unique and immutable.
Dictionary keys must be immutable: str, tuple, int, float...
in; -> check if a key in the dictionary
print("carbon" in elements)  -> True
get;
print(elements.get('dilithium')) -> None 
print(elements.get('dilithium', 0)) -> 0
identity: is / is not; (Equality: ==)
is_null = x is None
dict_example = {key1: value1, key2: value2, key3: value3}
define a dictionary: a = {} or a = dict()
# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())
# find the element with the highest count in the list of keys
max_dict = [[value, key] for key, value in verse_dict.items()]
print(max(max_dict)[1]) 


