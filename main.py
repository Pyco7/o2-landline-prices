import time

from selenium import webdriver


class Scraper:
    url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
    countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

    def __init__(self, driver):
        driver.get(self.url)
        self._get_id = lambda name: driver.find_element_by_id(name)
        self._get_classes = lambda name: driver.find_elements_by_class_name(name)

    def run(self):
        print("Prices of calling a landline (per Month):\n")
        print("Price - Country")
        for country in self.countries:
            self._find_price(country)

    def _find_price(self, country):
        self._get_id("countryName").clear()
        self._get_id("countryName").send_keys(country)
        self._get_id("countryFlag").click()
        time.sleep(0.5)

        self._get_id("paymonthly").click()
        time.sleep(0.5)

        for box in self._get_classes("intrCallCardbg"):
            price = box.find_element_by_id("landLine").text
            if 'p' in price:
                print("   " + price, end="")
                break
        print("   " + country)


if __name__ == "__main__":
    firefox = webdriver.Firefox()
    try:
        Scraper(firefox).run()
    finally:
        firefox.quit()
