# Bug Log

Defects found while testing https://www.saucedemo.com. Each one is encoded as an `xfail` test,
so the suite stays green while the defect is still open, and flips to XPASS when it is fixed.

> Saucedemo is a demo site whose "problem" users are built to misbehave. Re-confirm each entry
> on your own run (open `reports/report.html`) and update **Status** and **Date** before submitting.

| ID | Issue | Steps to reproduce | Expected result | Actual result | Severity | Test case | Status |
|---|---|---|---|---|---|---|---|
| BUG-001 | All products show the same image for `problem_user` | 1. Open saucedemo.com<br>2. Log in as `problem_user` / `secret_sauce`<br>3. Look at the product images | Each product shows its own image | All six products show the same placeholder image | Medium | TC-INV-06 | Open |
| BUG-002 | Sorting has no effect for `problem_user` | 1. Log in as `problem_user`<br>2. Choose "Name (Z to A)" in the sort dropdown | Products reorder Z to A | Product order does not change | Medium | TC-INV-07 | Open |
| BUG-003 | Last name input overwrites first name for `problem_user` during checkout | 1. Log in as `problem_user`<br>2. Add the backpack, open cart, click Checkout<br>3. Type a first name, then a last name | First name and last name fields keep their own values | The text typed in Last Name ends up in First Name; Last Name stays empty | High | TC-CHK-03 | Open |
| BUG-004 | Very slow login for `performance_glitch_user` | 1. Log in as `performance_glitch_user` / `secret_sauce`<br>2. Measure time until Products page appears | Products page loads within 2 s | Login takes several seconds | Low | TC-LOGIN-09 | Open |
| BUG-XXX | *(template)* | | | | | | |
