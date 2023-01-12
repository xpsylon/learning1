#set comprehension: same as list comprehension, just with curly instead of square brackets:
#{<expression> 'for' item 'in' set if <conditional>}

peruggia = {tito for tito in range(1, 5) if tito % 2 == 1}

#dictionary expressions: we have to input key=value pairs.

mataburros = {pim: pim ** 2 for pim in (2, 4, 6)}
#dict = {expresion 'for' item 'in' tuple}

