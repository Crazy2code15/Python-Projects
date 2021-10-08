Basic Python Interview Questions

<h4> Q1. What is the difference between list and tuples in Python? </h4>

LIST	
<ol>
  <li> Lists are mutable i.e they can be edited.</li>
  <li> Lists are slower than tuples. </li>
  <li> Syntax: list_1 = [10, ‘Chelsea’, 20] </li>
  </ol>
TUPLES
<ol>
  <li> Tuples are immutable (tuples are lists which can’t be edited).</li>
  <li>Tuples are faster than list.</li>
	<li>Syntax: tup_1 = (10, ‘Chelsea’ , 20)</li>
  </ol>

<h4> Q2. What are the key features of Python? </h4>
A2. <ul> 
  <li> Python is an interpreted language. That means that, unlike languages like C and its variants, Python does not need to be compiled before it is run. Other interpreted languages include PHP and Ruby.</li>
<li> Python is dynamically typed, this means that you don’t need to state the types of variables when you declare them or anything like that. You can do things like x=111 and then x="I'm a string" without erro.</li>
<li> Python is well suited to object orientated programming in that it allows the definition of classes along with composition and inheritance. Python does not have access specifiers (like C++’s public, private).</li>
<li> In Python, functions are first-class objects. This means that they can be assigned to variables, returned from other functions and passed into functions. Classes are also first class objects</li>
<li> Writing Python code is quick but running it is often slower than compiled languages. Fortunately，Python allows the inclusion of C-based extensions so bottlenecks can be optimized away and often are. The numpy package is a good example of this, it’s really quite quick because a lot of the number-crunching it does isn’t actually done by Python</li>
<li> Python finds use in many spheres – web applications, automation, scientific modeling, big data applications and many more. It’s also often used as “glue” code to get other languages and components to play nice.
</ul>

<h4> Q3. What type of language is python? Programming or scripting? </h4>
Ans: Python is capable of scripting, but in general sense, it is considered as a general-purpose programming language.

<h4> Q4.Python an interpreted language. Explain.</h4>
Ans: An interpreted language is any programming language which is not in machine-level code before runtime. Therefore, Python is an interpreted language.

<h4> Q5.What is pep 8?</h4> 
Ans: PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

<h4> Q6.What are the benefits of using Python?</h4>

Ans: The benefits of using python are-
<ol>
<li> Easy to use– Python is a high-level programming language that is easy to use, read, write and learn. </li> 
<li> Interpreted language– Since python is interpreted language, it executes the code line by line and stops if an error occurs in any line.</li>
<li> Dynamically typed– the developer does not assign data types to variables at the time of coding. It automatically gets assigned during execution.</li>
<li> Free and open source– Python is free to use and distribute. It is open source.</li>
<li> Extensive support for libraries– Python has vast libraries that contain almost any function needed. It also further provides the facility to import other packages using Python Package Manager(pip).</li>
<li> Portable– Python programs can run on any platform without requiring any change.</li>
<li> The data structures used in python are user friendly.</li>
<li> It provides more functionality with less coding.</li>
</ol>

<h4> Q7.What are Python namespaces? </h4>

Ans: A namespace in python refers to the name which is assigned to each object in python. The objects are variables and functions. As each object is created, its name along with space(the address of the outer function in which the object is), gets created. The namespaces are maintained in python like a dictionary where the key is the namespace and value is the address of the object. 

There 4 types of namespace in python-

Built-in namespace– These namespaces contain all the built in objects in python and are available whenever python is running.

Global namespace– These are namespaces for all the objects created at the level of the main program.

Enclosing namespaces– These namespaces are at the higher level or outer function.

Local namespaces– These namespaces are at the local or inner function.

<h4> Q8.What are decorators in Python?</h4> 

Ans: Decorators are used to add some design patterns to a function without changing its structure. Decorators generally are defined before the function they are enhancing. To apply a decorator we first define the decorator function. Then we write the function it is applied to and simply add the decorator function above the function it has to be applied to. For this, we use the @ symbol before the decorator.

<h4> Q9.What are Dict and List comprehensions?</h4> 

Ans: Dictionary and list comprehensions are just another concise way to define dictionaries and lists.

Example of list comprehension is-

x=[i for i in range(5)]

The above code creates a list as below-

4

[0,1,2,3,4]

Example of dictionary comprehension is-

x=[i : i+2 for i in range(5)]

The above code creates a list as below-

[0: 2, 1: 3, 2: 4, 3: 5, 4: 6]

<h4> Q10.What are the common built-in data types in Python?</h4>

Ans: The common built in data types in python are-

Numbers– They include integers, floating point numbers, and complex numbers. eg. 1, 7.9,3+4i

List– An ordered sequence of items is called a list. The elements of a list may belong to different data types. Eg. [5,’market’,2.4]

Tuple– It is also an ordered sequence of elements. Unlike lists , tuples are immutable, which means they can’t be changed. Eg. (3,’tool’,1)

String– A sequence of characters is called a string. They are declared within single or double quotes. Eg. “Sana”, ‘She is going to the market’, etc.

Set– Sets are a collection of unique items that are not in order. Eg. {7,6,8}

Dictionary– A dictionary stores values in key and value pairs where each value can be accessed through its key. The order of items is not important. Eg. {1:’apple’,2:’mango}

Boolean– There are 2 boolean values- True and False.

<h4> Q11.What is the difference between .py and .pyc files?</h4>

Ans: The .py files are the python source code files. While the .pyc files contain the bytecode of the python files. .pyc files are created when the code is imported from some other source. The interpreter converts the source .py files to .pyc files which helps by saving time.

<h4> Q12.What is slicing in Python?</h4>

Ans: Slicing is used to access parts of sequences like lists, tuples, and strings. The syntax of slicing is-[start:end:step]. 
The step can be omitted as well. When we write [start:end] this returns all the elements of the sequence from the start (inclusive) till the end-1 element. If the start or end element is negative i, it means the ith element from the end. The step indicates the jump or how many elements have to be skipped. 

Eg. if there is a list- [1,2,3,4,5,6,7,8]. Then [-1:2:2] will return elements starting from the last element till the third element by printing every second element.
i.e. [8,6,4].

<!--
Q13.What are Keywords in Python?

Ans: Keywords in python are reserved words that have special meaning.They are generally used to define type of variables. Keywords cannot be used for variable or function names. There are following 33 keywords in python-

And
Or
Not
If
Elif
Else
For
While
Break
 As
Def
Lambda
Pass
Return
True
False
Try
With
Assert
Class
Continue
Del
Except
Finally
From
Global
Import
In
Is
None
Nonlocal
Raise
Yield

Q14.What are Literals in Python and explain about different Literals

Ans: A literal in python source code represents a fixed value for primitive data types. There are 5 types of literals in python-

