from PySide6.QtWidgets import QFileSystemModel
from PySide6.QtCore import QDir

ROOT_FOLDER = QDir.rootPath()


class Explorer(QFileSystemModel):
    def __init__(self):
        super().__init__()

        self.setRootPath(ROOT_FOLDER)
