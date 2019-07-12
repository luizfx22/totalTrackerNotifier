from bs4 import BeautifulSoup
import requests

import json

class TotalNotifyer:
    def __init__(self, link):
        self.link = link
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
    
    def main(self):
        req = requests.get(self.link, headers={'User-Agent': self.ua})
        req.close()

        bs = BeautifulSoup(req.content, "html.parser")
        
        table = bs.find('td', attrs={"width":"51%"})
        print (table)


if __name__ == "__main__":
    l = TotalNotifyer("""https://tracking.totalexpress.com.br/tracking_encomenda.php?code=qeYm9rL%2FzUONCsHcdFBnDZdOAhK6Owza2qbdGHq6lcQ1Nl2k5EASR0PN6BEpqlYc%2BPEmW32Hj8TXD%2B9ZwHMBCmJisKFHg5ruD66XMS8vEmiMVSBpnxY5zvI0fmocxx9cmK7OAbBnT78JRP3WXnP%2FZ%2F6fiLVfwgE6voYTvfzgy0dCLK3%2F""")
    l.main()
