# Functions go here
def make_statement(statement, decoration, lines):
    ###Emphasises headings by adding decoration at the start and end###
    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)


    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)





# Main routine go here
make_statement(statement= "Programming is Fun!", decoration= "=", lines = 3)
print()
make_statement(statement= "Programming is Still Fun!", decoration= "*", lines = 2)
print()
make_statement(statement= "Emoji in Action", decoration= "🐍", lines = 1)