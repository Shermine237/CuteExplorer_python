#   Design Widget
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QListWidget, QTextEdit, QPushButton, QToolBar,\
    QTreeView, QListView, QSlider, QHBoxLayout
from PySide6.QtCore import QSize, QItemSelectionModel, QStandardPaths
from PySide6.QtGui import QIcon


class Application(QApplication):
    def __init__(self):
        super().__init__()


class HBoxLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)


class Icon(QIcon):
    def __init__(self, path):
        super().__init__(path)


class ItemSelectionModel(QItemSelectionModel):
    def __init__(self):
        super().__init__()


class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)


class ListWidget(QListWidget):
    def __init__(self):
        super().__init__()


class ListView(QListView):
    def __init__(self):
        super().__init__()
        self.setViewMode(QListView.ViewMode.IconMode)
        self.setUniformItemSizes(True)
        self.setIconSize(QSize(60, 60))

    # Methods
    def set_icon_size(self, b, h):
        self.setIconSize(QSize(b, h))


class MainWidget(QWidget):
    def __init__(self, title, b=600, h=500):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(b, h)


class MainWindows(QMainWindow):
    def __init__(self, title, b=600, h=500):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(b, h)

        self.central_widget = QWidget()
        self.toolbar = QToolBar()

        self.addToolBar(self.toolbar)
        self.setCentralWidget(self.central_widget)


class PushButton(QPushButton):
    def __init__(self, title):
        super().__init__(title)
        self.setDisabled(True)


class Slider(QSlider):
    def __init__(self):
        super().__init__()


class StandardPaths(QStandardPaths):
    def __init__(self):
        super().__init__()


class TextEdit(QTextEdit):
    def __init__(self):
        super().__init__()


class TreeView(QTreeView):
    def __init__(self):
        super().__init__()
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
