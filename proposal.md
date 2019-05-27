# Proposal

## Abstract
Special methods are a powerful feature of Python. Such methods have names starting and ending with double underscores (aka dunder). In this talk, we will explore some of those special methods and show how you can use them to make your custom types more full-featured.

## Description
Special methods are those methods on a type which are called implicitly by Python to execute a certain operation (e.g., addition). These methods have distinctive names which start and end with double underscores (aka dunder).

Dunder methods are a language feature which allows developers to implement custom types which have the same features and expressiveness as the Python standard types.

It is impossible to discuss all of the various dunder methods in a single 25-minute talk, so we will focus on a selected subset of dunder methods. We will discuss how and why you would implement them and in which situations Python will implicitly call them.

## Notes
When talking to developers, even those of moderate experience, I have found that most of them are not aware of the capabilities that special methods make available to them or are confused about how to use/implement them. Even repr vs str is not as well understood as it should be.

There are way too many special methods to cover everything in 25 minutes so the goal of this talk is to raise awareness of special methods. The talk does this by cherry picking a few examples and exploring them - both usage and implementation.

## Outline
* Introduction (1 min)
* Special methods defined (2 min)
* Basic Class Customization (3 min)
  * init, repr, str
* Callable (3 min)
* Operator Overloading (7 min)
  * Binary Operators
  * Extended Assignment
  * Comparison
* Protocols (8 min)
  * Context Manager
  * Container
  * Iterator
* Conclusion (1 min)
