from os import path
from functools import partial

from Packages.DesignUI import MainWindows, TreeView, ListView, Slider, HBoxLayout, Icon, ItemSelectionModel,\
    StandardPaths
from Packages.api.explorer import ROOT_FOLDER, Explorer


def hide_column(view: TreeView, nb_column: int):
    view.setHeaderHidden(True)
    for i in range(1, nb_column):
        view.setColumnHidden(i, True)


class Windows(MainWindows):
    def __init__(self):
        super().__init__("Cute Explorer", 800, 500)

        self.tree_view = TreeView()
        self.list_view = ListView()
        self.slider = Slider()
        self.explorer = Explorer()

        self.slider.setRange(40, 256)
        self.slider.setValue(60)

        h_layout = HBoxLayout(self.central_widget)
        h_layout.addWidget(self.tree_view)
        h_layout.addWidget(self.list_view)
        h_layout.addWidget(self.slider)
        h_layout.setStretch(0, 1)  # (a, b) a: index of first widget, b: value of proportion of space
        h_layout.setStretch(1, 3)  # 2+1 = 100 % of space

        self.tree_view.setModel(self.explorer)
        self.tree_view.setRootIndex(self.explorer.index(ROOT_FOLDER))
        hide_column(self.tree_view, 4)

        self.list_view.setModel(self.explorer)
        self.list_view.setRootIndex(self.explorer.index(ROOT_FOLDER))

        # Toolbar
        project_path = path.dirname(path.abspath(__file__))
        locations = ["home", "desktop", "documents", "movies", "music", "pictures"]
        for location in locations:
            icon = Icon(path.join(project_path, 'resources', 'icons', f"{location}.svg"))
            # add and connect actions to slots
            action = self.toolbar.addAction(icon, location.capitalize())
            action.triggered.connect(partial(self.open_folder, location))   # partial use to pass an argument to slot

        # Connections
        self.tree_view.clicked.connect(self.tree_view_clicked)
        self.list_view.clicked.connect(self.list_view_clicked)
        self.list_view.doubleClicked.connect(self.list_view_double_clicked)
        self.slider.valueChanged.connect(self.change_icon_size)

    # slot
    def tree_view_clicked(self, index):
        if self.explorer.isDir(index):  # if selected is a dir, we send the index to the list view
            self.list_view.setRootIndex(index)
        else:   # if it's a file, we show the parent to the list view
            self.list_view.setRootIndex(index.parent())

    def list_view_clicked(self, index):
        selection_model = self.tree_view.selectionModel()   # model selected
        selection_model.setCurrentIndex(index, ItemSelectionModel.ClearAndSelect)   # choose index to select

    def list_view_double_clicked(self, index):
        self.list_view.setRootIndex(index)  # open folder

    def open_folder(self, location):
        # QtCore have a lot of standard path as attribute that we'll use many here
        paths_to_open = eval(f"StandardPaths().standardLocations(StandardPaths.{location.capitalize()}Location)")
        self.tree_view.setRootIndex(self.explorer.index(paths_to_open[0]))
        self.list_view.setRootIndex(self.explorer.index(paths_to_open[0]))

    def change_icon_size(self, value):
        self.list_view.set_icon_size(value, value)

    # methods
