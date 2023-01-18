from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, \
    QVBoxLayout, QHBoxLayout, QComboBox
from datetime import datetime
from Lab2.first_task import first_task
from Lab2.second_task import second_task
from Lab2.third_task import third_task
from Lab2.fourth_task import first_type, second_type
from Lab2.utils import get_data


class Window(QMainWindow):

    search_string: str = ''
    folder_path_for_dataset: list = ['', '', '']
    folder_path_for_new_dataset: str = ''
    folder_path_for_annotation: str = ''
    state: int = 0

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
        widget.addItems(["X/Y", "Yearly", "Weekly", "Default"])
        widget.currentIndexChanged.connect(self.index_changed)

        layout.addWidget(widget)

        date_input = QLineEdit()
        date_input.setInputMask('0000-00-00;_')
        date_input.setMaxLength(10)
        date_input.textChanged.connect(self.text_changed)
        layout.addWidget(date_input)

        value = QLabel()
        value.setText("Search result will be here")
        layout.addWidget(value)

        default_folder = QPushButton("Set default dataset folder")
        layout.addWidget(default_folder)
        annotation = QPushButton("Create dataset annotation")
        layout.addWidget(annotation)
        splice = QPushButton("Splice default dataset")
        layout.addWidget(splice)
        search = QPushButton("Get data")
        layout.addWidget(search)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def index_changed(self, i):
        self.state = i
        print(self.state)

    def text_changed(self, s):
        print("Text changed...")
        print(s)
        self.search_string = s


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.show()

    app.exec()
