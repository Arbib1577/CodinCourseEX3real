from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About Me')
        self.setGeometry(250, 150, 380, 580)
        self.setStyleSheet('background-color: #FAA18F;')

        self.name_label = QLabel('Name: Yehonatan Arbib', self)
        self.name_label.setGeometry(30, 20, 300, 30)
        self.name_label.setStyleSheet('font-size: 18px; font-weight: bold; color: #2f3640;')

        self.role_label = QLabel('Mechanical Engineering Student - Afeka', self)
        self.role_label.setGeometry(30, 50, 300, 30)
        self.role_label.setStyleSheet('font-size: 16px; color: #353b48;')

        self.email_label = QLabel('Email: Jonathan.Arbib@s.afeka.ac.il', self)
        self.email_label.setGeometry(30, 80, 300, 30)
        self.email_label.setStyleSheet('font-size: 16px; color: #353b48;')

        self.linkedin_label = QLabel('<a href="https://www.linkedin.com/in/jenhsunhuang">My LinkedIn Profile</a>', self)
        self.linkedin_label.setGeometry(30, 110, 300, 25)
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel('<a href="https://github.com/Arbib1577/CodinCourseEX3real">GitHub Repository</a>', self)
        self.github_label.setGeometry(30, 135, 300, 25)
        self.github_label.setOpenExternalLinks(True)

        self.my_picture = QLabel(self)
        self.my_picture.setGeometry(30, 170, 300, 270)
        self.my_picture.setStyleSheet('border: 2px solid #7f8fa6; background-color: white;')

        image = QPixmap('Best_Image.png').scaled(300, 270)
        self.my_picture.setPixmap(image)

        # bonus
        self.btn_copy = QPushButton('Copy', self)
        self.btn_copy.setGeometry(295, 80, 65, 25)
        self.btn_copy.setStyleSheet('background-color: #dcdde1;')
        self.btn_copy.clicked.connect(self.copy_email)

        self.status_label = QLabel('', self)
        self.status_label.setGeometry(40, 505, 300, 30)
        self.status_label.setStyleSheet('color: #192a56; font-weight: bold;')

        # bonus
        self.pat_counter = 0
        self.btn_pat = QPushButton('Say Hi (0)', self)
        self.btn_pat.setGeometry(40, 455, 140, 35)
        self.btn_pat.setStyleSheet('background-color: #4cd137; font-weight: bold;')
        self.btn_pat.clicked.connect(self.say_hi)

        # bonus
        self.btn_close = QPushButton('Close', self)
        self.btn_close.setGeometry(200, 455, 140, 35)
        self.btn_close.setStyleSheet('background-color: #e84118; color: white; font-weight: bold;')
        self.btn_close.clicked.connect(self.close)

    # bonus
    def copy_email(self):
        QApplication.clipboard().setText('Jonathan.Arbib@s.afeka.ac.il')
        self.status_label.setText('Email copied to clipboard!')

    # bonus
    def say_hi(self):
        self.pat_counter = self.pat_counter + 1
        self.btn_pat.setText(f'Say Hi ({self.pat_counter})')
        if self.pat_counter % 3 == 0:
            self.status_label.setText('The Monkey is looking away...')
        else:
            self.status_label.setText('Thanks for checking my project!')


if __name__ == '__main__':
    app = QApplication()
    window = AboutWindow()
    window.show()
    app.exec()