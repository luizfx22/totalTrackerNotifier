import re
import os
import asyncio
import requests
import time

from bs4 import BeautifulSoup

class TotalNotifyer:
    def __init__(self, link):
        self.link = link
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
        self.date = []
        self.time = []
        self.status = []


    async def main(self, delay):   
        timer = delay * 60
        while True:
            req = requests.get(self.link, headers={'User-Agent': self.ua})
            req.close()

            bs = BeautifulSoup(req.content, "html.parser")
            bs2 = BeautifulSoup(req.content, "html.parser")
            
            table = bs.findAll('td', attrs={"width":"51%"})
            table2 = bs2.findAll('td', attrs={"width": "25%"})
            table3 = bs2.findAll('td', attrs={"width": "24%"})

            self.date.clear()
            self.time.clear()
            self.status.clear()

            for tag in table2:
                txt = tag.font.text
                self.date.append(txt.strip())

            for tag in table3:
                txt = tag.font.text
                self.time.append(txt.strip())

            for tag in table:
                txt = tag.font.text
                self.status.append(txt.strip())        
            
            self.date.pop(0)
            self.time.pop(0)
            self.status.pop(0)

            os.system("cls")

            for i in range(len(self.status)):
                print (f" >> {time.strftime('%X')}:", self.date[i], self.time[i], self.status[i])
            
            await asyncio.sleep(timer)

    async def getLoop(self):
        while True:
            a = 2 + 2
            await asyncio.sleep(0.0002)
          

if __name__ == "__main__":
    mine = """https://tracking.totalexpress.com.br/tracking_encomenda.php?code=qeYm9rL%2FzUONCsHcdFBnDZdOAhK6Owza2qbdGHq6lcQ1Nl2k5EASR0PN6BEpqlYc%2BPEmW32Hj8TXD%2B9ZwHMBCmJisKFHg5ruD66XMS8vEmiMVSBpnxY5zvI0fmocxx9cmK7OAbBnT78JRP3WXnP%2FZ%2F6fiLVfwgE6voYTvfzgy0dCLK3%2F"""
    async def yeet():
        l = TotalNotifyer(mine)
        run = asyncio.create_task(l.main(5))
        bg = asyncio.create_task(l.getLoop())
        await run
        await bg
    
    asyncio.run(yeet())
