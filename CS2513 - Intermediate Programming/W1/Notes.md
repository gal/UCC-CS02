- [CS2513 Week 1 - Module Intro](#cs2513-week-1---module-intro)
  - [Module Contents](#module-contents)
- [CS2513 Week 1 - Intro to OOP and ADT](#cs2513-week-1---intro-to-oop-and-adt)
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

---

# CS2513 Week 1 - Module Intro

## Module Contents

- **Object Oriented Programming** (OOP)
- How do we leverage (**reuse**, **extend**, **interact**) with others code
- How do we **package code** so others can use it
- How do we **produce code** so that it is **easily maintained**
- How to create **libraries** of code for yourself and others while ensuring it works **correctly** and **robustly**
- How do we organise **large projects** and allow **several teammates** to work together

---

# CS2513 Week 1 - Intro to OOP and ADT

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
- **Python** doesnt require **Object Oriented** to be used
- **Python** emphasises freedom to use the language in any way
  - Developers implement **Encapsulation** based on trust
- **Python** provides more **Object Oriented** features than **Java** in some ways
  - Allows the use of **Multiple Inheritance** and other features
