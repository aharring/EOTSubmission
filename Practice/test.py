# Test print for approach Helen used

modules = {
    'courses':['math', 'english'],
    'grades' : [23, 64]
}

i = 0

for i in range (2):
    print ("Subject {} \t Grade {}\t" .format (modules['courses'][i], str(modules['grades'][i])))
    i+= 1
