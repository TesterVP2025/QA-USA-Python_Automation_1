import json
import time
import ssl
import urllib.request
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def retrieve_phone_code(driver: WebDriver) -> str:
    code = None
    for _ in range(10):
        try:
            logs = [
                log["message"]
                for log in driver.get_log('performance')
                if log.get("message") and 'api/v1/number?number' in log["message"]
            ]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd(
                    'Network.getResponseBody',
                    {'requestId': message_data["params"]["requestId"]}
                )
                code = ''.join(filter(str.isdigit, body['body']))
        except WebDriverException:
            time.sleep(1)
            continue

        if code:
            return code

    raise Exception("No phone confirmation code found. Ensure the code was requested before calling this function.")

def is_url_reachable(url: str) -> bool:
    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            return response.status == 200
    except Exception:
        return False

def complete_phone_login(page, driver):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(page.phone_number_field)).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(page.phone_number_field)).send_keys("+11231231212")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(page.next_button)).click()
    time.sleep(5)
    code = retrieve_phone_code(driver)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located(page.sms_code_field)).send_keys(code)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(page.confirm_button)).click()
