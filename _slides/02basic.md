---
title: Basic Customization
---

# Basic Customization

--

## `__init__`
- Initialises a newly created instance of the class
- Derived class <span style="color:indianred">`__init__`</span> needs to explicitly call the base class <span style="color:indianred">`__init__`</span>
- Should not have a <span style="color:indianred">`return`</span> statement
  - A <span style="color:indianred">`TypeError`</span> is raised if a non-<span style="color:indianred">`None`</span> is returned

```python
{% include examples/02basic/init.py %}
```

--

## `__repr__`
- Returns the "official" string representation of an object
- If possible, should look like a valid Python expression
- Typically used for debugging, so string should be information-rich and unambiguous

```python
{% include examples/02basic/repr.py %}
```

--

## `__str__`
- Returns the "informal" or "pretty print" string representation of an object
- Default implementation calls <span style="color:indianred">`__repr__()__`</span>

```python
{% include examples/02basic/str.py %}
```

--

## `__bool__`
- Defines the truthiness of the object
- Should return <span style="color:indianred">`False`</span> or <span style="color:indianred">`True`</span>
- If not defined, <span style="color:indianred">`__len__()`</span> is called instead
- If neither is defined, all  instances are considered true

```python
{% include examples/02basic/bool.py %}
```

--

## Additional Customization
- Representation
  - <span style="color:indianred">`__format__`</span>, <span style="color:indianred">`__bytes__`</span>
- _"Rich Comparison"_ Methods
  - <span style="color:indianred">`__lt__`</span>, <span style="color:indianred">`__le__`</span>, <span style="color:indianred">`__eq__`</span>, <span style="color:indianred">`__ne__`</span>, <span style="color:indianred">`__gt__`</span>, <span style="color:indianred">`__ge__`</span>
- Advanced
  - <span style="color:indianred">`__new__`</span>, <span style="color:indianred">`__del__`</span>, <span style="color:indianred">`__hash__`</span>