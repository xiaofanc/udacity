# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.


def remove_tags(string):
    start_point = string.find("<")
    while start_point != -1:
        end_point = string.find(">", start_point)
        string = string[:start_point] + " " + string[end_point+1 : ]
        start_point = string.find("<")
    return string.split()
    
"""   
def remove_tags(string):
    end_point = 0
    res = []
    while end_point< len(string):
        substring, end_point = find_next(string, end_point)
        res.append(substring)
    return res
    
    
def find_next(string, end_point):
    start_point = string.find(">", end_point)
    end_point = string.find("<", start_point)
    return string[start_point+1: end_point], end_point
"""

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']