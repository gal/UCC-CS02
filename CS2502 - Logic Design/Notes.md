<details>
<summary>Table of Content</summary>
<!-- TOC -->

- [CS2507 Week 1](#cs2507-week-1)
  - [Combinational Circuits](#combinational-circuits)
    - [Introduction](#introduction)
    - [And](#and)
    - [OR](#or)
    - [NOT](#not)
- [CS2502 Week 2](#cs2502-week-2)
  - [Boolean Algebra](#boolean-algebra)
    - [Rules](#rules)
    - [Boolean Algebra vs Numerical Algebra](#boolean-algebra-vs-numerical-algebra)

</details>

---

# CS2507 Week 1

- Logic Design is primarily about **digital circuits**, such as computer hardware
- Logic Design can also be applied to more general digital systems, such as **computer software**

## Combinational Circuits

### Introduction

![](https://cdn.discordapp.com/attachments/471231303317192735/762657625560055818/output-onlinepngtools.png)
![](https://cdn.discordapp.com/attachments/471231303317192735/762657922140078080/output-onlinepngtools_1.png)

### And

![](https://cdn.discordapp.com/attachments/471231303317192735/764803823612461076/output-onlinepngtools_2.png)

- X1 and X2 are **inputs**
- L is the only **output**
- L is on if X1 **AND** X2 are closed
- L assumes 1 if both X1 **AND** X2 assume 1
  - L is 0 otherwise
- Logical equivalent of **Multiplication**
- **Notations**:
  - L = X1 AND X2
  - L = X1 $\land$ X2
  - L = X1 \* X2

### OR

![](https://cdn.discordapp.com/attachments/471231303317192735/764805341220962314/output-onlinepngtools_3.png)

- X1 and X2 are **inputs**
- L is the only **output**
- L is on if either X1 **OR** X2 **OR** Both are closed
- L assumes 1 if either X1 **OR** X2 **OR** Both assume 1
  - L is 0 if otherwise
- Logical equivalent of **Addition**
- **Notations**:
  - L = X1 OR X2
  - L = X1 $\lor$ X2
  - L = X1 + X2

### NOT

![](https://media.discordapp.net/attachments/471231303317192735/764807992071159828/output-onlinepngtools_4.png)

- X is the only **input**
- L is the only **output**
- L is on if X is closed
- L assumes 1 if X assumes 1
  - L is 0 if otherwise
- Logical equivalent of **Addition**
- **Notations**:
  - L = NOT X
  - L = $\neg$X

# CS2502 Week 2

## Boolean Algebra

### Rules

- **Commutative**
  - A + B = B + A
  - A \* B = B \* A
- **Associative**
  - A + (B + C) = (A + B) + C
  - A \* (B \* C) = (A \* B) \* C
- **Distributive**

  - A \* (B + C) = A \* B \* C
  - A + B \* C = (A + B) \* (A + C)

- **Misc Rules**
  - O is **neutral** to $+$
    - A + 0 = A
  - 1 is **neutral** to \*
    - A \* 1 = A
  - Property of Not
    - A + NOT(A) = 1
    - A \* NOT(A) = 0

### Boolean Algebra vs Numerical Algebra

- All values are either 0 or 1
- The NOT function is a **fundamental** operation
- 1 + 1 = 1
- Both $+$ and $*$ are distributive with respect to the other operation
- Neither $+$ nor $*$ have an **inverse** operation
  - e.g. **Subtraction** and **Division** does not exist
