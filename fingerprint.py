
import io, os, random, string

changed_lines = []

def randomString( stringLength = 8 ):
    letters = string.ascii_lowercase
    return ''.join( random.choice( letters ) for i in range( stringLength ) )

def append_line( fileName, line, text ):
    line = line - 1
    lines = open( fileName, 'r' ).readlines()
    lines[line] = str( lines[line] )[:-1] + text + "\n"
    out = open( fileName, 'w' )
    out.writelines( lines )
    out.close()

def append_line_usersha( fileName, line ):
    sha_randomkey = randomString()
    changed_lines.append( "Line " + str( line ) + ": SHA256 Encrypted, Key '" + sha_randomkey + "'" )
    append_line( fileName, line, " -- {{ user_id sha256 " + sha_randomkey + " }}" )

def append_random_line_usersha( fileName ):
    with open( fileName, 'r' ) as file:
        lines = file.readlines()
        randomInt = random.choice( range( 1, len( lines ) ) )
        append_line_usersha( fileName, randomInt )

print( "Running fingerprinter..." )

append_random_line_usersha( "test.lua" )
print(changed_lines)