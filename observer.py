# Let us say we have a stock price monitoring system where with each stock price change we have to send notification on E-mail and SMS

# =========  The Bad Design ============ #

class Stock:
    def __init__ (self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new_price):
        self.price = new_price
        print(f"The new price of {self.name} is ${self.price}")


class Dashboard:
    def __init__ (self, stock):
        self.stock = stock


    def update(self):
        print(f"Dashboard updated: {self.stock.name} is now ${self.stock.price}")


class EmailAlert:
    def __init__ (self, stock):
        self.stock = stock

    def send_email(self):
        print(f"Email Alert: {self.stock.name} price updated to ${self.stock.price}")


class SMSAlert:
    def __init__ (self, stock):
        self.stock = stock

    def send_sms(self):
        print(f"SMS Alert: {self.stock.name} price updated to ${self.stock.price}")


# Usage
apple_stock = Stock("AAPL", 150)
dashboard = Dashboard(apple_stock)
email_alert = EmailAlert(apple_stock)
sms_alert = SMSAlert(apple_stock)


# Update stock price
apple_stock.set_price(155)
dashboard.update()
email_alert.send_email()
sms_alert.send_sms()



# =========  The OBSERVER Design Pattern ============ #

from typing import List

class Stock:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        self.observers: List = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self)

    def set_price(self, new_price):
        self.price = new_price
        print(f"The new price of {self.name} is ${self.price}")
        self.notify_observer()

class Observer:
    def update(self, stock):
        raise NotImplementedError("This method should be overriden by subclasses")



class Dashboard(Observer):
    def update(self, stock):
        print(f"Dashboard updated: {stock.name} is now ${stock.price}")


class EmailAlert(Observer):
    def update(self, stock):
        print(f"Email Alert: {stock.name} price updated to ${stock.price}")


class SMSAlert(Observer):
    def update(self, stock):
        print(f"SMS Alert: {stock.name} price updated to ${stock.price}")



# Usage
apple_stock = Stock("AAPL", 150)
tesla_stock = Stock("TSLA", 500)


# Observer
dashboard = Dashboard()
email_alerts = EmailAlert()
sms_alerts = SMSAlert()


apple_stock.add_observer(dashboard)
apple_stock.add_observer(email_alerts)
apple_stock.add_observer(sms_alerts)


tesla_stock.add_observer(dashboard)
tesla_stock.add_observer(email_alerts)


# Events
apple_stock.set_price(200)
tesla_stock.set_price(520)
apple_stock.set_price(250)
