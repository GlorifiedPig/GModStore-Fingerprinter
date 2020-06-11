import io

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

with open( 'test.lua', 'a' ) as file:
    file.write( '\n-- {user.id}\n' )