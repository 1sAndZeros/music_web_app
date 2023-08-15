class Album:
    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"
