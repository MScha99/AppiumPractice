import pytest
from appium import webdriver
from appium.options.windows import WindowsOptions

capabilitiesPyqt = dict(
    platformName='windows',
    automationName='windows',
    # UWP or Win32 executable path.
    # UWP ex "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
    # Win32 ex: r"C:\Windows\System32\notepad.exe"
    app=r'E:\Projekty\pyDesktopApp\dist\pyqt.exe',
)


@pytest.fixture
def driver():
    driver = webdriver.Remote(
        "http://127.0.0.1:4723", options=WindowsOptions().load_capabilities(capabilitiesPyqt))
    yield driver
    driver.quit()
