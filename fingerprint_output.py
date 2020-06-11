
import os

changed_lines = []

def changed_lines_to_file():
    with open( "output.txt", "w" ) as file:
        for changed_line in changed_lines:
            file.write( changed_line + "\n" )
    return changed_lines