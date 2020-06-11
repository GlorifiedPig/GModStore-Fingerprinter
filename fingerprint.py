import io

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

with open( "test.lua" ) as file:
    lines = file.readlines()

file = open( "test.lua", "w" )
for lineKey, line in enumerate( lines ):
    lineKey = lineKey + 1
    print( lineKey )
    print( line )