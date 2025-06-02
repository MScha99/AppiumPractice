import unittest
from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='windows',
    automationName='windows',
    #UWP or Win32 executable path.
    #UWP ex "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    #Win32 ex: r"C:\Windows\System32\notepad.exe"
    app='Microsoft.WindowsCalculator_8wekyb3d8bbwe!App',
)
appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=WindowsOptions().load_capabilities(capabilities))

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
       



if __name__ == '__main__':
    unittest.main()
