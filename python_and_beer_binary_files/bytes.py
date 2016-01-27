from struct import unpack, calcsize

output = '{: <13}  {: >6} : {}'

raw = b'Python \xFF'


print(output.format('  ', 'char[]', raw))

for typ_desc, typ in (('int8', 'b'), ('uint8', 'B'), ('int16', 'h'), ('uint16', 'H'), ('int32', 'i'), ('uint32', 'I'), ('int64', 'q'), ('uint64', 'Q'), ('float', 'f'), ('double', 'd')):
    for endian_desc, endian in (('Little-Endian', '<'), ('Big-Endian', '>')):
        size = calcsize(typ)
        form = endian + str(8 // size) + typ
        print(output.format(endian_desc, typ_desc, unpack(form, raw)))
        
