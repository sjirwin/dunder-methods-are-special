---
title: Special Methods
---

# Special Methods

--

## Terminology
- _special methods_ is the name used in the Python documentation
- Might be referred to elsewhere as 
  - _magic methods_
  - _dunder methods_
    - dunder is shorthand for **d**ouble **under**score (\_\_)

--

## Official Definition
- From the Python [docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)
> Python’s approach to operator overloading, allowing classes to define their own behavior with respect to language operators
- Example: <span style="color:indianred">`__add__`</span> method is called by the <span style="color:indianred">**`+`**</span> (plus) operator and is defined by the built-in types <span style="color:indianred">`int`</span>, <span style="color:indianred">`float`</span>, and <span style="color:indianred">`str`</span>

--

## Why _Special Methods_ Are Useful
- Enables your custom types (classes) to have the same features and expressiveness as the Python standard types

--

## General Notes
- When emulating a built-in type, you should generally only implement the _special methods_ that you need
  - Do not necessarily need to worry about completeness
- Can block functionality by setting special method to <span style="color:indianred">`None`</span>
  - Example, for a sequence container class, can set <span style="color:indianred">`__reversed__`</span> to <span style="color:indianred">`None`</span> to prevent reverse iteration
