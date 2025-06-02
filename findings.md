# installation

```
start venv
npm install -g appium
appium --version
pip install Appium-Python-Client
appium driver install --source=npm appium-windows-driver
appium driver list
appium driver run windows install-wad
```

# resources

## find UWP user model ID

```
Get-StartApps
```

## docs (incomplete and/or outdated)

https://github.com/appium/appium-windows-driver#install-wad  
https://pypi.org/project/Appium-Python-Client/  
https://appium.io/docs/en/latest/quickstart/test-py/  
https://github.com/Microsoft/WinAppDriver  

## find locators
https://accessibilityinsights.io/


## some things to remember

ACCESSIBILITY_ID (appium term) maps to AutomationId (windows term)