from playwright.sync_api import Page, expect


def _safe_count(locator):
    try:
        return locator.count()
    except Exception:
        return 0


def _click_first_available(page: Page, selectors):
    for sel in selectors:
        try:
            loc = page.locator(sel)
            if _safe_count(loc) > 0:
                loc.first.click()
                return True
        except Exception:
            continue
    return False


def _fill_first_available(page: Page, selectors, text):
    for sel in selectors:
        try:
            loc = page.locator(sel)
            if _safe_count(loc) > 0:
                loc.first.fill(text)
                return True
        except Exception:
            continue
    return False


def test_search_product(page: Page):
    # Open home page
    page.goto("https://automationexercise.com/", wait_until='domcontentloaded', timeout=30000)

    # Navigate to Products
    product_selectors = ["a[href='/products']", "a:has-text('Products')", "text=Products"]
    assert _click_first_available(page, product_selectors), "Could not navigate to Products page"
    page.wait_for_load_state('domcontentloaded')

    # Search for T-shirts
    search_selectors = ["input#search_product", "input[name='search']", "input[placeholder*='Search']", "input[type='text']"]
    assert _fill_first_available(page, search_selectors, 'T-shirts'), "Search input not found"

    # Click search button
    search_btn_selectors = ["button#submit_search", "button:has-text('Search')", "button[type='submit']", "input[type='submit']"]
    assert _click_first_available(page, search_btn_selectors), "Search button not found"

    # Verify that results are displayed
    results_selectors = [".product-list", ".features_items", ".product-item", ".single-products", ".col-sm-4", ".productinfo"]
    has_results = False
    for sel in results_selectors:
        loc = page.locator(sel)
        if _safe_count(loc) > 0:
            has_results = True
            break
    assert has_results, "No search results found"

    # Add first product to the cart
    add_selectors = ["a.add-to-cart", "button:has-text('Add to cart')", "a:has-text('Add to cart')", "div.product-overlay a"]
    assert _click_first_available(page, add_selectors), "Add to cart button not found"

    # Open cart
    cart_selectors = ["a[href='/view_cart']", "a:has-text('Cart')", "a:has-text('View Cart')", "text=Cart"]
    assert _click_first_available(page, cart_selectors), "Cart link not found"

    # Verify product is displayed in the cart
    cart_item_selectors = ["tr.cart_item", ".cart_info", "td.cart_description", ".product-name", ".table-responsive tr"]
    in_cart = False
    for sel in cart_item_selectors:
        loc = page.locator(sel)
        if _safe_count(loc) > 0:
            in_cart = True
            break
    assert in_cart, "No items found in the cart"
