
import io, os, random, string, fingerprint_output

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

def append_line_sha( fileName, line ):
    sha_randomkey = randomString()
    fingerprint_output.changed_lines.append( "Line " + str( line ) + ": SHA256 Encrypted, Key '" + sha_randomkey + "'" )
    append_line( fileName, line, " -- {{ user_id sha256 " + sha_randomkey + " }}" )

def append_line_xor( fileName, line ):
    xor_randomkey = str( random.choice( range( 10, 100000 ) ) )
    fingerprint_output.changed_lines.append( "Line " + str( line ) + ": XOR Encrypted, Key '" + xor_randomkey + "'" )
    append_line( fileName, line, " -- {{ user_id | " + xor_randomkey + " }}" )

def append_random_line_sha( fileName ):
    with open( fileName, "r" ) as file:
        lines = file.readlines()
        randomInt = random.choice( range( 1, len( lines ) ) )
        append_line_sha( fileName, randomInt )

def append_random_line_xor( fileName ):
    with open( fileName, "r" ) as file:
        lines = file.readlines()
        randomInt = random.choice( range( 1, len( lines ) ) )
        append_line_xor( fileName, randomInt )