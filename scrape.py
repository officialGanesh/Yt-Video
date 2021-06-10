from selenium import webdriver
import asyncio


PATH = 'C:\Program Files (x86)\geckodriver.exe'

async def main():
    '''Main function to play youtube video'''

    url = 'https://www.youtube.com'
    driver = webdriver.Firefox(executable_path=PATH)
    driver.get(url)



    driver.quit()

if __name__ == '__main__':

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    print('Code Completed 🔥')