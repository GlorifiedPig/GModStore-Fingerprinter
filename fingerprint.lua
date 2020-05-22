
print( "Please input a folder name to convert." )

local folderName = io.read()

local function folderExists( file )
    local ok, err, code = os.rename(file, file)
    if not ok and code == 13 then
        return true
    end
    return ok, err
end

if not folderExists( folderName ) then print( "Folder does not exist." ) return end