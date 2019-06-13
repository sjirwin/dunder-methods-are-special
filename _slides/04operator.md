---
title: Numerical Operators
---

# Numerical Operators

--

## Binary Operators
- Emulate numerical types by defining these methods

Method | Operator
--- | ---
<span style="color:indianred">`__add__`</span> | <span style="color:indianred">**`+`**</span>
<span style="color:indianred">`__sub__`</span> | <span style="color:indianred">**`-`**</span>
<span style="color:indianred">`__mul__`</span> | <span style="color:indianred">**`*`**</span>
<span style="color:indianred">`__truediv__`</span> | <span style="color:indianred">**`/`**</span>
<span style="color:indianred">`__floordiv__`</span> | <span style="color:indianred">**`//`**</span>

--

## Additional Methods
- Many more methods possible
  - <span style="color:indianred">`__matmul__`</span> [<span style="color:indianred">`@`</span>]
  - <span style="color:indianred">`__mod__`</span> [<span style="color:indianred">`%`</span>], <span style="color:indianred">`__divmod__`</span> [<span style="color:indianred">`divmod()`</span>]
  - <span style="color:indianred">`__pow__`</span> [<span style="color:indianred">`**`</span>, <span style="color:indianred">`pow()`</span>]
  - <span style="color:indianred">`__lshift__`</span> [<span style="color:indianred">`<<`</span>], <span style="color:indianred">`__rshift__`</span> [<span style="color:indianred">`>>`</span>]
  - <span style="color:indianred">`__and__`</span> [<span style="color:indianred">`&`</span>], <span style="color:indianred">`__xor__`</span> [<span style="color:indianred">`^`</span>], <span style="color:indianred">`__or__`</span> [<span style="color:indianred">`|`</span>]

--

## Implementation
- Method should return <span style="color:indianred">`NotImplemented`</span> if it does not support the operation with the supplied argument

--

## Reflected Operators
- All of the numerical operators have a reflected version
  - <span style="color:indianred">`__radd__`</span>, <span style="color:indianred">`__rsub__`</span>, etc.
- _Right operand_'s reflected operation is called if the left operand's method returns <span style="color:indianred">`NotImplemented`</span> **and** the operands are different types

--

## Reflected Operator Example
- <span style="color:indianred">`a * b`</span>
  - First call <span style="color:indianred">`a.__mul__(b)`</span>
  - If that returns <span style="color:indianred">`NotImplemented`</span> **and** <span style="color:indianred">`a`</span> and <span style="color:indianred">`b`</span> are different types, then call <span style="color:indianred">`b.__rmul__(a)`</span>
- String "multiplication" uses the reflected operator
  - <span style="color:indianred">`3*'spam'`</span> becomes <span style="color:indianred">`'spam'.__rmul__(3)`</span>

``` python
>>> (3).__mul__('spam')
NotImplemented
>>> 'spam'.__rmul__(3)
'spamspamspam'
```

--

## Augmented Assignments
- Nearly all of the numerical operators have an augmented ("in-place") version
  - <span style="color:indianred">`__iadd__`</span>, <span style="color:indianred">`__isub__`</span>, etc.
  - No in-place <span style="color:indianred">`divmod`</span>
- Implements operations <span style="color:indianred">**`+=`**</span>, <span style="color:indianred">**`-=`**</span>, etc.
- Generally, these methods should do the operation in-place (modifying _self_) and return the result
  - While the result could be _self_, it does not have to be

--

## Fallback Behavior
- If no in-place version available, the operation falls back to the normal method
- So <span style="color:indianred">`a += b`</span> would become either:
  - <span style="color:indianred">`a = a.__add__(b)`</span>
  - <span style="color:indianred">`a = b.__radd__(a)`</span>
- Example: <span style="color:indianred">`str`</span> class does not have <span style="color:indianred">`__imul__`</span>, but <span style="color:indianred">`*=`</span> works regardless

``` python
>>> a = 'spam'
>>> a *= 3
>>> a
'spamspamspam'
```

--

## Yet More Operators
- <span style="color:indianred">`__neg__`</span>, <span style="color:indianred">`__pos__`</span>, <span style="color:indianred">`__abs__`</span>, <span style="color:indianred">`__invert__`</span>
- <span style="color:indianred">`__complex__`</span>, <span style="color:indianred">`__int__`</span>, <span style="color:indianred">`__float__`</span>
- <span style="color:indianred">`__index__`</span>
- <span style="color:indianred">`__round__`</span>, <span style="color:indianred">`__trunc__`</span>, <span style="color:indianred">`__floor__`</span>, <span style="color:indianred">`__ceil__`</span>
