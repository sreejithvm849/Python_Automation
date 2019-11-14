class PaymentPage():

    def __init__(self, driver):
        self.driver = driver

        self.FullName_TextBox_Id = "full-name"
        self.Phone_TextBox_ClassName = "form-control"
        self.email_TextBox_Id = "primary-email"
        self.confirm_email_TextBox_Id = "verify-undefined_0"
        self.CardName_TextBox_Id = "credit-card-name"
        self.CardNum_TextBox_Id = "credit-card-number"
        self.CardExpiry_TextBox_Id = "credit-card-expiry"
        self.CardCVV_TextBox_Id = "credit-card-cvv"
        self.Conform_Button_Xpath = '//*[@id="checkout-book-button"]/div/div[2]/p'

    def enter_full_name(self, full_name):
        self.driver.find_element_by_id(self.FullName_TextBox_Id).send_keys(full_name)

    def enter_phone_num(self, phn_num):
        self.driver.find_element_by_class_name(self.Phone_TextBox_ClassName).send_keys(phn_num)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_TextBox_Id).send_keys(email)

    def enter_confirm_email(self,confirm_email):
        self.driver.find_element_by_id(self.confirm_email_TextBox_Id).send_keys(confirm_email)

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0,500)")

    def enter_card_name(self, crd_name):
        self.driver.find_element_by_id(self.CardName_TextBox_Id).send_keys(crd_name)

    def enter_card_number(self, crd_num):
        self.driver.find_element_by_id(self.CardNum_TextBox_Id).send_keys(crd_num)

    def enter_card_expiry(self, crd_expiry):
        self.driver.find_element_by_id(self.CardExpiry_TextBox_Id).send_keys(crd_expiry)

    def enter_card_cvv(self, cvv):
        self.driver.find_element_by_id(self.CardCVV_TextBox_Id).send_keys(cvv)

    def click_confirm(self):
        self.driver.find_element_by_xpath(self.Conform_Button_Xpath).click()
