# Computational Thinking Exercise
## Smart School Canteen Queue
**Name:** Willary A. Abriol
**Section:** 9-Silicon
**Last Name:** Abriol
**Date:** August 20, 2026

## Step 1: Identify the Big Problem
### Main Problem
The school canteen is small, and the system is inefficient during lunch break due to a number of factors like long lines, manual transaction, and an inefficient ordering system.

## Step 2: Identify the Sub-Problems
1. The cashier has to manually count the bills and change, which increases transaction time.
2. Students take too long to order.
3. There is no inventory system to track food items.
4. The canteen gets crowded and disorganized.

## Step 3: Apply Computational Thinking Skills
1. Problem - Slow, manual transactions
- CT Skill: Algorithm Design
- Solution: We can design an algorithm to facilitate or automate the computation of the bill.
2. Problem - No inventory system
- CT Skill: Algorithm Design
- Solution: Similar to the manual transaction problem, we can design an algorithm to keep track of product stocks and see which ones are running out.
3. Problem - Canteen getting crowded
- CT Skill: Pattern Recognition
- Solution: We can observe patterns in customer orders during lunch hour to speed up. We may predict what food items they are most likely to order.
4. Problem - Slow ordering
- CT Skill: Abstraction
- Solution: To speed up the ordering process as much as possible, we can create a simplified menu that shows only the essential things like name and price.

## Step 4: Algorithmic Solution

### Sub-Problem: The cashier has to manually count the bills and change.

    START
        Input ITEMS (this will be a list)
        Input CASH
        Set COST = 0
        For ITEM in ITEMS:
            #COST += PRICE
        Print "Total Amount: ", COST

        If CASH < COST:
            #Print "Not enough cash."
        Else:
            #CHANGE = CASH - COST
            #Print "Change: ", CHANGE
    END