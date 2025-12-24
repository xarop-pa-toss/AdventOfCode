
local Utils = require("./2025/utils")

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

local function leftSplitString(str)
    local strLen = string.len(str)
    if strLen <= 1 then
        return str
    end

    return string.sub(str, 0, string.len(str) / 2)
end

local function getLeftSplits(range)
    local dashIndex = string.find(range, '-')
    local rangeStart = string.sub(range, 0, dashIndex - 1)
    local rangeEnd = string.sub(range, dashIndex + 1, range.length)

    local startLeftSplit = leftSplitString(rangeStart)
    local endLeftSplit = leftSplitString(rangeEnd)
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

local function checkRange(range)
    for k, v in ipairs(range) do
        -- Instead of checking every single number, we start by getting the left 'half' of a number (12345678 would be 1234)
        -- Then we perform math to check if it would exist in the rest of the range by subtracting last number in range from duplicated number
        -- For example: in a range that ends at 88888888, the number 55923213 would become 5592. Then we do 88888888 - 55925592
        -- If that result < 0 then it has to exist

        
    end
end

local idsRaw = getIDsFromFile('./2025/Day2/Day2Data.txt')
local idsSplit = {}
for i, v in pairs(idsRaw) do
    table.insert(idsSplit, { getFullRange(v) })
end

for _, range in ipairs(idsSplit) do
    for _, inner in ipairs(range) do
        checkRange(inner)
    end
end

-- print(Utils.DumpTable(idsSplit));

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


