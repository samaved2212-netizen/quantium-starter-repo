import pytest
from dash.testing.application_runners import import_app
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- Full paths to ChromeDriver and Chrome ---
CHROMEDRIVER_PATH = r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
CHROME_PATH = r"C:\chrome-win64\chrome-win64\chrome.exe"

# --- Selenium Service & Options ---
service = Service(executable_path=CHROMEDRIVER_PATH)
options = Options()
options.binary_location = CHROME_PATH
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# --- Import your Dash app ---
from app import app  # Replace 'app' with your Dash app filename if different

# --- Fixture to start Dash app ---
@pytest.fixture
def dash_app(dash_duo):
    dash_duo.start_server(app)
    # Override Selenium driver with explicit paths
    dash_duo.driver.quit()  # Quit default
    from selenium import webdriver
    dash_duo.driver = webdriver.Chrome(service=service, options=options)
    return dash_duo

# --- Test 1: Header ---
def test_header_present(dash_app):
    header = dash_app.find_element(By.ID, "app-header")
    assert header is not None
    assert header.text != ""

# --- Test 2: Visualisation ---
def test_visualisation_present(dash_app):
    graph = dash_app.find_element(By.ID, "main-graph")
    assert graph is not None

# --- Test 3: Region picker ---
def test_region_picker_present(dash_app):
    picker = dash_app.find_element(By.ID, "region-picker")
    assert picker is not None
