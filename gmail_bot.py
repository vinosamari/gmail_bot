from selenium import webdriver
import time

#Instantiate the selenium chromedriver
driver = webdriver.Chrome(
    "/Users/FEM_I/Documents/PYTHON DOCS/BOTS/gmail_creator_bot/chromedriver"
)

#set url variable
gmail_url = """
https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S-570253040%3A1599936062576243&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp
"""

#acoount creation function
def create_account(url):
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_xpath("//*[@id= 'firstName']").send_keys("yourfirstname")
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys("yourlastname")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys("youruniqueusername")
    driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input').send_keys(
        "yourprivatepassword123"
    )
    driver.find_element_by_xpath(
        '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'
    ).send_keys("yourprivatepassword123")
    driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/span').click()


if __name__ == "__main__":
    
