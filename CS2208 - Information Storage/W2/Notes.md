# CS2208 Week 2 - Query Languages

## Relational Query Languages

- **Query Languages**
  - Allow manipulation and retrieval of **data** from a **database**
- **Relational** model supports **simple**, **powerful** QLs
  - Strong **formal foundation** based on logic
  - Allows for much **optimization**
- Query Languages **!=** Programming Languages
  - QLs not expected to be "Turing complete"
  - QLs not intended to be used for complex calculations
  - QLs support easy, efficient access to large data sets

### Formal Relational Query Languages

- Two mathematical Query Languages form the basis for “real” languages (e.g. SQL), and for implementation
  - **Relational Algebra**
    - More operational, very useful for representing execution plans
  - **Relational Calculus**
    - Lets users describe what they want, rather than how to compute it
      - Non-operational, declarative

## Preliminaries

- A query is applied to relation instances, and the result of a query is also a relation instance
  - Schemas of input relations for a query are fixed(but query will run regardless of instance)
  - The schema for the result of a given query is also fixed, Determined by definition of query language constructs
- Positional vs. Named-field Notation
  - Positional notation easier for formal definitions, named-field notation more readable
  - Both used in Relational Algebra and SQL

## Relational Algebra

- Basic operations
  - Selection - Selects a subset of rows from relation
  - Projection - Deletes unwanted columns from relation
  - Cross-product - Allows us to combine two relations
  - Set-difference - Tuples in rel.1, but not in rel.2
  - Union - Tuples in rel.1 and in rel.2
  - Renaming (for named perspective)
- Additional operations
  - Not essential, but very useful
    - Intersection
    - Join
    - Division
    - Renaming
- Since each operation returns a relation, operations can be composed
