To understand what yield does, you must understand what generators are. And before generators come iterables.

## Iterables

When you create a list, you can read its items one by one. Reading its items one by one is called iteration:

``` pyth
>>>  mylist = [1, 2, 3]
>>>  for i in mylist:
...    print(i)
1
2
3
```

## Generators

Generators are iterators, but you can only iterate over them once. 
It's because they do not store all the values in memory, they generate the values on the fly:

``` pyth
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4

```
## Yield

``` pyth
>>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

Yield is a keyword that is used like return, except the function will return a generator.

Here it's a useless example, but it's handy when you know your function will return a huge set of values that you will only need to read once.

To master yield, you must understand that when you call the function, the code you have written in the function body does not run. The function only returns the generator object, this is a bit tricky :-)

Then, your code will be run each time the for uses the generator.

Now the hard part:

The first time the for calls the generator object created from your function, it will run the code in your function from the beginning until it hits yield, then it'll return the first value of the loop. Then, each other call will run the loop you have written in the function one more time, and return the next value, until there is no value to return.

The generator is considered empty once the function runs but does not hit yield anymore. It can be because the loop had come to an end, or because you do not satisfy a "if/else" anymore.
