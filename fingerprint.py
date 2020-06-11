import io, os, random

def append_random_line( file_name, text ):
    with open( file_name ) as file: # Opens file
        lines = file.readlines()

        # Appends a new line to a random line
        randomInt = random.choice(range( 0, len( lines ) ) )
        
        line = str( lines[ randomInt ] )
        lines[ int( randomInt ) ] = line + text

        # Saves the changes
        out = open( file_name, 'w' )
        out.writelines( lines )
        out.close() # Closes the file

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

append_random_line( 'test.lua', '-- {user.id}' )