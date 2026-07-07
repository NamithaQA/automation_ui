Repo: automation_ui

UI automation suite for built with Playwright + pytest (Python), using the Page Object Model.
Covers navigation (with test parameterization), trading dashboard data, content link integrity, and edge-case/invalid-route handling. Runs cross-browser (Chromium, Firefox, WebKit) and added GitHub Actions for CI.

Project structure

```text
automation_ui/
├── .github/workflows/       # CI pipeline definition
│   └── playwright-test.yml
├── config/
│   └── config.json          # Per-environment settings (qa/uat/prod), browser, viewport, timeout
├── pages/                    # Page Object Model classes
│   ├── base_page.py          # Baicl actions/assertions (click, fill, visibility, etc.)
│   └── home_page.py          # Home page object, extends BasePage
├── tests/                    # Test specs (pytest)
│   ├── test_navigation.py        # Main nav bar: links present, visible, redirect correctly, parameterize tests
│   ├── test_content_links.py     # Duplicate of navigation coverage (candidate for consolidation)
│   ├── test_trading.py           # Spot market table: category filters, price/% formatting
│   └── test_edge_cases.py        # Broken-link detection across footer links; invalid route returns 404
├── utils/
│   └── config.py             # Loads config.json and resolves settings for the selected --env
├── reports/
│   └── trace.zip              # Playwright trace from the last run
├── conftest.py                # pytest fixtures: CLI options (--env, --browser), browser/context/page setup, tracing
├── pytest.ini                  # Default pytest options (verbose, chromium, qa env) and test discovery rules
├── requirements.txt            # Python dependencies: pytest, playwright, pytest-html
├── task_2_solution_QA_strategy.md   # QA strategy write-up (Task 2 solution - QA strategy)
```

## Key files explained


- conftest.py -  Defines `--env` and `--browser` CLI flags, and session/function-scoped fixtures (`config`, `browser`, `context`, `page`). Starts Playwright tracing per test and saves it to `reports/trace.zip`. 

- pytest.ini - Sets default options (--browser chromium --env qa), test discovery to tests/ folder

- config/config.json - One base_url per environment (`qa`, `uat`, `prod`) plus shared `browser`, `headless`, `viewport`, and `timeout` settings.

- utils/config.py - Reads `config.json`

- pages/base_page.py -  Reusable Playwright wrappers: `goto`, `click`, `fill`, `get_text`, `is_visible`, `wait_for_visible`, plus `expect`-based assertions. 

- pages/home_page.py -  Page object for the home page, used as the entry point in every test. 

- tests/test_* - all scenario test files

## Prerequisites

- Python 3.10+
- pip
- Run requirements.txt file to isntall dependencies
- playwright install

## Command to run test  from root folder of repo

pytest --html=reports/report.html


## Running against a different browser or environment


pytest --browser firefox          # or webkit
pytest --env uat                  # or prod
pytest --browser webkit --env prod


> Note: `config/config.json` sets `"headless": false` by default, so browsers launch with a visible UI. Set it to `true` to run headless. For Ci runs it's headless

## Reports and traces

- Add `--html=reports/report.html` to any `pytest` command to generate HTML test report.
- Every test run captures a Playwright trace (screenshots, DOM snapshots, sources) to `reports/trace.zip`. Inspect it with below command:
  
  playwright show-trace reports/trace.zip
  

## Continuous Integration

`.github/workflows/playwright-test.yml` runs the full suite on every push and pull request to `main`: installs dependencies, installs Playwright browsers with OS deps, and executes `pytest`.

## Trace file  (Test with Chromium)
<img width="1911" height="946" alt="image" src="https://github.com/user-attachments/assets/d98f0181-5391-4ce2-88a3-c6b1c99d163e" />

## Test report
<img width="1863" height="726" alt="image" src="https://github.com/user-attachments/assets/daeace94-8ef7-4121-9821-5887833f3ce8" />

## HTML report
<img width="1879" height="946" alt="image" src="https://github.com/user-attachments/assets/b92a646e-528d-4cb7-a234-314ec836f709" />

## Test run on Firefox
<img width="1881" height="1006" alt="image" src="https://github.com/user-attachments/assets/6d0d7a03-62c7-4e15-b706-06fde454e332" />

## Github actions:
<img width="941" height="475" alt="image" src="https://github.com/user-attachments/assets/0825e116-8ecf-462d-aec5-d56c9a8a1b30" />




