# Transactions Filtering — Playwright Automation

This project contains automated tests for the Transactions page using **Python**, **Playwright**, and **pytest**.

This repo is owned by the QA team and is separate from the main app repo.

## How to Use This README

Use this README as a quick guide to set up and run the automation project.

1. **Overview:** Understand the purpose of the project and the tools used.
2. **Prerequisites:** Check that Python and the required tools are installed.
3. **Installation:** Follow the steps to create the virtual environment and install dependencies.
4. **Run Tests:** Use the provided commands to execute the automated tests.
5. **Test Scenarios:** Review which transaction filtering scenarios are covered.
6. **Troubleshooting:** If a test fails, check the error message and verify that the application is accessible.

## Overview

The tests verify that the Status filter and Search field narrow the transaction results correctly, and that the **Clear all** button restores the full, unfiltered list of 55 transactions.

**Application under test:**  
https://transaction-page-zeta.vercel.app/transactions_qa_demo.html

## Tech Stack

- Python
- Playwright
- pytest
- Chromium

## Prerequisites

- Python 3 installed
- pip (Python package installer)

## Installation

1. Clone or download this repository and navigate to the project directory.

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment.

   **Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

   **Windows:**

   ```bash
   .venv\Scripts\activate
   ```

4. Install the project dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Install the Chromium browser required by Playwright:

   ```bash
   python -m playwright install chromium
   ```

## Running the Tests

Run all tests from the project root directory:

```bash
pytest -v
```

To run the tests with the browser visible:

```bash
pytest -v --headed
```

## Automated Test Scenarios

### 1. Status Filter

Select **Unmatched** from the Status filter and verify that the result count shows fewer transactions than the original 55.

### 2. Search Transactions

Enter `0x18` in the Search field and verify that the matching transaction appears and the results are narrowed accordingly.

### 3. Clear All Filters

Apply the Status filter, click **Clear all**, and verify that the full, unfiltered list of 55 transactions is restored.

## Handling Asynchronous Updates

The page applies filter changes asynchronously and does not provide a reliable fixed delay. The tests use Playwright's condition-based assertions, such as `expect(locator).to_be_visible()`, to wait for the expected result-count label or matching transaction to appear.

This avoids hardcoded sleeps and helps reduce flaky tests caused by timing differences.

## Future Improvements

With another day, I would first review the Part 1 PRD against the application's behavior to identify any mismatches and add clear assertions for those requirements. I would also improve test maintainability by extracting repeated locators and common page interactions into reusable helpers if the suite grows. Finally, I would add a few high-value edge cases, such as searching for a term with no matching transactions and verifying how filters behave when combined, while keeping the tests reliable and focused on the intended requirements.
