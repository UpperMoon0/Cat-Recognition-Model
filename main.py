from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from model_test import test_model
from model_train import train_model
import sys


# Create a QThread subclass to run the training and testing functions in a separate thread
class Worker(QThread):
    signal = pyqtSignal(str)

    def __init__(self, func):
        super().__init__()
        self.func = func

    def run(self):
        self.func()
        self.signal.emit('Finished')


# Create a QWidget subclass for the main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.test_button = None
        self.train_button = None
        self.text_edit = None
        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.train_button = QPushButton('Train Model')
        self.test_button = QPushButton('Test Model')

        self.train_button.clicked.connect(train_model)
        self.test_button.clicked.connect(test_model)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.train_button)
        layout.addWidget(self.test_button)

        self.setLayout(layout)

    def start_training(self):
        self.train_worker = Worker(train_model)
        self.train_worker.signal.connect(self.update_text_edit)
        self.train_worker.start()

    def start_testing(self):
        self.test_worker = Worker(test_model)
        self.test_worker.signal.connect(self.update_text_edit)
        self.test_worker.start()

    def update_text_edit(self, text):
        self.text_edit.append(text)


# Create a QApplication and show the main window
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
