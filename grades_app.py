import os
import subprocess
import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton,
                               QSpinBox, QTableWidget, QTableWidgetItem, QFileDialog,
                               QVBoxLayout, QHBoxLayout)

from about_window import AboutWindow


def open_with_default_program(path):
    """Opens a file with the default program (Excel for csv) on Windows, macOS and Linux."""
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform == "darwin":
        subprocess.run(["open", path])
    else:
        subprocess.run(["xdg-open", path])


class GradesWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''
        self.about_window = AboutWindow()    # created, but hidden until About is clicked
        self.initUI()

    # ------------- the interface (the part AI is allowed to write) -------------
    def initUI(self):
        self.setWindowTitle("Grades Correction")
        self.setGeometry(100, 100, 520, 700)

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.title_label = QLabel("Grades Correction")
        self.title_label.setObjectName("title")

        self.load_button = QPushButton("Load Students File")
        self.load_button.clicked.connect(self.load_clicked)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(["ID", "Grades Original", "Corrected Grades"])
        self.table.horizontalHeader().setStretchLastSection(True)

        self.points_label = QLabel("Bonus points:")
        self.points_spin = QSpinBox()
        self.points_spin.setRange(0, 100)
        self.points_spin.editingFinished.connect(self.points_entered)   # Enter, or leaving the box

        self.update_button = QPushButton("File Update")
        self.update_button.setObjectName("update")
        self.update_button.clicked.connect(self.file_update_clicked)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("about")
        self.about_button.clicked.connect(self.about_clicked)

        points_layout = QHBoxLayout()
        points_layout.addWidget(self.points_label)
        points_layout.addWidget(self.points_spin)
        points_layout.addStretch()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.load_button)
        main_layout.addWidget(self.table)
        main_layout.addLayout(points_layout)
        main_layout.addWidget(self.update_button)
        main_layout.addWidget(self.about_button)
        self.central.setLayout(main_layout)

    def update_table(self):
        """Fills the table from the three lists (generated method)."""
        self.table.clearContents()
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(str(self.student_ids[row])))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def about_clicked(self):
        self.about_window.show()

    # ------------- YOUR PART: write it yourself, as we learned in class -------------
    def load_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose the students file", "", "CSV files (*.csv)")
        if file_name == '':
            return
        self.selected_file = file_name
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(self.selected_file, "r") as f:
            self.header = f.readline()
            for line in f:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split(",")
                student_id = parts[0]
                grade = int(parts[1])
                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)

        self.update_table()

    def points_entered(self):
        points = self.points_spin.value()
        
        for i in range(len(self.original_grades)):
            new_grade = self.original_grades[i] + points
            if new_grade > 100:
                new_grade = 100
            self.corrected_grades[i] = new_grade

        self.update_table()

    def file_update_clicked(self):
        # TODO: overwrite self.selected_file - same headers, only the corrected grades.
        #       Then open it:  open_with_default_program(self.selected_file)
        pass


if __name__ == "__main__":
    app = QApplication()

    with open("style.qss") as f:
        app.setStyleSheet(f.read())

    window = GradesWindow()
    window.show()
    app.exec()
