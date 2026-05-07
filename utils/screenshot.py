import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    os.makedirs("screenshots", exist_ok=True)

    file_name = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join("screenshots", file_name)

    driver.save_screenshot(path)
    return path