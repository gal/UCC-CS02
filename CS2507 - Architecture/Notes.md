<details>
<summary>Table of Content</summary>

- [CS2507 Week 1](#cs2507-week-1)
  - [Module Content](#module-content)
  - [Introduction to Computer Architecture](#introduction-to-computer-architecture)
    - [What is a Computer](#what-is-a-computer)
      - [Computer Components](#computer-components)
      - [Inside the Processor](#inside-the-processor)
      - [Inside the Memory](#inside-the-memory)
      - [Networks](#networks)
    - [Eight Great Ideas](#eight-great-ideas)
    - [Computer Abstraction](#computer-abstraction)
      - [Levels of Code](#levels-of-code)
    - [Key approaches to Improve Computer Performance](#key-approaches-to-improve-computer-performance)
      - [Key Performance Metrics](#key-performance-metrics)
      - [Key Performance Limits](#key-performance-limits)

</details>

---

# CS2507 Week 1

## Module Content

- What determines a computers performance
- **Data representation** (e.g. Floating point number) and **Data processing**
- How is code execute in the computer
- **Hardware/Software interfaces**
- **Processor Internals** and **Processor Design**
- **Memory Design** and **Memory Performance**
- **Assembly Programming**

---

## Introduction to Computer Architecture

- Computer Architecture is the science and art of designing **Hardware Components** to create computers that meet **Functional**, **Performance**, and **Cost** goals

### What is a Computer

- Personal computer (general purpose)
- Servers (from Simple Servers to Data Centers)
- Embedded computers (processors inside cars, phones, watches, appliances, etc)

#### Computer Components

- Similar components for in all computers

  - **Inputs/Outputs**
  - **Memory/Storage**
  - **Processor**

- These components would distinct **Physical** and **Logical** implementations
  - The hardware choice depends on many factors such as **Usage**, **Cost**, and **Energy Efficiency**

#### Inside the Processor

- **Datapath**
  - Performs operations on data
- **Controller**
  - Sequences **Datapath** and handles **Memory Access**
- **Cache Memory**
  - Small fast memory for immediate access to **Data**

#### Inside the Memory

- _Volatile_ **Main** Memory
  - Loses instructions and data (resets) when they are powered off
    - **RAM** and **Cache**
- _Non-Volatile_ **Secondary** Memory
  - Stores data persistently through multiple power cycles
    - **Magnet disk** (Hard Drive)
    - **Flash Memory** (SSD)
    - **Optical Disk** (CD-ROM, DVD)

#### Networks

- **Communication**

  - Ethernet
  - WiFi
  - Bluetooth

- **Resources sharing** (Cloud Computing, Printers, etc)

- **Nonlocal access** (Mobile Computing)

---

### Eight Great Ideas

1. Design for **Moore's Law**

   - Design for rapid change

2. Use **Abstraction** to simplify design

   - Representing hardware and software a different levels

3. Make the **Common Case** faster

   - Easier to improve on simple cases than complex ones

4. Performance via **Pipelining**

   - Sequential pattern of parallelism

5. Performance via **Parallellism**

   - Parallel operations are faster

6. **Hierarchy** of memories

   - Arranging memory according to cost/speed

7. Performance via **Prediction**

   - Operating based on healthy guesses

8. **Dependability** via redundancy
   - Including redundant components incase of component failure

---

### Computer Abstraction

- **Abstraction** is the only way to deal with complex systems
  - Divide the system into **Objects**
    - **Interface** (Buttons, Knobs, etc)
      - **_General Users_** deal with the interface
    - **Implementation** ("Black Box")
      - **_Specialists_** deal with the implementation

![Hardware Abstraction](https://i.ibb.co/2MMkrSb/Abstraction-Chart.png)

- The **Instruction Set Architecture** is the key interface between the **Hardware** and low-level **Software**
- Enables many **Implementations** of varying **Cost** and **Performance**

#### Levels of Code

![Code Levels](https://i.ibb.co/vjX71JX/Code-Levels.png)

- **High Level Language**

  - Level of abstraction closer to the problem domain
    - Allowing you to code for the problem itself
    - Not needing to worry about whats really happening in the background of every piece of code
  - Helps with **Productivity** and **Portability**

- **Assembly Language**

  - Textual representation of the individual **Instructions**

- **Machine Language**

  - **Binary** digits (Bits)
  - Encoded **Instructions** and **Data**

---

### Key approaches to Improve Computer Performance

#### Key Performance Metrics

- **Response Time**

  - How long does it take to complete a task
  - Also referred to as **Execution Time** or **Run Time**

- **Throughput**
  - Total work done per unit time
    - How many tasks/transactions/etc per hour
  - Relevent to **Servers**

#### Key Performance Limits

- **Power Wall**

  - This refers to the inability to improve computer performance by just continuously increasing the speed of the **CPU Processing Core**
    - Higher **CPU Processing Core** speed means higher power draw
    - Higher electricity use means more heat output, until eventually the **Processor** cant work reliably
      - **Power** = **CapacitiveLoad** _ **Voltage**&#x00B2; _ **Frequency**

- **Multiprocessors**
  - The way we get around the **Power Wall** is by using **Multi Core Processors**
    - More than one **CPU Processing Core** per chip running at lower individual speeds
    - This uses less power overall (therefor also less heat)
    - Improves system throughput regardless of the lower **Core** speed by harnessing **Parallel Programming**
