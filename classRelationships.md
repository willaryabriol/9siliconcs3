# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: Employee
Description: A representation of a real-world employee.

## New Related Class
Class: Supervisor
Description: A representation of a real-world supervisor. Will be assigned to employees to monitor progress and hand out tasks.

## Association
Relationship: One-to-many
Explanation:

## Multiplicity
Multiplicity: One or more objects can participate in the relationship.
Explanation:

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

## Analysis
### What is the association between your two classes?
- A superviser has (or can have) multiple employees to supervise.
### What multiplicity did you choose and why?
- I chose a multiplicity of one or more and a relationship of one-to-many. I wanted my supervisor class to be able to be assigned to multiple employees. However, I only want each employee to have only one supervisor.
### How did you implement the relationship in Python?
- I allowed each supervisor to have multiple employee classes to "supervise".
### Why did you store an object reference instead of copying its data?
- 
### If your relationship uses many, why is a list appropriate?
- 