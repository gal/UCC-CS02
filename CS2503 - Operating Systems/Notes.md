<details>
<summary>Table of Content</summary>
<!-- TOC -->

- [CS2503 Week 1](#cs2503-week-1)
  - [Module Content](#module-content)
  - [Linux](#linux)
    - [Why Study This](#why-study-this)
  - [Unix Philosophy](#unix-philosophy)
  - [Underpin Means Overrule](#underpin-means-overrule)
- [CS2503 Week 2](#cs2503-week-2)
  - [General Command Format](#general-command-format)
    - [The Command Prompt](#the-command-prompt)
      - [Essential Info Commands](#essential-info-commands)
    - [Files](#files)
      - [Cat Tips](#cat-tips)
      - [Redirection Operators](#redirection-operators)
      - [Pipes](#pipes)
        - [Uses of Pipes](#uses-of-pipes)
        - [Brief note of Grep & Find](#brief-note-of-grep--find)
      _ [Uses of Pipes](#uses-of-pipes)
      _ [Brief note of Grep & Find](#brief-note-of-grep---find)

</details>

---

# CS2503 Week 1

- This **IS NOT** an **Introduction to Basic OS Theory**
  - That is covered in the Semester 2 module
- This **IS** designed to provide **Hands On** practice in
  - Command Line
  - Filesystem
  - Text Processing
    - Regex, AWK, Sed families, etc
  - Bash Scripting (For basic uses)
    - e.g. System Monitoring, Log Processing, etc
- While you may not be able to
  - Design and write advanced complex scripts
- You should not be freaked by scripts and be able to
  - Run and modify even advanced scripts to suit your own requirements

## Module Content

- **Basic commands**
  - Files
  - Directories
  - Access management - modes
  - Disk space management
  - Processes & process management
- **Editors**
  - Basic ubiquitous:
    - Ed
    - Sed
    - Vi(m)
    - pico
    - nano
  - GUI
  - IDE
- **Tools & Utilities**
  - Grep
    - Basically to find strings, either names, contents, but flexible & programmable with **Regular Expressions**
      - A way of specifying string patterns (grep:- global regular expression print)
  - AWK (open source gawk)
- **Extras**
  - bash scripting
  - ssh
  - VPN
- **System Administration**
  - System configuration
  - User administration
  - Software installation/compiles etc

---

## Linux

- _What?_
  - **Open Source** Unix-like **Operating System**
- _Why?_
  - **Modify** and **Adapt**, even **Commercialise** derivatives
  - Free from **Licence Restrictions**
  - Low/Zero **Cost**
- _Where?_
  - **Everywhere**
    - Tiny Embedded Microchips
    - Massive Mainframes
    - Worldwide Web
- _How?_
  - It's made - **CS2506** (Semester 2)
  - It works - **CS2503** (Semester 1)

### Why Study This

- **Forerunner** of all modern **Operating Systems**
- It **Underpins** everything, so it **Overrules** everything
  - If you want to get something to work, do it using the thing that runs _everything_
  - If you need to get files, processes, and processors to work well together; Use the glue that molds, holds, and folds all of them in the first place
- Completely **Modifyable**

---

## Unix Philosophy

- Write programs that:
  - Do just **one thing** and do it **well**
    - **Focussed**
    - **Efficient**
    - Runs fast of large amounts of **Data**
    - Using **Low Resources**
  - Work **together**
    - **Output** of one
    - **Input** of another
  - Handles **Text Streams**
    - **Universal** Interface
    - **Efficient**

---

## Underpin Means Overrule

- A program is only **one link** in the **chain**, or **one cog** in the **wheel**
  - In **_'Nix_** everything is either a **File** or a **Process**
- Programs run as **Processes**
  - They **_Consume_** and **_Generate_** **Data Streams** in the form of
    - **Files**
      - For **Storage**, **Subsequent Processing** or **Analysis**
        - via **Buffers**, **File System Managers**, **Disk Controllers**, etc
    - **Pipes**
      - **Temporary Files** created and afterwards destroyed by the system to allow processes to communicate
    - **Sockets**
      - Basically like **Pipes** but are on different **Processors/Machines**
  - Which are fed to other **Processes**
    - Over and over, until the job is complete

---

# CS2503 Week 2

## General Command Format

### The Command Prompt

- Commands are the way to "do things" in Unix consisting of a **command name** with options called **_flags_** and **_arguments_**
  - [prompt]\$: **_< command >_**, **_< flags >_**, **_< arguments >_**
- **Commands** are typed at the _command prompt_
- In Unix, **everything** (including commands) is **case sensitive**
- **Flags** can be combined into strings
  - e.g (**-l -a - o**) could be written just as (**-lao** or **-aol**, etc)
- **Note:**
  - In Unix, you're expected to know what you're doing
  - Commands only give errors if it fails to run, Otherwise itll do exactly what you tell it to
    - You could destroy youre entire system without a single warning

#### Essential Info Commands

- The most **useful** commands you’ll ever learn

  - **man** ("Manual")
  - **info**

- They help youfind information about other commands

### Files

- All **data** are handled as **files**, which are simply a sequence of **bytes**

  - including **devices**: screen, keyboard, printer, disks

- **Files** can be
  - **Redirected** using **operators** "< . >"
    - e.g cmd < input file > output file
      - So screen output can be **sent** to a file instead
      - Input can be taken from the file instead of **keyboard** (vice versa)
  - **Appended** using **operators** ">>"
    - e.g >>append_outputfile
    - Useful for **adding** to a file instead of overwriting an existing file
  - **Piped** from program to program: cmd1|cmd2|cmd3
    - Instead of having the user having to create temporary files
    - Handy and powerful "**One-liner**" commands
  - **Teed** - "tee"
    - Outputs from a program can be **split** : as in a **T-junction**

#### Cat Tips

- **cat filename1 filename2 >filename3**
  - Concatenates or Joins
    - Input files **_filename1_** and **_filename2_**
      - No designator need for the input file
    - Into the output file **_filename3_**
      - Designated by the **redirection operator** >
- **cat file >filecopy**
  - Copies **_file_** to **_filecopy_**, but best to use copy command **cp file filecopy**
- **cat filename1**
  - Displays the contents of **_filename1_**
    - No output file is designated, so **standard output** is used (**Screen**)
- **cat >filename1**
  - Creates a new file named **_filename1_** whose contents are whatever you type on the keyboard
    - No input file is designated, so **standard input** is used (**Keyboard**)

#### Redirection Operators

- **< file**
  - **Read** standard input from file
- **> file**
  - **Write** standard output to file
    - file will be **created** if not there, otherwise **overwritten**
- **>> file**
  - **Append** (add to end) standard output to end of file
    - will **not overwrite** existing file

#### Pipes

- **Pipe** output from one command or process to another command or process
  - Through the **intermediate files**
    - Which the system automatically
      - Creates so they can be used, and saves user doing it
      - **Clears** up after use to save space
  - e.g cat myfile | grep key | sort | lpr
    - or the normal shorter equivalent
      - grep key myfile | sort | lpr
        - **grep** does **global regular expression pattern matching** (More later)

##### Uses of Pipes

- The examples below only search the **filenames** for **patterns**, not the **file contents**, as the "**file**" piped to **grep**, is merely the **file listing** from "**ls**"
  - ls -alR | grep searchterm
    - ls - alR will
      - List all **filenamess** in long format **Recursively** from cwd
    - **Piping** the output to grep which
      - Will only output lines **matching** the **searchterm**
  - e.g ls -al | grep music
    - Will output **all filenames** from ls within the current directory which have **music** in their title
    - Saves waiting on scrolling and searching through huge output on screen

##### Brief note of Grep & Find

- **find**
  - Finds **filenames** in a **directory hierarchy**, with many of the features of grep below
  - Has security issues in a **multiuser environment**
- **locate**
  - Runs **faster** when called since it
  - Searches a **file index** / database, already created by so
    - The **system** needs to build an **index** in advance
    - It may miss **recently created** (or **deleted**) files
  - Is clearly less flexible than a DIY grep configured command
- **grep**
  - Can use **regular expressions** to specify text patterns
  - search (**recursively**)
    - **File contents**
    - **File names**, by **piping** just **output** from "ls"
  - Run much **slower** than **locate**, as it works through the **filesystem** when called
  - Is more **flexible** than locate, which only works on pre-indexed filenames
