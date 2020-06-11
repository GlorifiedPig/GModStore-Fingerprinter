
import functions

changed_lines = []

print( "Running fingerprinter..." )

functions.append_random_line_sha( "test.lua" )
functions.append_random_line_xor( "test.lua" )
print(changed_lines)