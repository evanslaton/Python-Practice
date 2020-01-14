name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74
height_in_centimeters = height_in_inches * 2.54
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_centimeters} centimeters tall.")
print(f"He's {weight} pounds.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair..")
print(f"His teeth are usuall {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_in_centimeters + weight
print(f"If I add {age}, {height_in_centimeters}, and {weight} I get {total}.")