from selenium import webdriver
from selenium.webdriver.common.by import By
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

chrome_driver_path = "/Users/navodanilakshi/Documents/Development/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)

cookie = driver.find_element(By.ID, "cookie")


def check_upgrades():
    cur_score = driver.find_element(By.ID, "money")
    items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    award_prices = [item.find_element(By.TAG_NAME, "b").text.split("-")[-1].strip().replace(",", "") for item in
                    items]
    award_prices.pop()
    prices_ints = [int(n) for n in award_prices]
    eligible_prize = min(prices_ints, key=lambda x: abs(x - cur_score))
    match = items[prices_ints.index(eligible_prize)]
    match.click()

while True:
    cookie.click()
    sched.add_job(check_upgrades, 'interval', seconds=5)
