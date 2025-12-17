local utils = {}

function DumpTable(tab)
   if type(tab) == 'table' then
      local s = '{ '
      for k,v in pairs(tab) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. DumpTable(v) .. ','
      end
      return s .. '} '
   else
      return tostring(tab)
   end
end

return utils