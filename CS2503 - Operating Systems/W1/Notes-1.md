- [CS2503 Week 1 - Module Intro](#cs2503-week-1---module-intro)
  - [Module Content](#module-content)
- [CS2503 Week 1 - Intro to Linux (Unix)](#cs2503-week-1---intro-to-linux-unix)
  - [Linux](#linux)
    - [Why Study This](#why-study-this)
  - [Unix Philosophy](#unix-philosophy)
  - [Underpin Means Overrule](#underpin-means-overrule)

---

# CS2503 Week 1 - Module Intro

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

# CS2503 Week 1 - Intro to Linux (Unix)

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
