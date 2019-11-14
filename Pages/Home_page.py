class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.Serach_Textbox_xpath = "/html/body/div[1]/div[2]/section/div[1]/div[1]/form/input"
        self.SearchItem_Button_class_name = "title"
        self.BookNow_Button_tag_name = "body"

    def enter_search(self, search_name):
        self.driver.find_element_by_xpath(self.Serach_Textbox_xpath).send_keys(search_name)

    def click_search_item(self):
        self.driver.find_element_by_class_name(self.SearchItem_Button_class_name).click()

    def click_book_now(self):
        elem = self.driver.find_element_by_class_name("button")
        if elem.is_enabled():
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get('https://book.london-theater-tickets.com/book/7233')
        else:
            print("button not clickable")
