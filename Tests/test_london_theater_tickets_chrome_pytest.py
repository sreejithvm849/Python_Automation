import time
import pytest

from selenium import webdriver

from XTUtils.XTUtils import XTUtils
from Pages.Home_page import HomePage
from Pages.Booking_page import BookingPage
from Pages.Payment_Page import PaymentPage


@pytest.fixture(scope="module")
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/Vinay/Documents/automation/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.london-theater-tickets.com/")

    yield

    driver.close()
    driver.quit()


def test_home_page_Valid(test_setup):
    homepage = HomePage(driver)
    homepage.enter_search(XTUtils.Search_value)
    homepage.click_search_item()
    time.sleep(2)
    homepage.click_book_now()
    title = driver.title
    print(title)
    assert title == "The Simon and Garfunkel Story London | Best Prices on West End Tickets"

    # this method checks the booking page validation about date & seats  of Book London Theater Tickets website


def test_booking_page_valid(test_setup):
    booking = BookingPage(driver)
    booking.click_date()
    time.sleep(2)
    booking.click_seat()
    booking.click_next()
    time.sleep(2)
    assert "Full Name" == "Full Name"

    # this method checks the payment page validation about personal details in Book London Theater Tickets website.


def test_payment_page_Details_valid(test_setup):
    personal_details = PaymentPage(driver)
    personal_details.enter_full_name(XTUtils.Full_name)
    personal_details.enter_phone_num(XTUtils.Phone_number)
    personal_details.enter_email(XTUtils.Email)
    personal_details.enter_confirm_email(XTUtils.Email)
    personal_details.scroll_page()
    time.sleep(2)
    title = driver.title
    print(title)
    assert "Credit Card Number" == "Credit Card Number"

    # this method checks the payment page validation about payment details in Book London Theater Tickets website.


def test_payment_page_Payment_Details_valid(test_setup):
    payment_details = PaymentPage(driver)
    payment_details.enter_card_name(XTUtils.Full_name)
    payment_details.enter_card_number(XTUtils.Card_number)
    payment_details.enter_card_expiry(XTUtils.Card_expiry)
    payment_details.enter_card_cvv(XTUtils.Card_cvv)
    payment_details.click_confirm()
    time.sleep(5)
