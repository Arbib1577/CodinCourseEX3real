import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QFileDialog,
    QSpinBox
)

from About import AboutWindow


class GradesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grades Manager')
        self.setGeometry(250, 120, 560, 620)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.load_btn = QPushButton('Select Grades File', self)
        self.load_btn.setGeometry(30, 20, 180, 38)
        self.load_btn.clicked.connect(self.load_file)

        self.file_label = QLabel('No file selected', self)
        self.file_label.setGeometry(225, 20, 305, 38)

        self.id_label = QLabel('Select Student ID:', self)
        self.id_label.setGeometry(30, 72, 200, 35)

        self.id_combo = QComboBox(self)
        self.id_combo.setGeometry(255, 72, 160, 35)
        self.id_combo.currentTextChanged.connect(self.reset_bonus)

        self.bonus_label = QLabel('Bonus Points:', self)
        self.bonus_label.setGeometry(30, 120, 200, 35)

        self.bonus_input = QSpinBox(self)
        self.bonus_input.setGeometry(255, 120, 100, 35)
        self.bonus_input.setRange(-100, 100)
        self.bonus_input.valueChanged.connect(self.apply_bonus)

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(30, 170, 500, 360)
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
        self.about_btn.setGeometry(410, 550, 120, 40)
        self.about_btn.clicked.connect(self.open_about)

        self.about_window = None

    def update_table(self):
        self.table.clearContents()
        for i in range(len(self.student_ids)):
            self.table.setItem(i,0, QTableWidgetItem(str(self.student_ids[i])))
            self.table.setItem(i,1, QTableWidgetItem(str(self.original_grades[i])))
            self.table.setItem(i,2, QTableWidgetItem(str(self.corrected_grades[i])))

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select Grage File', "", 'CSV File (*.csv);;All Files(*)')
        if not file_path:
            return
        self.selected_file=file_path
        self.file_label.setText(file_path.split('/')[-1])

        self.student_ids = []
        self.original_grades=[]
        self.corrected_grades =[]

        with open(self.selected_file, 'r') as f:
            lines = f.readlines()

        for line in lines[1:]:
            line=line.strip()
            if line != '':
                parts = line.split(',')
                student_id = parts[0]
                grade = int(parts[1])

                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)
        self.id_combo.clear()
        self.id_combo.addItems(self.student_ids)
        self.update_table()

    def reset_bonus(self):
        self.bonus_input.blockSignals(True)
        self.bonus_input.setValue(0)
        self.bonus_input.blockSignals(False)

    def apply_bonus(self):
        selected_id = self.id_combo.currentText()
        if selected_id == '':
            return

        bonus = self.bonus_input.value()
        for i in range(len(self.student_ids)):
            if self.student_ids[i] == selected_id:
                new_grade = self.original_grades[i] + bonus
                if new_grade > 100:
                    new_grade = 100
                if new_grade < 0:
                    new_grade = 0
                self.corrected_grades[i] = new_grade
                break

        self.update_table()
        
    def update_file(self):
        if self.selected_file == '':
            return

        with open(self.selected_file, 'w') as f:
            f.write('ID,Grade\n')
            for i in range(len(self.student_ids)):
                f.write(f'{self.student_ids[i]},{self.corrected_grades[i]}\n')

        msg = QDialog(self)
        msg.setWindowTitle('Success')
        msg.setGeometry(400, 300, 260, 110)
        lbl = QLabel('File updated successfully!', msg)
        lbl.setGeometry(45, 35, 180, 30)
        msg.exec()

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