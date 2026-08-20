# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used in the inventory system for keeping some properties private and unable to be tampered with. Some properties of the inventory system such as the prices and number of stocks can be set as private (by adding double or single underscores) and can only be modified through methods. If encapsulation is applied, then we can ensure that our data cannot be corrupted as easily.

### 2. Abstraction
Abstraction is vital because it keeps our code organized. Within a method or class, we can call a method simply without having to rewrite the code anytime.

### 3. Inheritance
Using inheritance, we can create categories of products that can fall under a parent class. Like, example, we can have a parent class called *Product* and have child classes that inherit from it, such as *Snack* and *Drink*. The child classes may also inherit methods from the parent class such as their name and price.

### 4. Polymorphism
This is somewhat more related to inheritance than any of the others. With polymorphism, we can make classes like the *Snack* and *Drink* respond to the same method names, but differently.

## Reflection
Although all of them are essential to improving the inventory system, I personally think that *inheritance* is the most vital. One of our main problems is creating new, redundant variables if we use procedural programming. As we add new items and the store grows, our inheritance prevents code duplication and redundancy.