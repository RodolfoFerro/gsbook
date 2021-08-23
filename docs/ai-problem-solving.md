---
layout: default
title: AI and Problem Solving
nav_order: 3
---

# AI and Problem Solving

AI at first may seem as magic, or an enigmatic thing, but that's far from reality. Artificial Intelligence is a tool that help us solve problems.

For the purposes of this summary, we will use the concept of problem to be: "Difficult task to solve".

Some problems we may have in our daily life such as how much time we need to travel from point A to point B, or how many bills we need to pay certain cost; to solve those problems our brains tend to break the problem into little pieces, so they're easier to understand and solve. Even when the situations may seem simple, we follow a process of simplification in order to achieve a goal.

## What we need when solving a *problem*:
**Model** -> Simplification of the real problem. How the variables in our enviroment are connected.

**Objective** -> How we know we've reached a goal. What we can achieve.

**Evaluation Function** -> How good our solution is.

**Notes when solving the problem**
The solution we get at the end, is the solution for our model, not the real problem, that's why we need to be as descriptive as posible when building a model, so it can have a better adjustment to the real problem. 

### Some problems

**Traveling Salesman Problem**

Suppose we have a person (or object) that has to travel to different cities, visit all of them, and then return to the original starting point, no city can be repeated, but the path it follows must be the shortest possible.
To solve this problem with a few cities, we can even solve it ourselves with a few iterations, but as we increase the number of cities and/or constraints, the most difficult is to get to an ideal solution. That's where AI comes in.
Even when AI is a lot faster than us to solve this kind of problem, it still falls short due to the nature of the problem, with 10 cities, we would need to consider 3,628,800 possible solutions!.
That's why we need to evaluate our ai algorithm basing on how good the solution is and the time it takes to solve it. Time to solve the problem is the most difficult contraint to satisfy because of the resources of the computer.

**Boolean Satisfiability Problem**

If we have a boolean values, we expect True or False, 1 or 0. The operators that we have in this problem are AND, OR and NOT. With these, we can make different functions that will give us a boolean solution.

The Boolean Satisfiability Problem can be explained with the example:

Given a function like: (x <sub>2</sub> v x<sub>4</sub>) ^ (x<sub>3</sub> v x<sub>1</sub>) ^ (x<sub>2</sub> v ¬x<sub>1</sub>) we need to find the boolean values that will give us True as a result. As the TSP, we have a complexity related to time and resources to solve the problem due to the quantity of variables and iterations we need to make to get a solution, and be able to compare which solution is better.


**Conclusion**

The different problems shown here represent common problems in computer science, problems that have been studied for years. Why keep studying them? These problems are models to real life situations like product production, vehicle routing, computer designs, etc.
All of these can be solved in different ways using artificial intelligence.

---
