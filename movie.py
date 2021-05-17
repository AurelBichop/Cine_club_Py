import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


def get_movies():
    with open(DATA_FILE, "r", encoding='utf-8') as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]

    return movies


class Movie:
    def __init__(self, titre):
        self.titre = titre.title()

    def __str__(self):
        return self.titre

    def _get_movies(self):
        with open(DATA_FILE, "r", encoding='utf-8') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w", encoding='utf-8') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.titre not in movies:
            movies.append(self.titre)
            self._write_movies(movies)
            return True
        else:
            logging.warning(
                f"Attention le film {self.titre} existe déja dan la liste")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()

        if self.titre in movies:
            movies.remove(self.titre)
            self._write_movies(movies)
            return True
        else:
            logging.warning(
                f"Attention le film {self.titre} n'existe pas dans la liste")
            return False


if __name__ == "__main__":
    all_movies = get_movies()
    print(all_movies)
