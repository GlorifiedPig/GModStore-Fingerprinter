
import io, os, random

def append_line( fileName, line, text ):
    line = line - 1
    lines = open( fileName, 'r' ).readlines()
    lines[line] = str( lines[line] )[:-1] + text + "\n"
    out = open( fileName, 'w' )
    out.writelines( lines )
    out.close()

def append_random_line( fileName, text ):
    with open( fileName ) as file:
        lines = file.readlines()
        randomInt = random.choice( range( 1, len( lines ) + 1 ) )
        append_line( fileName, randomInt, text )

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

append_line( "test.lua", 5, " -- {user.id}" )