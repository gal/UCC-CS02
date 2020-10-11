<details>
<summary>Table of Content</summary>
<!-- TOC -->

- [CS2513 Week 1](#cs2513-week-1)
  - [Module Contents](#module-contents)
  - [Object Oriented Programming](#object-oriented-programming)
    - [Advantages of OOP](#advantages-of-oop)
    - [Disadvantages of OOP](#disadvantages-of-oop)
    - [Procedural Oriented Programming vs Object Oriented Programming](#procedural-oriented-programming-vs-object-oriented-programming)
    - [Features of OOP](#features-of-oop)
  - [The Abstract Data Type (ADT)](#the-abstract-data-type-adt)
    - [Data Structure Key Points](#data-structure-key-points)
    - [Abstract Data Type Key Points](#abstract-data-type-key-points)
      - [The Two Parts of an ADT](#the-two-parts-of-an-adt)
      - [Advantages of an ADT](#advantages-of-an-adt)
  - [The Formal Concepts in OOP](#the-formal-concepts-in-oop)
  - [Python vs Purely Object Oriented Languages](#python-vs-purely-object-oriented-languages)
- [CS2513 Week 2](#cs2513-week-2)
  - [Encapsulation](#encapsulation)
    - [What is a Class](#what-is-a-class)
    - [What is an Object](#what-is-an-object)
  - [Our First Class](#our-first-class)
      - [Destruction](#destruction)
      - [Instantiation](#instantiation)
      - [Default Constructors](#default-constructors)
    - [The Constructor](#the-constructor)
      - [Instantiating Objects with **\_\_init\_\_**](#instantiating-objects-with-__init__)
    - [Self](#self)
  - [Abstraction](#abstraction)
    - [Scope of Data](#scope-of-data)

</details>

---

# CS2513 Week 1

## Module Contents

- **Object Oriented Programming** (OOP)
- How do we leverage (**reuse**, **extend**, **interact**) with others code
- How do we **package code** so others can use it
- How do we **produce code** so that it is **easily maintained**
- How to create **libraries** of code for yourself and others while ensuring it works **correctly** and **robustly**
- How do we organise **large projects** and allow **several teammates** to work together

---

## Object Oriented Programming

- Seeks to define a program in terms of the _things_ in the problem (files, molecules, buildings, cars, people, etc.) as a **class**

  - What each class needs
  - What each class can do

- OOP is a **Programming Paradigm** focused of modeling your problem as objects, object attributes and object actions
  - Previously we have been thought **Procedural Programming**
- e.g. The **ball** _bounced_, The **coffee** was _poured_, The **car** got _dirty_

<br>

### Advantages of OOP

- Allows parallel code development for groups of developers
- Helps us write cleaner code that has fewer errors
  - And when errors do occur they are easier to fix
- Helps us to reuse code
- Allows us to use related code organisation and design techniques

- **Advantages from an Industry Perspective**

  - Consider the costs involved in developing a large software project
    - Building and Fittings
    - Equipment
    - Utilities
    - Developers

### Disadvantages of OOP

- As an individual, it can be difficult to see the advantages of OOP
- There is more code with OOP, and OOP Design takes more effort
  - Not ideal for prototyping or developing a one off project
- **Note** - Not all code in python you write needs to be OOP

<br>

### Procedural Oriented Programming vs Object Oriented Programming

- **Procedural Programming** creates a step by step program that guides the application through a sequence of instructions
  - Each instruction is executed in order
- **Procedural Programming** also focuses on the idea that all algorithms are executed with functions and data that the programmer has access to/is able to interact with
- **OOP** is much more similar to the way the real-world works
  - Each program is made up of many entities called **objects**
- In **OOP** a message must be sent requesting the data
  - Just like people must ask one another for information, we cannot see inside eachothers heads

<br>

### Features of OOP

- Ability to simulate the real world events much more effectively
- The code is reuseable so less code needs to be written over time
- Data becomes active
- Better able to create GUI applications
- Programmers can write faster, more accurate and better written applications

---

## The Abstract Data Type (ADT)

1. **Constant/Variable** - Uses a Storage location paired with an associated symbolic name, containing some value

   - **Constant** - Information that is **known** and **fixed**
   - **Variable** - Information that is **know** or **unknown** but is **dynamic**

2. **Datatype** - Classification to identify one of various types of data

   - The possible values this type can take
   - The operations that can be done with the values of this type
   - The meaning of the data and the way values of that type can be stored

   - **Example**:
     - The value set of the **Boolean** datatype is **true** and **false**
     - The **Boolean** type supports most logical operations
       - **&&**
       - **||**
       - **!**
     - The **Boolean** data represents a logical statement and it can be stored in a computers memory with the values **0** and **1** (only using a single byte)

<br>

### Data Structure Key Points

- It provides a concrete representation for the data and its organisation

  - That is associated with the **_How_**
  - That is easily understood by a software developer

  - **Example**
    - Both a **notebook** and a **ring binder** are types of **Data Structures**
      - They are significantly different
        - The **notebook** doesnt require new pages (unless its full)
        - The **ring binder** requires inserting a new page every time you want to take a new note
      - They are still 2 different kinds of containers that we use to store notes

<br>

### Abstract Data Type Key Points

- They are **mathematical models** of **data types**

  - That is associated with the **_What_**
  - That is easily understood by a software developer

  - **Example**
    - If you consider a plastic envelope **folder** as an **Abstract Data Type**
      - It can contain (n >= 0) pages of notes, one after another
      - We can use certain actions
        - Buy a new folder
        - Check how many pages of notes are inside
        - Put in a new page of notes
        - Retrieve a page of notes
        - Throw out a page of notes

<br>

#### The Two Parts of an ADT

- **Public/External**

  - What does the **Object** look like (How is it structured) | The view given to the **User**
  - What sort of operations can be done on the **Object** | The information given to the **User**

- **Private/Internal**

  - How is the data actually stored (Data Structure) | The view given to the **Developer**
  - How are the operations actually implemented | The information given to the **Developer**

- The **ADT** provides an **Interface** (protocol of communication) between:

  - The **Data Structure** (Concrete and Detailed representation of the data)
  - The **User** (Needs to make use of the data and its operations)

- When you are designing the **Public** part of the **ADT** you need to have the **User** in mind

  - Describe the **Data Type** you are going to offer
  - Describe the **Operations** that can be done with this **Data Type**
    - **Concrete**
      - Specify clearly how to call the operation
      - Specify completely the operations effect on the data type
    - **Generic**
      - Dont specify how the data is stored (Data Structure)
      - Dont specify the algorithms that are performing the operation

- When you are designing the **Private** part of the **ADT** you need to have the **Developer** in mind
  - Define concrete **Data Structures** to represent the data
  - Define concrete algorithms to impletement all **Operations**

<br>

#### Advantages of an ADT

- Improves a programming **readability** and **ease of maintenance** (the code is easier to understand)
- Enables **Modularity** in programming
  - Usually as the **size** and **complexity** of a program grows, programming tasks become more difficult
    - Breaking down the problem into multiple **small** and **independent** modules (**Modularity**), it allows to better go about the problem as a whole
    - This also allows easily changing/adding functionality in a big application with multiple functionality
      - Easy to locate and modify small modules of code
- Enables **Team** programming
  - Several programmers can work independently on their own individual modules before combining them into one big program/application
  - Programming teams can create ADT's to allow other teams to access their **Data** and **Operations**
    - Without needing to know how the data is represented
    - Without needing to know how the operations are done
- The implementation of an **ADT** can be changed without requiring changes to the program that uses the **ADT**

---

## The Formal Concepts in OOP

- Object Oriented Programming

  - Defines **Classes** to represent **Data** and **Logic** in a program
    - **Classes** can contain **Members** (Data) and **Methods** (Internal Functions)
  - Creates **Instances** of **Classes** (Objects)
    - Builds the program out of their interactions

- Core Concepts (in addition to **Classes** and **Objects**)
  - **Encapsulation**
    - Bundles related data and functions into a class (wraps them together)
  - **Inheritance**
    - Builds a relationship between classes to share class **Members** and **Methods**
  - **Polymorphism**
    - The application of the same code to multiple data types
  - **Abstraction**
    - The hiding of **Members**, **Methods**, and **Implementation** details inside of a class

---

## Python vs Purely Object Oriented Languages

- Languages such as **Java** are purely **Object Oriented**
  - Enforces the **Principles of Object Oriented** strictly
- **Python** doesn't require **Object Oriented** to be used
- **Python** emphasizes freedom to use the language in any way
  - Developers implement **Encapsulation** based on trust
- **Python** provides more **Object Oriented** features than **Java** in some ways
  - Allows the use of **Multiple Inheritance** and other features

---

# CS2513 Week 2

## Encapsulation

- First and most basic principle of OOP
- Describes real world entities (**Classes**) in terms of behaviors (**Methods** - actions) and states (**Attributes** - details)
- Change state through the use of **behaviors**
  - Makes code more **robust** by controlling how and when an attribute is changed
  - Means we can **parallelise** work easily
  - Allows the code to be loosely bound

### What is a Class

- A class is a special **Datatype** which defines how to **build** a certain kind of **object**
- The class also stores some **data items** that are shared by all the **instances** of this class
- Instances are objects that are created which follow the **definition** given inside of the class
- Python **doesn't** use separate class interface definitions as in some languages
  - You just define the class then use it

### What is an Object

- Objects are the basic run-time entities in an object-oriented system
- They may represent a person, a place, a bank account, a table of data or any item that the program must handle
- When a program is executed the objects interact by sending messages to one another
- Objects have two components
  - Data (i.e Attributes)
  - Behaviors (i.e Methods)

<!--
## Our First Class

```python
class Person:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary
``` -->

#### Construction

```Python
def function:
  ClassOne c1
```

- The **Constructor** is called when an object is created.
- This is used to initialize the object
  - Load values into member variables
  - Open files
  - Connect to hardware, databases, networks, etc

#### Destruction

- The **Destructor** is called when an object goes out of **_scope_**
- Object c1 is created when the progran reaches the first line of the function
  - It is then destroyed when the program leaves the function

#### Instantiation

- The object c1 is created in memory
- When it is created its constructor is called to do any necessary initializing
  - Here the constructor is empty so nothing is done
- The constructor can take any number of arguments like any other function but it cannot _return_ any values
  - Essentially the return value is the **object itself**
- If there are multiple constructors the compiler chooses the correct one based on the arguments given

#### Default Constructors

- Every class has constructors and destructors
  - If you dont define them then empty ones that do nothing will be created by the complier
- You must define your own constructors when you want to initialize an object with arguments

### The Constructor

- The \_\_init\_\_ method is also known as a constructor
  - It is always called \_\_init\_\_
- The constructor is called when we create a new instance of a class
  - It used its instance attributes (the objects **_state_**) and gives them some initial values
- It is _"just"_ a function, It is called when we **_instantiate_** an object
- We can use it just like a function, providing default arguments, etc

#### Instantiating Objects with **\_\_init\_\_**

- \_\_init\_\_ is the default constructor
  - Used to begin constructing the class (Initializing)
  - It can take any number of arguments
- The first argument of **_self_** in the definition of \_\_init\_\_ is **special**

### Self

- The first argument of every method is a reference to the **current instance** of the class
  - By convention, we name this argument **self**
- In \_\_init\_\_, **self** refers to the object currently being created
  - So in other class methods, it refers to the instance whose method was called
- Simular to the keyword **_this_** in Java or C++
  - Python uses **_self_** more often than Java uses **_this_**
- You do not give a value for this parameter when you call the method
  - Python will provide it for you

## Abstraction

- **Encapsulation** and **Abstraction** are both used to hide data in some way
  - Generally speaking Encapsulation is the mechanism for **restricting access** to some of an objects components
- This means the internal representation of an object cant be seen from outside the objects definition
- Access to this data is typically only achieved through the use of special methods (**Getters** and **Setters**)
  - By using solely get() and set() methods, we can make sure that the internal data cannot be accidentally set into an inconsistent or invalid state

### Scope of Data

- **Public**
  - Can be accessed anywhere inside or outside the class once it has been initialized
    - Notation: name (no special notation)
- **Protected**
  - Can be accessed anywhere within the same package
  - Like a Public member but they represent data that **should not** be directly accessed from the outside (but still _can_ be)
    - Notation: \_name (single underline)
- **Private**
  - Can only be accessed inside the same class
  - **Cant** be seen or accessed from outside the class
    - Notation: \_\_name (double underline)
