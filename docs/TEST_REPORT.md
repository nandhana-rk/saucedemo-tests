# Test Execution Report

- **Application under test:** https://www.saucedemo.com
- **Tool:** Playwright (Python) + pytest
- **Generated:** 2026-11-24 21:31 UTC
- **Total duration:** 144.5s

## Summary

| Total | Passed | Failed | Known bugs (xfail) | Skipped |
|---|---|---|---|---|
| 27 | 23 | 0 | 4 | 0 |

`xfail` = test encodes the expected behaviour for a defect already listed in [BUG_LOG.md](BUG_LOG.md); it is expected to fail until the defect is fixed.

## Results

| Module | Test | Result | Time (s) |
|---|---|---|---|
| test_cart_checkout | `test_tc_cart_01_add_item_updates_badge[chromium]` | PASS | 3.81 |
| test_cart_checkout | `test_tc_cart_02_add_two_items[chromium]` | PASS | 3.19 |
| test_cart_checkout | `test_tc_cart_03_remove_item[chromium]` | PASS | 3.23 |
| test_cart_checkout | `test_tc_cart_04_cart_lists_added_item[chromium]` | PASS | 5.05 |
| test_cart_checkout | `test_tc_chk_01_complete_purchase[chromium]` | PASS | 5.72 |
| test_cart_checkout | `test_tc_chk_02_required_fields[chromium-no-first-name]` | PASS | 5.33 |
| test_cart_checkout | `test_tc_chk_02_required_fields[chromium-no-last-name]` | PASS | 6.87 |
| test_cart_checkout | `test_tc_chk_02_required_fields[chromium-no-postal-code]` | PASS | 6.33 |
| test_cart_checkout | `test_tc_chk_03_problem_user_last_name[chromium]` | XFAIL | 9.43 |
| test_inventory | `test_tc_inv_01_sort_name_az[chromium]` | PASS | 2.69 |
| test_inventory | `test_tc_inv_02_sort_name_za[chromium]` | PASS | 4.86 |
| test_inventory | `test_tc_inv_03_sort_price_low_high[chromium]` | PASS | 5.60 |
| test_inventory | `test_tc_inv_04_sort_price_high_low[chromium]` | PASS | 5.93 |
| test_inventory | `test_tc_inv_05_every_product_has_distinct_image[chromium]` | PASS | 4.41 |
| test_inventory | `test_tc_inv_06_problem_user_images[chromium]` | XFAIL | 5.49 |
| test_inventory | `test_tc_inv_07_problem_user_sort[chromium]` | XFAIL | 6.20 |
| test_login | `test_tc_login_01_valid_login[chromium]` | PASS | 5.25 |
| test_login | `test_tc_login_02_wrong_password[chromium]` | PASS | 4.37 |
| test_login | `test_tc_login_03_unknown_user[chromium]` | PASS | 5.41 |
| test_login | `test_tc_login_04_locked_out_user[chromium]` | PASS | 4.39 |
| test_login | `test_tc_login_05_required_fields[chromium-empty-username]` | PASS | 5.49 |
| test_login | `test_tc_login_05_required_fields[chromium-empty-password]` | PASS | 5.10 |
| test_login | `test_tc_login_05_required_fields[chromium-both-empty]` | PASS | 4.40 |
| test_login | `test_tc_login_06_username_is_case_sensitive[chromium]` | PASS | 4.37 |
| test_login | `test_tc_login_07_direct_url_requires_login[chromium]` | PASS | 3.19 |
| test_login | `test_tc_login_08_logout[chromium]` | PASS | 5.47 |
| test_login | `test_tc_login_09_performance_user_logs_in_quickly[chromium]` | XFAIL | 12.71 |
