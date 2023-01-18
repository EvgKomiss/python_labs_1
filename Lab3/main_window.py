from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QFileDialog, QLineEdit, QLabel, \
    QVBoxLayout, QComboBox
from datetime import datetime
from Lab2.first_task import first_task
from Lab2.second_task import second_task
from Lab2.third_task import third_task
from Lab2.fourth_task import first_type, second_type, default_type
from Lab2.utils import get_data
from shutil import copyfile


class Window(QMainWindow):

    search_string: str = ''
    folder_path_for_dataset: str = '../Lab1'
    folder_path_for_new_dataset: list = ['../Lab2', '../Lab2', '../Lab2']
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

        self.setWindowTitle("Lab 3")

        layout = QVBoxLayout()

        widget = QComboBox()
        widget.addItems(["X/Y", "Yearly", "Weekly", "Default"])
        widget.currentIndexChanged.connect(self.index_changed)

        layout.addWidget(widget)

        self.value = QLabel()
        self.value.setText("Search result will be here")
        layout.addWidget(self.value)

        date_input = QLineEdit()
        date_input.setInputMask('0000-00-00;_')
        date_input.setMaxLength(10)
        date_input.textChanged.connect(self.text_changed)
        layout.addWidget(date_input)

        default_folder = QPushButton("Set default dataset folder")
        default_folder.clicked.connect(self.default_folder_func)
        layout.addWidget(default_folder)
        annotation = QPushButton("Create dataset annotation")
        annotation.clicked.connect(self.copy_func)
        layout.addWidget(annotation)
        splice = QPushButton("Splice default dataset")
        splice.clicked.connect(self.splice_func)
        layout.addWidget(splice)
        search = QPushButton("Get data")
        search.clicked.connect(self.search_func)
        layout.addWidget(search)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.show()

    def index_changed(self, i):
        self.state = i

    def text_changed(self, s):
        self.search_string = s

    def search_func(self):
        if self.state == 0:
            result = first_type(self.raw_date, self.folder_path_for_new_dataset[self.state])
        elif self.state == 1 or self.state == 2:
            print(self.raw_date, self.folder_path_for_new_dataset[self.state], self.state)
            result = second_type(self.raw_date, self.folder_path_for_new_dataset[self.state])
        else:
            result = default_type(self.raw_date, self.folder_path_for_dataset)
        self.value.setText(str(result))

    def splice_func(self):
        self.folder_func()
        if self.state < 3:
            temp = [first_task, second_task, third_task]
            temp[self.state](get_data(self.folder_path_for_dataset + "/dataset.csv"),
                             self.folder_path_for_new_dataset[self.state])

    def copy_func(self):
        self.folder_path_for_annotation = \
            QFileDialog.getExistingDirectory(self, "Select annotation folder")
        print(self.folder_path_for_annotation)
        try:
            copyfile(self.folder_path_for_dataset + "/dataset.csv",
                     self.folder_path_for_annotation + "/dataset_copy.csv")
        except FileNotFoundError:
            self.value.setText("Error occurred. Bad path")

    def default_folder_func(self):
        self.folder_path_for_dataset = QFileDialog.getExistingDirectory(self, "Select default dataset folder")
        print(self.folder_path_for_dataset)
        if len(self.folder_path_for_dataset) == 0:
            self.folder_path_for_dataset = '../Lab1'

    def folder_func(self):
        if self.state < 3:
            self.folder_path_for_new_dataset[self.state] = \
                QFileDialog.getExistingDirectory(self, "Select folder for new files")
            if len(self.folder_path_for_new_dataset[self.state]) == 0:
                self.folder_path_for_new_dataset[self.state] = './'
        print(self.folder_path_for_new_dataset)


if __name__ == '__main__':
    app = QApplication([])

    window = Window()
    window.show()

    app.exec()
