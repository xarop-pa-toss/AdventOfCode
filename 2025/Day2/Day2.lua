
local Utils = require("utils")

local function getFullRange(range)
    local dashIndex = string.find(range, '-')
    local rangeStart = string.sub(range, 0, dashIndex - 1)
    local rangeEnd = string.sub(range, dashIndex + 1, range.length)

    local fullRange = {}
    for i = 1, rangeEnd - rangeStart do
        fullRange[i] = rangeStart + i
    end

    print('Finished range '..rangeStart..' - '..rangeEnd)
    return fullRange
end

local function getIDsFromFile(path)
    local file = io.open(path)
    if file then
        local fileStr = file:read "*a"
        -- print(fileStr)

        local ids = {}
        for id in string.gmatch(fileStr, "[^,]+") do
            -- print(id)
            table.insert(ids, id)
        end
        file:close()

        return ids
    end
end

local idsRaw = getIDsFromFile('./Day2/Day2Data.txt')
local idsSplit = {}
for i, v in pairs(idsRaw) do
    table.insert(idsSplit, { getFullRange(v) })
end

print(Utils.DumpTable(idsSplit));

-- print(Utils.dumpTable(getIDsFromFile('./Day2Data.txt')))


-- if condition then
--     -- code
-- elseif condition then
--     -- code
-- else
--     -- code
-- end

-- for i = 1, 10 do
--     -- code
-- end

-- for i, v in ipairs(table) do
--     -- code
-- end

-- while condition do
--     -- code
-- end


