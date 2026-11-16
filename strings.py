phrase = "Girl, you are amazing!"

print(phrase.upper())  # Output: GIRL, YOU ARE AMAZING!
print(phrase[0:5])     # Output: Girl,
print(phrase[0:7:2])  # Output: Gl y
 
print(phrase.replace("amazing" , "awesome"))  # Output: Girl, you are awesome!

print(phrase.isupper())  # Output: False
print(phrase.islower())  # Output: True