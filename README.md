# Saucedemo Automated Test Suite

Automated UI tests for https://www.saucedemo.com using **Python, Playwright and pytest**,
with the Page Object Model, an HTML report, a Markdown test report, a bug log, and CI on GitHub Actions.

## Structure

```
pages/        page objects (login, inventory, cart, checkout)
tests/        test cases (login, inventory, cart + checkout)
scripts/      make_report.py: builds docs/TEST_REPORT.md from JUnit XML
docs/         TEST_CASES.md, BUG_LOG.md, TEST_REPORT.md (generated)
.github/      CI workflow
```

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                          # headless, all tests
pytest --headed --slowmo 400    # watch the browser
pytest -m smoke                 # quick critical-path run
pytest -m login                 # only login tests
pytest --browser firefox        # other browsers (playwright install firefox)

python scripts/make_report.py   # writes docs/TEST_REPORT.md
```

Outputs: `reports/report.html` (self-contained HTML report with failure screenshots),
`reports/junit.xml`, `docs/TEST_REPORT.md`.

## Continuous integration

`.github/workflows/tests.yml` runs on every push and pull request, publishes the result table in the
run summary, and uploads the reports as a downloadable artifact.

## Documentation

- [Test cases](docs/TEST_CASES.md)
- [Bug log](docs/BUG_LOG.md)
- [Test report](docs/TEST_REPORT.md) (regenerated after each run)

## Design notes

- Tests tagged `known_bug` are `xfail`: they assert the *correct* behaviour of a defect in the bug log,
  so CI stays green while it is open and the test flags XPASS once it is fixed.
- Locators use the site's `data-test` attributes, which are more stable than CSS classes.
- Each test is independent and starts from a fresh browser context.
