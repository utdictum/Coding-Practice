""""Seitsemän veljestä" is one of the first novels ever written in Finnish. It is the story of seven orphaned brothers learning to make their way in the world (read more on Wikipedia).

This program is supposed to print out the names of the brothers in alphabetical order, but it's not working quite right yet. Please fix the program so that the names are printed in the correct order.

print("Simeoni")
print("Juhani")
print("Eero")
print("Lauri")
print("Aapo")
print("Tuomas")
print("Timo")"""

def print_ordered_strings(strings): 
    for a in sorted(strings):
        print(a)

strings= ["Simeoni","Juhani","Eero","Lauri","Aapo","Tuomas","Timo"]
print_ordered_strings(strings)