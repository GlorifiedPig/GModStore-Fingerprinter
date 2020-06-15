
import os

import fingerprint_functions, fingerprint_output

print("""
   _____ _            _  __ _          _   ______ _                                  _       _            
  / ____| |          (_)/ _(_)        | | |  ____(_)                                (_)     | |           
 | |  __| | ___  _ __ _| |_ _  ___  __| | | |__   _ _ __   __ _  ___ _ __ _ __  _ __ _ _ __ | |_ ___ _ __ 
 | | |_ | |/ _ \| '__| |  _| |/ _ \/ _` | |  __| | | '_ \ / _` |/ _ \ '__| '_ \| '__| | '_ \| __/ _ \ '__|
 | |__| | | (_) | |  | | | | |  __/ (_| | | |    | | | | | (_| |  __/ |  | |_) | |  | | | | | ||  __/ |   
  \_____|_|\___/|_|  |_|_| |_|\___|\__,_| |_|    |_|_| |_|\__, |\___|_|  | .__/|_|  |_|_| |_|\__\___|_|   
                                                           __/ |         | |                              
                                                          |___/          |_|                              

\nMelvin & GlorifiedPig © 2020\n""")
directory = input( "Enter a directory to run the fingerprinter on:\n" )

files = []
for r, d, f in os.walk(directory):
    for file in f:
        if '.lua' in file:
            files.append(os.path.join(r, file))

for f in files:
    fingerprint_output.changed_lines.append( "Affected file: " + f )
    fingerprint_functions.append_random_line_sha( f )
    fingerprint_functions.append_random_line_xor( f )


fingerprint_output.changed_lines_to_file()