import asyncio
from selenium import webdriver
from time import sleep

PATH = 'C:\Program Files (x86)\geckodriver.exe'

async def main():
    '''Main function to play youtube video'''

    url = 'https://www.youtube.com'
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get(url)
    
    yt_channel = 'youtube channel name'     
    
    query = driver.find_element_by_name('search_query')
    query.send_keys(yt_channel)
    
    search_btn = driver.find_element_by_id("search-icon-legacy").click()
    
    vid = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer[1]/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[1]').click()
    
    sleep(120) # max video play time 

    driver.quit()

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print('Code Completed 🔥')