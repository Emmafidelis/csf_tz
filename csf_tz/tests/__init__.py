import frappe

# Skip Frappe's global test_records dependency resolution. ERPNext's
# ItemTaxTemplate test_records reference an Account whose Company
# ("_Test Company") never successfully inserts in this app's test bench,
# breaking the whole run. Tests in this module set up their own data;
# any test that needs a specific DocType seeded should declare it via
# `test_dependencies` on the class.
frappe.flags.skip_test_records = True
