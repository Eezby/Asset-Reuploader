-- Download list of assets. Input is a file containing a list of asset IDs, one
-- per line. Output is a path to a directory.
--
-- Usage:
--     rbxmk run download-assets.lua INPUT OUTPUT
--
-- Example:
--     rbxmk run download-assets.lua assetList.txt assets

local assetIDs, outputDirectory = ...
fs.mkdir(outputDirectory, true)

local list = fs.read(assetIDs, "bin")
for id in string.gmatch(list, "[^\r\n]+") do
	id = tonumber(id)
	if id then
		local ok, data = pcall(rbxassetid.read, {
			AssetID = id,
			Format = "bin",
		})
		if not ok then
			print(string.format("download %10d: %s", id, data))
		else
			-- WARNING: May not actually be mp3.
			local file = path.join(outputDirectory, id .. ".mp3")
			local ok, err = pcall(fs.write, file, data, "bin")
			if not ok then
				print(string.format("write    %10d: %s", id, err))
			else
				print(string.format("ok       %10d", id))
			end
		end
	end
end