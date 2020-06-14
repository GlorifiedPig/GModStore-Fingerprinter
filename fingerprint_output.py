
import os
from os import path

import datetime

changed_lines = []

def changed_lines_to_file():
    
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    try:
        path.exists( "output.txt" )
    except FileNotFoundError:
        with open( "output.txt", "x" ) as file:
            string = "Created {0} fingerprints successfully at {1};\n".format( len( changed_lines ), date_time )
            
            for changed_line in changed_lines:
                string += "\n" + changed_line
            
            file.write( string )
            file.close()

            print( string )
    else:
        with open( "output.txt", "a" ) as file:
            string = "Created {0} fingerprints successfully at {1};\n".format( len( changed_lines ), date_time )
            
            for changed_line in changed_lines:
                string += "\n" + changed_line
            
            file.write( string )
            file.close()

            print( string )

    return changed_lines