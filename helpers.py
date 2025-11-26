import json
import time
import ssl
import urllib.request
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver


def retrieve_phone_code(driver: WebDriver) -> str:
    """
    Retrieves the phone confirmation code from the browser's performance logs.
    Automatically extracts the numeric confirmation code from the
    api/v1/number response in the Chrome DevTools Protocol logs.
    """
    code = None

    for _ in range(10):  # Retry up to 10 times
        try:
            logs = [
                log["message"]
                for log in driver.get_log("performance")
                if log.get("message") and "api/v1/number?number" in log["message"]
            ]

            for log in reversed(logs):
                message_data = json.loads(log)["message"]

                body = driver.execute_cdp_cmd(
                    "Network.getResponseBody",
                    {"requestId": message_data["params"]["requestId"]}
                )

                code = "".join(filter(str.isdigit, body["body"]))

        except WebDriverException:
            time.sleep(1)
            continue

        if code:
            return code  # Return extracted digits

    raise Exception(
        "No phone confirmation code found. Make sure the code request was triggered."
    )


def is_url_reachable(url: str) -> bool:
    """
    Checks whether the given URL is reachable by performing a simple HTTP GET request.
    SSL certificate checks are disabled.
    """
    try:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE

        with urllib.request.urlopen(url, context=ssl_ctx) as response:
            return response.status == 200

    except Exception:
        return False
