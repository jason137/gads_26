# welcome to data science at GA!

## anaconda installation 
- click here for installer (python3.4): http://continuum.io/downloads#py34 
- download installer, double-click .pkg file
- follow installation wizard

note that this installation edits your system search path (!) 
- `which python`
- look at your `~/.profile` file

if you don't like this, you can revert the change & create a separate shortcut
to anaconda 
- edit `~/.profile` 
- create a symbolic link with `ln` (`man ln` for help) 

## small-group questions

*1) define these statistical terms*  
- distribution
- quartile
- mean (or average)
- median
- mode
- standard deviation
- variance
- skew
- fat tails
- outlier 
- histogram
- scatterplot

*2) describe these distributions (bonus: using 1 word each!)*  
- normal distribution
- exponential distribution
- uniform distribution 

*3) take a look at one of the datasets in this repo*
- how is it delimited?
- what does it describe?
- what are some ways you could summarize this data?
- what are some empirical questions you could ask from this data?
- what are some questions you could ask from this data if given other data?

*4) what's the difference between an array and an associative array (bonus: use
O)? how are these implemented in python? what are some other fundamental python data 
structures?*

*5) define these python (more generally, computation) terms*  
- iterable
- immutable
- context manager
- lambda
- apply
- package
- namespace
- lazy evaluation 
- computational complexity

*6) how would you characterize the accuracy for each of targets below?*  
<img src="dartboards.png" align="middle", width=300>  

*7) use unix programs to perform the following tasks on one of the datasets in
this repo*
- print 10 first lines
- count number of lines
- print selected column/s
- count number of fields
- search for a pattern
- find/replace a pattern with regex
