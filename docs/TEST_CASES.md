# Test Case Catalogue

| ID | Area | Scenario | Type | Expected result |
|---|---|---|---|---|
| TC-LOGIN-01 | Login | Valid login (`standard_user`) | Positive | Products page with 6 items |
| TC-LOGIN-02 | Login | Wrong password | Negative | "do not match" error, stays on login |
| TC-LOGIN-03 | Login | Unknown username | Negative | "do not match" error |
| TC-LOGIN-04 | Login | `locked_out_user` | Negative | "locked out" error |
| TC-LOGIN-05 | Login | Empty username / password / both | Negative | "... is required" error |
| TC-LOGIN-06 | Login | Username in wrong case | Negative | Error shown |
| TC-LOGIN-07 | Login | Open /inventory.html without login | Security | Access error, no products |
| TC-LOGIN-08 | Login | Logout | Positive | Back on login page |
| TC-LOGIN-09 | Login | `performance_glitch_user` speed | Performance | Login under 2 s (known bug) |
| TC-INV-01..04 | Inventory | Sort name A-Z / Z-A, price low-high / high-low | Positive | Correct order |
| TC-INV-05 | Inventory | Distinct product images | Positive | 6 unique images |
| TC-INV-06 | Inventory | Distinct images as `problem_user` | Regression | Known bug |
| TC-INV-07 | Inventory | Sorting as `problem_user` | Regression | Known bug |
| TC-CART-01..04 | Cart | Add, add two, remove, cart contents | Positive | Badge and cart page correct |
| TC-CHK-01 | Checkout | Complete purchase | E2E | "Thank you for your order!" |
| TC-CHK-02 | Checkout | Missing first name / last name / postal code | Negative | Field-specific error |
| TC-CHK-03 | Checkout | Last name field as `problem_user` | Regression | Known bug |
