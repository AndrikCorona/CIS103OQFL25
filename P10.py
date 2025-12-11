thetext = '''Python was conceived in the late 1980's by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
as a hobby project for Van Rossum to keep him occupied over 
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python's Flying Circus, and
Rossum used letters of code often in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this 
language to support both front-end and back-end functionality.'''

print(thetext)
print("Original Length:", len(thetext))

thetext = thetext.strip()
print("New Length after strip:", len(thetext))

the_count = thetext.lower().count('the')
print("Count of 'the':", the_count)

if 'little' in thetext.lower():
    print("The word 'little' was found.")
else:
    print("The word 'little' was not found.")

if 'titan' in thetext.lower():
    print("The word 'titan' was found.")
else:
    print("The word 'titan' was not found.")

position = thetext.find('appl')
print("Position of 'appl':", position)

thetext2 = thetext
thetext2 = thetext2.replace('Python', 'PYTHON')

print(thetext2)
