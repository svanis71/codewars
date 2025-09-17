# Mongodb ObjectID
from datetime import datetime, timezone


class Mongo:
    @staticmethod
    def is_valid(s) -> bool:
        """returns True if s is a valid MongoID; otherwise False"""
        return isinstance(s, str) and all(c in '0123456789abcdef' for c in s) and len(s) == 24

    @staticmethod
    def get_timestamp(s) -> datetime | bool:
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        if Mongo.is_valid(s):
            return datetime.fromtimestamp(int(s[0:8], 16), tz=timezone.utc)
        return False
