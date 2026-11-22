from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About")
        self.setGeometry(550, 100, 380, 150)

        # TODO: write your name and your real GitHub repository address
        self.info_label = QLabel(
            "Grades Correction\nWritten by: <YOUR NAME>\n"
            "GitHub: https://github.com/<YOUR-USERNAME>/<YOUR-REPO>")
        self.info_label.setOpenExternalLinks(True)

        layout = QVBoxLayout()
        layout.addWidget(self.info_label)
        self.setLayout(layout)
