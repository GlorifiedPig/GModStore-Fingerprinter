
import os

changed_lines = []

def changed_lines_to_file():
    with open( "output.txt", "w" ) as file:
        file.write( str( changed_lines ) )
    return changed_lines