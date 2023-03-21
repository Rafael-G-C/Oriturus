## Oriturus: A python reference manager

To run Oriturus change the `path_to_file` and `name_of_file` in the Oriturus.py file
To write an ORDERED file change the `read_write` to a 1

**QUICK GUIDE**
```
!!tag>>long_name! << tag declaration

[tag.] << tag calling just the long name
long_name

[tag.REF] << tag calling the long name and the index of the ref
long_name1

[tag.REF,REF1] << tag calling the long name and the indices of the references belonging to the tag in order
long_name1,2

[REF1] << reference calling
[1]

[REF1,REF2] 
[1,2]

[REF1,REF2,REF3] << if at least three refs are consecutive oriturus will write a hyphen ("-")
[1-3]

!!ref_start! << this special tag tells oriturus where it should start reading the references
```

