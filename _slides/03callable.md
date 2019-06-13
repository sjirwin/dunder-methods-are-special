---
title: Callable
---

# Callable

--

## Definition
- A callable object is any object that can be "called"
  - Basically, any object that supports the <span style="color:indianred">`()`</span> operator
- Python callable objects
  - Built-in functions
  - User-defined functions
  - Class objects
  - Methods of built-in objects
  - Methods of class instances
  - Objects which have a <span style="color:indianred">`__call__()`</span> method

--

## `__call__`
- Informally, defining <span style="color:indianred">`__call__()`</span> means class instances behave as functions

```python
{% include examples/03callable/MultiplyBy.py %}
```
```python
>>> from MultiplyBy import MultiplyBy
>>> f = MultiplyBy(3)
>>> f(42)
126
>>> f(1+2j)
(3+6j)
>>> f('spam')
'spamspamspam'
```
