
import io, os, random

def append_line( fileName, line, text ):
    line = line - 1
    lines = open( fileName, 'r' ).readlines()
    lines[line] = str( lines[line] )[:-1] + text + "\n"
    out = open( fileName, 'w' )
    out.writelines( lines )
    out.close()

def append_random_line( fileName, text ):
    with open( fileName, 'r' ) as file:
        lines = file.readlines()
        randomInt = random.choice( range( 1, len( lines ) ) )
        append_line( fileName, randomInt, text )

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

append_random_line( "test.lua", " -- {niggabyte?}" )