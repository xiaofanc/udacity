# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

# check 1140

index = []

def add_to_index0(index,keyword,url):
    if not index:
        index.append([keyword,[url]])
    else:
        for i in range(len(index)):
            if keyword == index[i][0]:
                index[i][1].append(url)
                break
            else:
                index.append([keyword,[url]])
        return index

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            # if url not in keyword, then add;
            if not url in entry[1]:
                entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):
    for element in index:
        if keyword == element[0]:
            return element[1]
    return []

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []  # page which is crawled
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            # add index to each page based on the content
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(get_page(page))) # remove duplicates and merge two lists
            crawled.append(page)
    return index


add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']  
add_page_to_index(index,'fake.text',"This is a test")
print index
