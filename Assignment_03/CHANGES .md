# Assignment 03 — CHANGES

**Name:** Nyan Moe Aung  
**Student ID:** 6705140058

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products, orders, and items used tuples and index numbers. | I used `Product`, `OrderItem`, `Customer`, and `Order` classes. | Classes / composition | I ran `python Assignment_03.py` → PASS |
| 2 | The code used many `if tier == ...` checks for discount and points. | I used `Customer`, `Silver`, `Gold`, and `Platinum` classes. | Inheritance / polymorphism | I ran `python Assignment_03.py` → PASS |
| 3 | Order data was inside tuples and lists. | An `Order` has a `Customer` and `OrderItem` objects. Each `OrderItem` has a `Product`. | Composition (has-a) | I ran `python Assignment_03.py` → PASS |
| 4 | `calc()` did calculation and printing together. | I used `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` for calculation. `receipt()` is separate. | Pure functions / interface vs implementation | I ran `python Assignment_03.py` → PASS |
| 5 | The code used `global`, magic numbers, and no quantity check. | I removed `global`, used named constants, and checked values in constructors. | Encapsulation / clean refactoring | I ran `python Assignment_03.py` → PASS |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The best change was using classes for customer tiers. Now each tier has its own discount and points value. Composition also makes the code easy to understand because an order has a customer and items. I was careful with tax, discount, points, and receipt output because the result must stay the same. I ran the self-test after the changes, and it printed PASS.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

> I used AI to help me build and review my code. I asked AI to help me refactor the program without changing the result. After that, I asked AI to review my code and check that everything was working correctly.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Help me build the refactored code for Assignment 03 and keep the same output." | It suggested using classes for products, customers, items, and orders. | Accepted and reviewed | I ran `python Assignment_03.py` → PASS and read the code. |
| 2 | "Please review my code and check the customer tier, discount, and points parts." | It suggested using different customer classes instead of many `if tier == ...` checks. | Accepted and reviewed | I checked the discount and points results and ran the program again → PASS. |
| 3 | "Please check my final code and make sure I did not add extra features or change the output." | It reviewed the final code and checked the calculations, receipt output, and class design. | Accepted and reviewed | I ran the self-test and got PASS. I also read the final code again. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
