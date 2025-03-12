import threading
import os
import time
from client import IBClient
from wrapper import IBWrapper
from contract import stock
from order import limit, BUY
from dotenv import load_dotenv


class IBApp(IBWrapper, IBClient):
    def __init__(self, ip, port, client_id):
        IBWrapper.__init__(self)
        IBClient.__init__(self, wrapper=self)
        self.connect(ip, port, client_id)

        thread = threading.Thread(target=self.run, daemon=True)
        thread.start()
        time.sleep(2)
   
if __name__ == "__main__":
    load_dotenv()
    app = IBApp(os.getenv("LOCALHOST"), 7497, client_id=10)
    aapl = stock("TUYA", "SMART", "USD")
    limit_order = limit(BUY, 100, 3.89)
    time.sleep(30)
    app.disconnect()