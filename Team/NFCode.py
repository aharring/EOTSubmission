import re
# Regex module

with open ('Week07-access.log', 'r') as file:
# 'r' denotes read-only
    for line in file:            # Niall - it's case sensitive
        result = re.findall(r'(?:(GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH ) )(\S+)', line)
# I tried searching for sentence beginning with / but was un-successful.
# The alternative was to find any possibiliy of HTTP methods, of which there are 9.
# Not case sensitive
        print(result) # You need the print indented or it will only print the last result
