import unittest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilitiesCalculator = dict(
    platformName='windows',
    automationName='windows',
    #UWP or Win32 executable path.
    #UWP ex "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    #Win32 ex: r"C:\Windows\System32\notepad.exe"
    app='Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
)

capabilitiesTKinter = dict(
    platformName='windows',
    automationName='windows',
    #UWP or Win32 executable path.
    #UWP ex "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    #Win32 ex: r"C:\Windows\System32\notepad.exe"
    app=r'E:\Projekty\pyDesktopApp\dist\pyqt.exe',
)

appium_server_url = 'http://localhost:4723'


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=WindowsOptions().load_capabilities(capabilitiesCalculator))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_addingUpNumbers(self) -> None:
        seven_btn = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="num7Button")
        plus_btn = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="plusButton")
        eight_btn = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="num8Button")
        equal_btn = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="equalButton")
        result_elem = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="CalculatorResults")

        seven_btn.click()
        plus_btn.click()
        eight_btn.click()
        equal_btn.click()

        result_text = result_elem.text
        print("Raw Calculator output:", result_text)

        prefix = "Wyświetlana wartość to "
        if result_text.startswith(prefix):
            value = result_text.removeprefix(prefix).strip()
        else:
            value = result_text.strip()

        print("Computed value:", value)

        self.assertEqual(15, int(value) )
       
class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=WindowsOptions().load_capabilities(capabilitiesTKinter))

    # def tearDown(self) -> None:
    #     if self.driver:
    #         self.driver.quit()

    def test_addingUpNumbers(self) -> None:
        welcome_popup = self.driver.find_element(AppiumBy.NAME, "Welcome")
        ok_button = welcome_popup.find_element(AppiumBy.XPATH, "/Window/Button[1]")
        ok_button.click()
        # seven_btn = self.driver.find_element(
        #     by=AppiumBy.ACCESSIBILITY_ID, value="num7Button")
        
        # equal_btn.click()

        window_handles = self.driver.window_handles
        for handle in window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == "Welcome":
                print("\n window_handles \n", window_handles)
                print("\n handl \n", handle)
                break
        
            
        ok2_button = self.driver.find_element(AppiumBy.NAME, "OK")
        ok2_button.click()

        window_handles = self.driver.window_handles
        for handle in window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == "Test Automation Playground":
                print("\n window_handles \n", window_handles)
                print("\n handl \n", handle)
                break
        
        openPopupsPage_button = self.driver.find_element(AppiumBy.NAME, "Popups")
        openPopupsPage_button.click()



        self.assertEqual(15,15 )



if __name__ == '__main__':
    unittest.main()



import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

def wait_for_new_window(driver, known_handles, timeout=10, poll_frequency=0.5):
    """
    Waits for a new window handle to appear.

    :param driver: The Appium driver instance.
    :param known_handles: A set of window handles known before the new window appears.
    :param timeout: Maximum time to wait for the new window.
    :param poll_frequency: Time interval between successive checks.
    :return: The handle of the new window.
    :raises TimeoutException: If no new window appears within the timeout period.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        current_handles = set(driver.window_handles)
        new_handles = current_handles - known_handles
        if new_handles:
            return new_handles.pop()
        time.sleep(poll_frequency)
    raise TimeoutException("No new window appeared within the given timeout.")

# # Example usage:
# # Store the current window handles

# existing_handles = set(driver.window_handles)

# # Perform the action that opens the new window
# # For example: driver.find_element(AppiumBy.NAME, "Open Window").click()

# try:
#     new_window_handle = wait_for_new_window(driver, existing_handles, timeout=15)
#     driver.switch_to.window(new_window_handle)
#     print("Switched to the new window.")
# except TimeoutException as e:
#     print(f"Failed to switch to the new window: {e}")
