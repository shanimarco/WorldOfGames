from selenium import webdriver
driver = webdriver.Chrome()
from time import sleep

def test_scores_service():
    driver.get("http://127.0.0.1:8777/worldOfGame")
    scor_val = int(driver.find_element(by="xpath", value="/html/body/h2").text)
    sleep(1)
    print(scor_val)

    if scor_val >=1 and scor_val <=1000:
        result = 'success'
    else:
        result = 'error'

    return(result)

def main_function():
    result = test_scores_service()
    if result == 'success':
        exit_code = '0'
    else:
        exit_code = '-1'

    return(exit_code)

print(main_function())



