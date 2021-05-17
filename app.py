from PySide2 import QtWidgets, QtCore
from PySide2.QtGui import Qt
from movie import Movie, get_movies


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.line_addFilm = QtWidgets.QLineEdit()
        self.btn_addFilm = QtWidgets.QPushButton("Ajouter un film")
        self.list_films = QtWidgets.QListWidget()
        self.list_films.setSelectionMode(
            QtWidgets.QListWidget.ExtendedSelection)
        self.btn_rmFilm = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.line_addFilm)
        self.layout.addWidget(self.btn_addFilm)
        self.layout.addWidget(self.list_films)
        self.layout.addWidget(self.btn_rmFilm)

    def setup_connections(self):
        self.btn_addFilm.clicked.connect(self.add_movie)
        self.line_addFilm.returnPressed.connect(self.add_movie)
        self.btn_rmFilm.clicked.connect(self.remove_movie)

    def populate_movies(self):
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.titre)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_films.addItem(lw_item)

    def add_movie(self):
        movie_title = self.line_addFilm.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)
        resultat = movie.add_to_movies()

        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.titre)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_films.addItem(lw_item)

        self.line_addFilm.setText("")

    def remove_movie(self):
        for seleted_item in self.list_films.selectedItems():
            movie = seleted_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.list_films.takeItem(self.list_films.row(seleted_item))


app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()
