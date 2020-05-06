CAREFUL WITH THIS BUGS

[REF1][REF2] or [tag.REF1][tag.REF2]
will break the code because the program interprets it as REF1][REF2

[tag.REF1] [tag.REF2]
will write a space between the tags ex. Figure1 .1 

[REF1-REF3] [A] [B] [REF1-REF4]
will write [1-3] [4] [5] [1-6] because the index it uses to write new refs is global and so to the program REF4 is a totally new reference

