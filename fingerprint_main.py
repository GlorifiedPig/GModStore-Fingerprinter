
import fingerprint_functions, fingerprint_output



print( "Running fingerprinter..." )

fingerprint_functions.append_random_line_sha( "test.lua" )
fingerprint_functions.append_random_line_xor( "test.lua" )

fingerprint_output.changed_lines_to_file()