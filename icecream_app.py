from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton,
                               QFileDialog, QVBoxLayout)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

from about_window import AboutWindow


class IceCreamWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []
        self.about_window = AboutWindow()    # created, but hidden until About is clicked
        self.initUI()
        self.draw_graph()

    # ------------- the interface (the part AI is allowed to write) -------------
    def initUI(self):
        self.setWindowTitle("Ice Cream Revenue")
        self.setGeometry(100, 100, 800, 600)

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.title_label = QLabel("Ice Cream Revenue vs Temperature")
        self.title_label.setObjectName("title")

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_clicked)

        # a matplotlib graph inside the window; the toolbar gives zoom and "save as image"
        self.figure = Figure()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("about")
        self.about_button.clicked.connect(self.about_clicked)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.load_button)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        main_layout.addWidget(self.about_button)
        self.central.setLayout(main_layout)

    def draw_graph(self):
        """Temporary graph (generated method). You will replace its content yourself."""
        self.ax.clear()
        self.ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
        self.ax.set_title("Temporary graph")
        self.canvas.draw()

    def about_clicked(self):
        self.about_window.show()

    # ------------- YOUR PART: write it yourself, as we learned in class -------------
    def load_clicked(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choose the data file", "", "CSV files (*.csv)")
        if file_name == '':
            return
        # TODO: open the file, read it into self.temperatures and self.revenues,
        #       then call self.draw_graph()


if __name__ == "__main__":
    app = QApplication()

    with open("style.qss") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    app.exec()
