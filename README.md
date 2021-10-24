# CSE107 - Lab 9

This lab plays with opening files and handling exceptions that may 
be caused by this process.

## Purpose

### word_count.py

This program opens a file specified by the user and finds the 
number of occurrances of a string also specified by the user.

### simplediff.py

This program opens two files specified by the user and prints the 
differences found in the file line by line. It also indicates the
location of these differences with a carot symbol underneath the 
character

### readscores.py

This program opens a file called actsat.txt and reads the contents. 
It grabs the values separated by whitespace and places them in a 
dictionary.

## Conclusion

* In this lab I practiced opening files in different modes as well as
  handling exceptions the user may run into and giving useful error
  messages.
* Pair programming aided in giving me an outside look at my code
  and allowed me to ask questions and give help to my partner when
  it was needed.
* I did not work with my buddy on the lab.
* I did not have any problems while working on this lab aside from minor
  syntax errors which were easily fixed.
* I think I could improve the ways I find differences in [simplediff.py](#simplediffpy).
  I can make this better by checking for differences in a per word basis
  so that if a difference is found in the middle of a line it doesn't just 
  indicated the remainder of the offsetted line as different since it could 
  be the same. This issue can be recreated by adding a comma or extra 
  character in the middle of a line in one file and not the other file.