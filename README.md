
# 🐦 Oriturus: A Python reference manager and keyword parser

No special modules are needed to run Oriturus; everything works from the standard Python libraries.
Clone the repository and run `python3 main.py path/to/file`; you will see your ordered text displayed along with any errors found.

Oriturus can be run as a module by calling the Oriturus function, which returns
- The new text with the replaced tags and references as a list.
- A dictionary with all the tags and their respective tag object with its long name and indices
- A changes metadata dictionary that contains the lines that contained the tags, the lines that were swapped, the references found with their respective order, and any errors found. 

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

[REF1,REF2,REF3] << If at least three refs are consecutive, Oriturus will write a hyphen ("-").
[1-3]

!!ref_start! << This special tag tells Oriturus where it should start reading the references.
```
## Motivation
 I needed a LaTeX alternative with a simple keyword replacement for my bachelor's thesis and to write scientific articles. 
 Many people at the lab used different technologies, mainly Microsoft Word, which in itself did not provide a reference manager, and of course, every time an image/table/scheme/reaction was moved, the whole index was messed up.
With Oriturus, I was able to submit my part without having to worry if I wrote the name of the reaction correctly every time, and whenever everyone submitted their changes, I could merge them in a single file and have it be ordered.

## Future plans
- Integrate Jinja
- Write a user interface 

## Q&A 
Why return a text file?
- It's easier to edit, share, and append to other text editors.

Why not use something like Jinja?
- At the time of writing this a few years back, I did not know about Jinja, though it would come in really handy.

Why build it instead of using something?
- I would have had to learn how to use that particular tool; I already knew a bit of Python code, enough to make my own in a few weeks.

Why not use a database instead of an object?
- Also, at the time I did not know about database integration, though useful, now it could complicate the understanding for new Python users.
