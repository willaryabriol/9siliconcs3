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
1. Problem 

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