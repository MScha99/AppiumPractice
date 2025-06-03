from appium.webdriver.common.appiumby import AppiumBy


def test_starting_app(driver):
    welcome_popup = driver.find_element(AppiumBy.NAME, "Welcome")
    ok_button = welcome_popup.find_element(AppiumBy.XPATH, "/Window/Button[1]")
    ok_button.click()

    window_handles = driver.window_handles
    for handle in window_handles:
        driver.switch_to.window(handle)
        if driver.title == "Welcome":
            print("\n window_handles \n", window_handles)
            print("\n handl \n", handle)
            break

    ok2_button = driver.find_element(AppiumBy.NAME, "OK")
    ok2_button.click()

    window_handles = driver.window_handles
    for handle in window_handles:
        driver.switch_to.window(handle)
        if driver.title == "Test Automation Playground":
            print("\n window_handles \n", window_handles)
            print("\n handl \n", handle)
            break

    openPopupsPage_button = driver.find_element(AppiumBy.NAME, "Popups")
    openPopupsPage_button.click()
    assert openPopupsPage_button.is_displayed(), "blabla"
    assert 2+2==5, "blabla"
