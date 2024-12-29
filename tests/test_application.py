
# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options


# class TestApplication(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         # Configure the Edge WebDriver with headless mode
#         options = Options()
#         options.add_argument('headless')
#         options.add_argument('disable-gpu')
#         cls.driver = webdriver.Edge(options=options)
#         cls.base_url = "http://localhost:3000"

#     @classmethod
#     def tearDownClass(cls):
#         # Quit the driver after all tests
#         cls.driver.quit()

#     def test_homepage_title(self):
#         """Test Case 1: Verify Homepage Title"""
#         self.driver.get(self.base_url)
#         self.assertIn("Basic App", self.driver.title)
#         print("Test 1 Passed: Homepage title verified")

#     def test_navigate_to_register(self):
#         """Test Case 2: Navigate to Registration Page"""
#         self.driver.get(self.base_url)
#         self.driver.find_element(By.LINK_TEXT, "Register").click()
#         self.assertIn("Register", self.driver.title)
#         print("Test 2 Passed: Navigation to Register page verified")

#     def test_register_user(self):
#         """Test Case 3: Registration Form Submission"""
#         self.driver.get(f"{self.base_url}/register")
#         self.driver.find_element(By.NAME, "username").send_keys("e")
#         self.driver.find_element(By.NAME, "password").send_keys("e")
#         self.driver.find_element(
#             By.XPATH, "//button[text()='Register']").click()

#         print("register: ", self.driver.title)

#         self.assertIn("Login", self.driver.title)
#         print("Test 3 Passed: User registration verified")

#     def test_login_user(self):
#         """Test Case 4: Login Form Submission"""
#         self.driver.get(f"{self.base_url}/login")
#         self.driver.find_element(By.NAME, "username").send_keys("d")
#         self.driver.find_element(By.NAME, "password").send_keys("d")
#         self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
#         print("login: ", self.driver.title)
#         print(self.driver.current_url)
#         self.assertIn("Dashboard", self.driver.title)

#         print("Test 4 Passed: User login verified")

#     def test_invalid_login(self):
#         """Test Case 5: Login with Invalid Credentials"""
#         self.driver.get(f"{self.base_url}/login")
#         self.driver.find_element(By.NAME, "username").send_keys("invaliduser")
#         self.driver.find_element(
#             By.NAME, "password").send_keys("wrongpassword")
#         self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
#         self.assertIn("Invalid", self.driver.page_source)
#         print("Test 5 Passed: Invalid login detected")


# # Run tests when the file is executed
# if __name__ == "__main__":
#     unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service


class TestApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure the Chrome WebDriver with headless mode
        options = Options()
        options.add_argument('headless')  # Optional: for headless mode
        options.add_argument('disable-gpu')  # Optional: for headless mode

        # Provide full path to the downloaded chromedriver
        chromedriver_path = r"C:\Files\Uni\S7\DevOps\chromedriver-win64\chromedriver-win64\chromedriver.exe"

        # Initialize the Chrome WebDriver with the Service
        service = Service(chromedriver_path)
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.base_url = "http://localhost:3000"

    @classmethod
    def tearDownClass(cls):
        # Quit the driver after all tests
        cls.driver.quit()

    def test_homepage_title(self):
        """Test Case 1: Verify Homepage Title"""
        self.driver.get(self.base_url)
        self.assertIn("Basic App", self.driver.title)
        print("Test 1 Passed: Homepage title verified")

    def test_navigate_to_register(self):
        """Test Case 2: Navigate to Registration Page"""
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.assertIn("Register", self.driver.title)
        print("Test 2 Passed: Navigation to Register page verified")

    def test_register_user(self):
        """Test Case 3: Registration Form Submission"""
        self.driver.get(f"{self.base_url}/register")
        self.driver.find_element(By.NAME, "username").send_keys("f")
        self.driver.find_element(By.NAME, "password").send_keys("f")
        self.driver.find_element(
            By.XPATH, "//button[text()='Register']").click()

        print("Test 3 Passed: User registration verified")

    def test_login_user(self):
        """Test Case 4: Login Form Submission"""
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("d")
        self.driver.find_element(By.NAME, "password").send_keys("d")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()

        self.assertIn("Dashboard", self.driver.title)

        print("Test 4 Passed: User login verified")

    def test_invalid_login(self):
        """Test Case 5: Login with Invalid Credentials"""
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("invaliduser")
        self.driver.find_element(
            By.NAME, "password").send_keys("wrongpassword")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()
        self.assertIn("Invalid", self.driver.page_source)
        print("Test 5 Passed: Invalid login detected")


# Run tests when the file is executed
if __name__ == "__main__":
    unittest.main()
