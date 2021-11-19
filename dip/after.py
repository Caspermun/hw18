import sys
import time

# DIP - Зависимость на абстракциях, нет зависимости на что-то конкретное

class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())


    def log(self, message, notifier):  # notifier - абстракция
        notifier().write(f"{self.prefix} {message}")


logger = Logger()
logger.log("Starting the program...", TerminalPrinter)  # Передали класс
logger.log("An error!", FilePrinter)