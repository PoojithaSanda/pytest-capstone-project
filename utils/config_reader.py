import os

BASE_DIR = os.getcwd()

def get_report_path():
    return os.path.join(BASE_DIR, "reports")

def get_screenshot_path():
    return os.path.join(BASE_DIR, "screenshots")

def get_log_path():
    return os.path.join(BASE_DIR, "logs")