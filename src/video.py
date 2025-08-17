class Video:
    """A class representing a single video."""

    def __init__(self, title: str, video_id: str, tags):
        self._title = title
        self._video_id = video_id
        # store tags as an immutable tuple
        self._tags = tuple(tags) if tags else ()

    @property
    def title(self) -> str:
        return self._title

    @property
    def video_id(self) -> str:
        return self._video_id

    @property
    def tags(self):
        return self._tags

    def __str__(self) -> str:
        tags_formatted = " ".join(self._tags)
        return f"{self._title} ({self._video_id}) [{tags_formatted}]"
