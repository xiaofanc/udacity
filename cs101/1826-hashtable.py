# Define a procedure,

# hashtable_update(htable,key,value)

# that updates the value associated with key. If key is already in the
# table, change the value to the new value. Otherwise, add a new entry
# for the key and value.

# Hint: Use hashtable_lookup as a starting point.
# Make sure that you return the new htable

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key,value])

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    bucket.append([key,value])

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table



table = make_hashtable(5)
#print hash_string("word",5)
#print hashtable_get_bucket(table,"word")
hashtable_add(table,'Bill', 17)
print table
print hashtable_get_bucket(table,"Bill")
hashtable_add(table,'Bill', 23)
print table
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#[[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Bill', 23], ['Zoe', 14]], 
#[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]
print 
print hashtable_lookup(table,'Louis')
print hashtable_lookup(table,'Rochelle')
print 
hashtable_update(table, 'Bill', 42)
hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
print table
#[[['Ellis', 11], ['Francis', 13]], [['Zed', 68]], [['Bill', 42], ['Bill', 23], 
#['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 94]]]
