# create an object called other_script with a type module
# a module is a file with python definitions and statements
import other_script as uf # 5
print(4)

# access obj in other_script
print(uf.num) # 12

# access function in other_script
scores = [23, 34, 89]
print("mean of scores: {}".format(uf.mean(scores)))

print(__name__)    # __main__
print(uf.__name__) # other_script
print(uf.main())

# The standard Library
# https://pymotw.com/3/
import math
print(math.factorial(4))

# Quiz: Password Generator
# Use an import statement at the top
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# print(word_list)
# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
import random
def generate_password():
    return "".join(random.sample(word_list, 3))
# or
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
# test your function
print(generate_password())

# useful modules in the standard library
# csv: very convenient for reading and writing csv files
# collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
# random: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
# string: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
# re: pattern-matching in strings via regular expressions
# math: some standard mathematical functions
# os: interacting with operating systems
# os.path: submodule of os for manipulating path names
# sys: work directly with the Python interpreter
# json: good for reading and writing json files (good for web work)

# Third-Party Libraries
# to install the third-party libraries:
# python3 -m pip install pytz 
# python3 -m pip install -r requirements.txt
from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone('Asia/Kolkata')

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)

# IPython - A better interactive Python interpreter
# requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
# Flask - a lightweight framework for making web applications and APIs.
# Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
# Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
# pytest - extends Python's builtin assertions and unittest module.
# PyYAML - For reading and writing YAML files.
# NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
# pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
# matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
# ggplot - Another 2D plotting library, based on R's ggplot2 library.
# Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
# pyglet - A cross-platform application framework intended for game development.
# Pygame - A set of Python modules designed for writing games.
# pytz - World Timezone Definitions for Python


