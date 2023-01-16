from currency_converter import CurrencyConverter

currencys = ['IDR', 'BGN', 'ILS','GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD'
            , 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'EUR', 'NOK', 'RUB'
            , 'INR', 'MXN', 'CZK', 'BRL', 'PLN','PHP', 'ZAR' , 'USD']


def welcome_message():
    message = "โปรแกรมคำนวน แปลงราคาสินค้าจากสกุลเงินต่างๆ เป็น THB ที่รวมภาษีมูลค่าเพิ่มแล้ว"
    print(message.center(88,"-"))
    print("Currency :",currencys)
    print()


def convert_currency():
    currency = input("Input Currency : ").upper()
    currency_in_list = check_currency_in_list(currency)
    while not currency_in_list:
        currency = input("Input Currency Again : ").upper()
        currency_in_list = check_currency_in_list(currency)

    price_is_number = True
    price = input("Input Price : ")
    while price_is_number:
        try:
            price = float(price)
            break
        except:
            price = input("Input Price number Only!: ")
            price_is_number = True

    currencty_converter = CurrencyConverter()
    result = currencty_converter.convert(float(price), currency, 'THB')
    include_vat(result)


def check_currency_in_list(currency):
    return currency in currencys


def include_vat(result):
    result += (result * 7) / 100
    print("Price inc. Vat :", result, "THB")


welcome_message()
convert_currency()

