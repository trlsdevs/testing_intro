import pytest
from playwright.sync_api import Page
from PIL import Image, ImageChops
import os


def compare_images(ch_path, fx_path):
    # Load the images
    image1 = Image.open(ch_path)
    image2 = Image.open(fx_path)

    # Check if the images have the same size and format
    if image1.size != image2.size or image1.mode != image2.mode:
        return False
    else:
        # Get the difference between the images
        diff = ImageChops.difference(image1, image2).convert("RGB")

        # Check if the images are the same
        if diff.getbbox() is None:
            return True
        else:
            diff.save(os.getcwd() + "/diff.png")
            return False


def test_main_navigation(page: Page, playwright):
    curr_dir = os.getcwd()

    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://playwright.dev/docs/api/class-playwright")
    ch_path = curr_dir + "/ch_screenshot.png"
    page.screenshot(path=ch_path)

    chromium = playwright.firefox  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://playwright.dev/docs/api/class-playwright")
    fx_path = curr_dir + "/fx_screenshot.png"
    page.screenshot(path=fx_path)

    assert compare_images(ch_path, fx_path)
