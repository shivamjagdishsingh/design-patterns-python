from threading import Lock, Thread

class Database:
    __instance = None
    access_count = 0
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls.__instance == None:
                cls.__instance = super().__new__(cls)

            cls.access_count += 1
        return cls.__instance

def test_singleton() -> None:
    singleton = Database()
    print(singleton.access_count)

if __name__ == "__main__":
    for _ in range(1000):
        t = Thread(target=test_singleton)
        t.start()
