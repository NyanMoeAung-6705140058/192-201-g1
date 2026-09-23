# Assignment 03 — CHANGES

**Name:** Nyan Moe Aung  
**Student ID:** 6705140058

This file explains what I changed in the code and why. It also shows my AI prompt log.

---

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products, orders, and items used tuples and index numbers. | I used `Product`, `OrderItem`, `Customer`, and `Order` classes. | Classes / composition | I ran `python Assignment_03.py` → PASS |
| 2 | The code used many `if tier == ...` checks for discount and points. | I used `Customer`, `Silver`, `Gold`, and `Platinum` classes. | Inheritance / polymorphism | I ran `python Assignment_03.py` → PASS |
| 3 | Order data was inside tuples and lists. | An `Order` has a `Customer` and `OrderItem` objects. Each `OrderItem` has a `Product`. | Composition (has-a) | I ran `python Assignment_03.py` → PASS |
| 4 | `calc()` did calculation and printing together. | I used `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` for calculation. `receipt()` is separate. | Pure functions / interface vs implementation | I ran `python Assignment_03.py` → PASS |
| 5 | The code used `global`, magic numbers, and no quantity check. | I removed `global`, used named constants, and checked values in constructors. | Encapsulation / clean refactoring | I ran `python Assignment_03.py` → PASS |

## 2 · Short reflection (4–6 sentences)

The best change was using classes for customer tiers.  
Now each tier has its own discount and points value.  
Composition also makes the code easy to understand because an order has a customer and items.  
I was careful with tax, discount, points, and receipt output because the result must stay the same.  
I ran the self-test after the changes, and it printed PASS.

---

## 3 · Prompt log (Level 2 — required)

I asked ChatGPT to review my refactored code and check it with the Week 5 lecture.  
ChatGPT checked my classes, composition, polymorphism, pure calculation methods, and the final output.  
It also checked that I did not add new features or change the store rules.  
After the review, I ran `python Assignment_03.py` by myself and the result was PASS.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Please review my Assignment_03 code with the Week 5 lecture. Do not add new code or new features." | It reviewed my code and checked the required OOP ideas and same behaviour. | Accepted | I read the code again and ran `python Assignment_03.py` → PASS |
| 2 | "Please check if my code uses composition, polymorphism, and pure methods correctly." | It checked the class design and told me the required Week 5 ideas were used correctly. | Accepted | I checked the class relationships and methods, then ran the program → PASS |
| 3 | "Please check my final code and make sure the output is the same as the original code." | It reviewed the final code and checked that no new feature was added and the output stayed the same. | Accepted | I ran `python Assignment_03.py` again and got PASS |

**Ownership statement.**  
By submitting, I confirm I understand and can explain every line of code I submitted, and this prompt log shows my real AI use.

**Signed:** Nyan Moe Aung

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
