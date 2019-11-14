class BookingPage():

    def __init__(self, driver):
        self.driver = driver

        self.Date_Button_xpath = \
            '//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]'

        self.Iframe_Switch_tag_name = 'iframe'

        self.Seat_Button_xpath = \
            './/*[@id="seatmap"]//*[name()="svg"]/*[name()="g"]/*[name()="g"]/*[name()="g"]/*[name()="svg"]/*' \
            '[name()="g"][5]/*[name()="g"][8]/*[name()="circle"][6]'

        self.Next_Button_xpath = '/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[3]'

    def click_date(self):
        elem = self.driver.find_element_by_xpath(self.Date_Button_xpath)
        if elem.is_enabled():
            self.driver.find_element_by_xpath(self.Date_Button_xpath).click()
        else:
            print("Element not clickable")

    def click_seat(self):
        iframe = self.driver.find_elements_by_tag_name(self.Iframe_Switch_tag_name)[0]
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(self.Seat_Button_xpath).click()

    def click_next(self):
        self.driver.switch_to_default_content()
        self.driver.find_element_by_xpath(self.Next_Button_xpath).click()
