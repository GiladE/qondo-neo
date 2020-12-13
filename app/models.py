from app import db
import enum

class SentimentType(enum.Enum):
    positive = 1
    negative = 2
    skip = 3
