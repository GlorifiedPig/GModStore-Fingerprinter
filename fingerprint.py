
import functions

changed_lines = []
# changed_lines.append( "Line " + str( line ) + ": SHA256 Encrypted, Key '" + sha_randomkey + "'" )
# changed_lines.append( "Line " + str( line ) + ": XOR Encrypted, Key '" + xor_randomkey + "'" )

print( "Running fingerprinter..." )

functions.append_random_line_sha( "test.lua" )
functions.append_random_line_xor( "test.lua" )
print(changed_lines)