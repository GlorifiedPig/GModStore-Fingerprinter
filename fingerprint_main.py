
import fingerprint_functions

changed_lines = []

print( "Running fingerprinter..." )

fingerprint_functions.append_random_line_sha( "test.lua" )
fingerprint_functions.append_random_line_xor( "test.lua" )
print(changed_lines)