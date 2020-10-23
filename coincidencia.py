cadena = 'a44453'
patron.match(cadena)  # <_sre.SRE_Match object at 0x02303BF0>
patron.search(cadena) # <_sre.SRE_Match object at 0x02303C28>
cadena = 'ba3455' # la coincidencia no está al principio! 
patron.search(cadena)  #  <_sre.SRE_Match object at 0x02303BF0>
print patron.match(cadena) # None 