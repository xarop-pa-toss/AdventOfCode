local utils = {}

function utils.dumpTable(tabl)
   if type(tabl) == 'table' then
      local s = '{ \n'
      for k,v in pairs(tabl) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. utils.dumpTable(v) .. '\n'
      end
      return s .. '} '
   else
      return tostring(tabl)
   end
end

return utils
