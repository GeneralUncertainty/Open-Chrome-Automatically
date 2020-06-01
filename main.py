from selenium import webdriver

'''
    Check your google chrome browser version

    chrome://version/

    [Only check the first two digits of the version, example: 81, 82, 83 etc.]

    Download ChromeDriver (for chrome)

    Version 84: https://chromedriver.storage.googleapis.com/index.html?path=84.0.4147.30/

    Version 83: https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/

    Version 81: https://chromedriver.storage.googleapis.com/index.html?path=81.0.4044.138/

    Save it anywhere and type it's address instead of path
    
'''

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://youtube.com')

# driver.close() - Close the active browser tab

# How to print the title of the webpage
print(driver.title)

driver.quit() # Close the whole browser window
