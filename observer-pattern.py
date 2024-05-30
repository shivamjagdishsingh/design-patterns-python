from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def notify(self):
        pass

class SmsOTP(Observer):
    def notify(self):
        print("OTP sent on SMS")

class EmailOTP(Observer):
    def notify(self):
        print("OTP sent on Email")

class WhatsAppOTP(Observer):
    def notify(self):
        print("OTP sent on Whatsapp")

class Observers:
    _observers = []

    def add_observer(self, observer: Observer):
        if isinstance(observer, Observer):
            self._observers.append(observer)
            print("New observer added")
    
    def send_otp(self):
        for observer in self._observers:
            observer.notify()

if __name__=="__main__":
    devices = Observers()
    devices.add_observer(SmsOTP())
    devices.add_observer(EmailOTP())
    devices.add_observer(WhatsAppOTP())
    devices.send_otp()
