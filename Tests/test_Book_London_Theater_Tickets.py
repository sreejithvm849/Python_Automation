import time
import unittest
import HtmlTestRunner

from selenium import webdriver

from london_theater.XTUtils.XTUtils import XTUtils
from london_theater.Pages.Home_page import HomePage
from london_theater.Pages.Booking_page import BookingPage
from london_theater.Pages.Payment_Page import PaymentPage


class LondonTicketBooking(unittest.TestCase):
    driver: webdriver

    @classmethod
    #setUpClass method which open chrome browser and opens links.
    def setUpClass(cls):

        #copy the and paste chrome driver path from London_theater>drivers>Chromedriver.exe
        cls.driver = webdriver.Chrome(
            executable_path="london_theater/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://www.london-theater-tickets.com/")

    #this method checks the home page validation of Book London Theater Tickets website.
    def test_home_page_Valid(self):
        homepage = HomePage(self.driver)
        homepage.enter_search(XTUtils.Search_value)
        homepage.click_search_item()
        time.sleep(2)
        homepage.click_book_now()

    #this method checks the booking page validation about date & seats  of Book London Theater Tickets website
    def test_booking_page_valid(self):
        booking = BookingPage(self.driver)
        booking.click_date()
        time.sleep(2)
        booking.click_seat()
        booking.click_next()
 
    #this method checks the payment page validation about personal details in Book London Theater Tickets website.
    def test_payment_page_Details_valid(self):
        personal_details = PaymentPage(self.driver)
        personal_details.enter_full_name(XTUtils.Full_name)
        personal_details.enter_phone_num(XTUtils.Phone_number)
        personal_details.enter_email(XTUtils.Email)
        personal_details.enter_confirm_email(XTUtils.Email)
        personal_details.scroll_page()
        time.sleep(2)

    #this method checks the payment page validation about payment details in Book London Theater Tickets website.
    def test_payment_page_Payment_Details_valid(self):
        payment_details = PaymentPage(self.driver)
        payment_details.enter_card_name(XTUtils.Full_name)
        payment_details.enter_card_number(XTUtils.Card_number)
        payment_details.enter_card_expiry(XTUtils.Card_expiry)
        payment_details.enter_card_cvv(XTUtils.Card_cvv)
        payment_details.click_confirm()
        time.sleep(5)

    #this tearDownClass method closes the chrome browser.
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="london_theater/reports"))
