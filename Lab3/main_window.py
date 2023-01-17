from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QComboBox
from datetime import datetime


class Window(QMainWindow):

    search_string: str = ''

    @property
    def raw_date(self):
        try:
            date = datetime.strptime(self.search_string, '%Y-%m-%d').date()
        except ValueError:
            date = datetime(2021, 7, 26).date()
        return date

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        widget = QComboBox()
        widget.addItems(["Task 0", "Task 1", "Task 2", "Task 3"])
        widget.currentIndexChanged.connect(self.index_changed)

        layout.addWidget(widget)

        date_input = QLineEdit()
        date_input.setInputMask('0000-00-00;_')
        date_input.setMaxLength(10)
        date_input.returnPressed.connect(self.return_pressed)
        date_input.textChanged.connect(self.text_changed)

        layout.addWidget(date_input)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def index_changed(self, i):
        print(i)

    def return_pressed(self):
        print(self.raw_date)

    def text_changed(self, s):
        print("Text changed...")
        print(s)
        self.search_string = s


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.show()

    app.exec()
