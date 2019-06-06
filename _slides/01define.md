---
title: Special Methods
---

# Special Methods

--

## Terminology
- _special methods_ is the name used in the Python documentation
- Elsewhere might be referred to as 
  - _dunder methods_
  - _magic methods_

--

## Official Definition
- From the Python [docs](https://docs.python.org/3/reference/datamodel.html#special-method-names)
> Python’s approach to operator overloading, allowing classes to define their own behavior with respect to language operators

--

## Why _Special Methods_ Are Useful
- Enables your custom types (classes) to have the same features and expressiveness as the Python standard types

--

## General Notes
- When emulating a built-in type, generally should only implement the _special methods_ that you need
  - Do not need to worry about completeness
- Can block functionality by setting special method to <span style="color:indianred">`None`</span>
  - Example, for a sequence container class, can set <span style="color:indianred">`__reversed__`</span> to <span style="color:indianred">`None`</span> to prevent reverse iteration
