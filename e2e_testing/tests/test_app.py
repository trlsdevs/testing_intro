from playwright.sync_api import Page

TODO_TEXT = [
    'Write unit test',
    'Write Integration test',
    'Write E2E',
    'Learn ChatGPT'
]


def test_to_do_app(page: Page, playwright):
    url = 'https://todomvc.com/examples/angular2/'
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(url)

    loc = page.get_by_placeholder("What needs to be done?")
    for i in range(len(TODO_TEXT)):
        loc.fill(TODO_TEXT[i])
        page.keyboard.press("Enter")

    for item in page.query_selector_all('.todo-list > li'):
        assert item.inner_text() in TODO_TEXT
