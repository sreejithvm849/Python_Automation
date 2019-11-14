import openpyxl


class XTUtils:
    #Create a new Excel Sheet in the same directory. Copy and paste the path below
    vk = openpyxl.load_workbook("london_theater/XTUtils/data.xlsx")
    sh = vk["Sheet1"]
    Search_value = sh['A1'].value
    Full_name = sh['A2'].value
    Phone_number = sh['A3'].value
    Email = sh['A4'].value
    Card_number = sh['A5'].value
    Card_expiry = sh['A6'].value
    Card_cvv = sh['A7'].value
