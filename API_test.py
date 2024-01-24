from ytmusicapi import YTMusic

ytmusic = YTMusic()

YTMusic.search(query: str, filter: str | None = None, scope: str | None = None, limit: int = 20, ignore_spelling: bool = False)→ List[Dict]