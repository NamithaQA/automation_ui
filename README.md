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

- tests/test_*

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


> Note: `config/config.json` sets `"headless": false` by default, so browsers launch with a visible UI. Set it to `true` to run headless.

## Reports and traces

- Add `--html=reports/report.html` to any `pytest` command to generate HTML test report.
- Every test run captures a Playwright trace (screenshots, DOM snapshots, sources) to `reports/trace.zip`. Inspect it with below command:
  
  playwright show-trace reports/trace.zip
  

## Continuous Integration

`.github/workflows/playwright-test.yml` runs the full suite on every push and pull request to `main`: installs dependencies, installs Playwright browsers with OS deps, and executes `pytest`.

## Trace file  (Test with Chromium)
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

- tests/test_*

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


> Note: `config/config.json` sets `"headless": false` by default, so browsers launch with a visible UI. Set it to `true` to run headless.

## Reports and traces

- Add `--html=reports/report.html` to any `pytest` command to generate HTML test report.
- Every test run captures a Playwright trace (screenshots, DOM snapshots, sources) to `reports/trace.zip`. Inspect it with below command:
  
  playwright show-trace reports/trace.zip
  

## Continuous Integration

`.github/workflows/playwright-test.yml` runs the full suite on every push and pull request to `main`: installs dependencies, installs Playwright browsers with OS deps, and executes `pytest`.

## Trace file  (Test with Chromium)
![alt text](image.png)

## Test report
![alt text](image-5.png)

## HTML report
![alt text](image-4.png)

## Test run on Firefox
![alt text](image-3.png)


## Test report
![alt text](image-5.png)

## HTML report
![alt text](image-4.png)

## Test run on Firefox
![alt text](image-3.png)
