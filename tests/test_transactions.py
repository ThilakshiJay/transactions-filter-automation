
import re

from playwright.sync_api import Page, expect

URL = "https://transaction-page-zeta.vercel.app/transactions_qa_demo.html"


def test_status_filter_narrows_transactions(page: Page):
    page.goto(URL)

    # Confirm the initial count is 55.
    expect(
        page.get_by_text(
            re.compile(r"\d+[–-]\d+ of 55 transactions \(55 total\)")
        )
    ).to_be_visible()

    # Select Unmatched.
    page.locator("#statusSelect").select_option("Unmatched")

    # Verify the filtered count is below 55.
    expect(
        page.get_by_text(
            re.compile(
                r"\d+[–-]\d+ of (?:[1-9]|[1-4]\d|5[0-4]) "
                r"transactions \(55 total\)"
            )
        )
    ).to_be_visible()


def test_search_narrows_transactions(page: Page):
    page.goto(URL)

    search = page.get_by_role("textbox", name="Search")
    search.fill("0x18")

    # This term was observed to return one transaction.
    expect(
        page.get_by_text(
            re.compile(r"1 of 1 transactions \(55 total\)")
        )
    ).to_be_visible()

    expect(
        page.get_by_role("row").filter(has_text="0x18")
    ).to_be_visible()


def test_search_is_case_insensitive(page: Page):
    page.goto(URL)

    # Start with uppercase input to independently verify case-insensitivity.
    search = page.get_by_role("textbox", name="Search")
    search.fill("0X18")

    expect(
        page.get_by_text(
            re.compile(r"1 of 1 transactions \(55 total\)")
        )
    ).to_be_visible()

    expect(
        page.get_by_role("row").filter(has_text="0x18")
    ).to_be_visible()


def test_clear_all_restores_full_transaction_list(page: Page):
    page.goto(URL)

    page.locator("#statusSelect").select_option("Unmatched")

    expect(
        page.get_by_text(
            re.compile(
                r"\d+[–-]\d+ of (?:[1-9]|[1-4]\d|5[0-4]) "
                r"transactions \(55 total\)"
            )
        )
    ).to_be_visible()

    page.get_by_role("button", name="Clear all").click()

    expect(
        page.get_by_text(
            re.compile(r"\d+[–-]\d+ of 55 transactions \(55 total\)")
        )
    ).to_be_visible()

    expect(page.locator("#statusSelect")).to_have_value("All")

