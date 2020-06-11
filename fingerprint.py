import io

# take biggest line in ALL files under folders
# add -- {{ user.id }}

print( "Running fingerprinter..." )

with open( "test.lua" ) as file:
    lines = file.readlines()

file = open( "test.lua", "w" )
for line in lines:
    # we need line and line number here
    # so we can append as seen in https://stackoverflow.com/questions/25822637/writing-to-the-end-of-specific-line-in-python
    print( line )