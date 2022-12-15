local name, id, outputDirectory = ...

local model = rbxassetid.read({
	AssetID = id,
	-- rbxm also decodes rbxmx.
	Format = "rbxm",
})

local decal = model:GetChildren()[1]
local textureURL = decal.Texture

local textureID = tonumber(string.match(textureURL.Value, "%d+$"))
if not textureID then
	error("texture ID not found")
end

local imageBytes = rbxassetid.read({
	AssetID = textureID,
	Format = "bin",
})

-- Match first few bytes to determine whether the file is PNG or a JPEG.
-- https://en.wikipedia.org/wiki/List_of_file_signatures
local extension
if string.match(imageBytes, "^\137\80\78\71\13\10\26\10") then
	extension = "png"
elseif string.match(imageBytes, "^\255\216\255\219") then
	extension = "jpg"
elseif string.match(imageBytes, "^\255\216\255\224\0\16\74\70\73\70\0\1") then
	extension = "jpg"
elseif string.match(imageBytes, "^\255\216\255\238") then
	extension = "jpg"
elseif string.match(imageBytes, "^\255\216\255\225..\69\120\105\102\0\0") then
	extension = "jpg"
elseif string.match(imageBytes, "^\255\216\255\224") then
	extension = "jpg"
else
	error("unknown image format")
end

local outputName = string.format(outputDirectory.."/"..name.."."..extension, textureID, extension)
fs.write(outputName, imageBytes, "bin")
