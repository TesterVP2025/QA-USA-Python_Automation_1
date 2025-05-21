import json
import time
import ssl
import urllib.request
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver


def retrieve_phone_code(driver: WebDriver) -> str:
    """
    Retrieves phone confirmation number from performance logs.
    Use this only after the code was requested in your application.
    Returns:
        str: The phone confirmation code.
    Raises:
        Exception: If no code is found after attempts.
    """
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

    raise Exception("No phone confirmation code found. "
                    "Ensure the code was requested in your application before calling this function.")


def is_url_reachable(url: str) -> bool:
    """
    Checks if the given URL is reachable (status code 200).
    SSL certificate validation is bypassed.

    Args:
        url (str): The URL to check.
    Returns:
        bool: True if reachable, False otherwise.
    """
    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            return response.status == 200
    except Exception:
        return False

