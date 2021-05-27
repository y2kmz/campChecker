import sendMail
from selenium import webdriver
from selenium.webdriver.support.select import Select


def checkArea(areaText):
    try:
        driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        # driver = webdriver.Chrome()
        driver.get("http://www.muji.net/camp/")
        driver.implicitly_wait(1)

        driver.find_element_by_link_text("空き状況を見る").click()
        driver.implicitly_wait(1)
        driver.switch_to.window(driver.window_handles.pop())

        campSite = driver.find_element_by_name("CAMP_JO")
        Select(campSite).select_by_visible_text("無印良品カンパーニャ嬬恋キャンプ場")
        driver.implicitly_wait(1)

        siteYear = driver.find_element_by_name("SITE_YEA")
        siteMonth = driver.find_element_by_name("SITE_MON")
        Select(siteYear).select_by_value('2021')
        Select(siteMonth).select_by_value('7')

        driver.find_element_by_name("SEARCH_SITE").click()
        driver.implicitly_wait(1)
        driver.switch_to.window(driver.window_handles.pop())

        driver.find_element_by_link_text(areaText).click()
        driver.implicitly_wait(1)

        seekTRs = driver.find_elements_by_xpath("//*[@id='door_stock_table_body']/table/tbody/tr")

        for trElement in seekTRs:
            # tdElements = trElement.find_elements_by_class_name("td_site_zaikoh")
            trStrAll = str(trElement.text)
            trStr24_25 = trStrAll[trStrAll.find("●"):][46:49]
            print(trStr24_25)
            if trStr24_25 == "● ●":
                print(areaText + "の席があり")
                sendMail.sendMails(areaText)

        driver.quit()
        driver.implicitly_wait(1)
    except Exception:
        pass


# checkArea("Aエリア")
