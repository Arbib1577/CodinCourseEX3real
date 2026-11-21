import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QFileDialog
from PySide6.QtGui import QIntValidator
from About import AboutWindow

class GradesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grades Manager')
        self.setGeometry(250,120,560,620)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.load_btn = QPushButton('Select Grades File', self)
        self.load_btn.setGeometry(30,20,180,38)
        self.load_btn.clicked.connect(self.load_file)

        self.file_label = QLabel('No file selected', self)
        self.file_label.setGeometry(225,20,305,38)

        self.bonus_label = QLabel('Bonus Points (Press Enter):', self)
        self.bonus_label.setGeometry(30,75,220,35)

        self.bonus_input = QLineEdit(self)
        self.bonus_input.setGeometry(255,75,100,35)
        self.bonus_input.setValidator(QIntValidator(-100,100))
        self.bonus_input.returnPressed.connect(self.apply_bonus)

        self.table = QTableWidget(50,3, self)
        self.table.setGeometry(30,130,500,400)
        self.table.setHorizontalHeaderLabels(['ID', 'Original Grades', 'Corrected Grades'])
        self.table.setColumnWidth(0, 155)
        self.table.setColumnWidth(1, 155)
        self.table.setColumnWidth(2, 155)

        self.update_btn = QPushButton('Update File', self)
        self.update_btn.setObjectName('update_btn')
        self.update_btn.setGeometry(30, 550, 180, 40)
        self.update_btn.clicked.connect(self.update_file)

        self.about_btn = QPushButton('About', self)
        self.about_btn.setObjectName('about_btn')
        self.about_btn.setGeometry(410,550,120,40)
        self.about_btn.clicked.connect(self.open_about)

        self.about_window = None

    def update_table(self):
        self.table.clearContents()
        for i in range(len(self.student_ids)):
            self.table.setItem(i,0, QTableWidgetItem(str(self.student_ids[i])))
            self.table.setItem(i,1, QTableWidgetItem(str(self.original_grades[i])))
            self.table.setItem(i,2, QTableWidgetItem(str(self.corrected_grades[i])))

    def load_file(self):
        pass
    def apply_bonus(self):
        pass
    def update_file(self):
        pass
    def open_about(self):
        if self.about_window is None:
            self.about_window = AboutWindow()
        self.about_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = GradesWindow()
    window.show()
    sys.exit(app.exec())