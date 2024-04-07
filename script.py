from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# Replace these with your actual login credentials and desired job search
LINKEDIN_USERNAME = 'test@gmail.com'
LINKEDIN_PASSWORD = 'test@1234'
JOB_SEARCH_QUERY = 'Java Developer'
JOB_SEARCH_LOCATION = 'United States'

def initialize_driver():
    # Setup Chrome WebDriver using the Service class and ChromeDriverManager.
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def login_to_linkedin(driver):
    # Navigate to LinkedIn's login page
    driver.get('https://www.linkedin.com/login')
    sleep(2)  # Wait for the page to load
    
    # Enter login credentials
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys(LINKEDIN_USERNAME)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(LINKEDIN_PASSWORD)
    
    # Click the login button
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(2)  # Wait for login to complete
    
def search_jobs(driver):
    # Navigate to the jobs page and enter search criteria
    driver.get('https://www.linkedin.com/jobs')
    sleep(3)
    
    # Enter job search query
    search_box = driver.find_element(By.XPATH, '//input[@aria-label="Search by title, skill, or company"]')
    search_box.send_keys(JOB_SEARCH_QUERY)
    
    # Enter location
    location_box = driver.find_element(By.XPATH, "//input[@aria-label='City, state, or zip code']")
    

    location_box.clear()  # Clear any pre-filled location
    location_box.send_keys(JOB_SEARCH_LOCATION)
    
    # Start the search
    search_box.send_keys(Keys.RETURN)
    sleep(10)  # Wait for the search results to load

def apply_to_jobs(driver):
    # This is a simplified version. Real job applications might require more complex interactions.
    # Find job listings
    job_listings = driver.find_elements(By.CSS_SELECTOR, 'ul.scaffold-layout__list-container li')
    for job in job_listings:
        job.click()
        sleep(1)
        
        # Attempt to click the "Easy Apply" button if it exists
        try:
            easy_apply_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.jobs-apply-button'))
            )
            easy_apply_button.click()
            sleep(10)

            # Submit the application. You might need to handle additional steps depending on the job.
            submit_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-control-name="submit_unify"]'))
            )
            submit_button.click()
            sleep(10)
            
            # Close the "application submitted" modal if it appears
            close_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-modal-close-btn]'))
            )
            close_button.click()
            sleep(10)
            
        except Exception as e:
            print("Could not apply to job:", e)
            continue  # Skip to the next job if any step fails
driver = initialize_driver()
#login_to_linkedin(driver)
search_jobs(driver)
apply_to_jobs(driver)
driver.quit()

