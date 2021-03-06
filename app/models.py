from app import db
import enum

class SentimentType(enum.Enum):
    positive = 1
    negative = 2
    neutral = 3

class Tweet(db.Model):

  __tablename__ = "tweets"

  id = db.Column(db.Integer, primary_key=True)
  externalid = db.Column(db.Integer, nullable=True)
  text = db.Column(db.String, nullable=False)
  answers = db.relationship('Answer', backref='tweet', lazy=True)

  def __init__(self, text, externalid=None):
    self.text = text
    self.externalid = externalid

  def __repr__(self):
    return '<id {} text {}... externalid {}>'.format(self.id, self.text[0:10], self.externalid)

class Answer(db.Model):

  __tablename__ = "answers"

  id = db.Column(db.Integer, primary_key=True)
  tweet_id = db.Column(db.Integer, db.ForeignKey('tweets.id'), nullable=False)
  sentiment = db.Column(db.Enum(SentimentType), nullable=True)

  def __init__(self, tweet, sentiment):
    self.tweet = tweet
    self.sentiment = sentiment

  def __repr__(self):
    return '<id {} tweet {} sentiment {}>'.format(self.id, self.tweet, self.sentiment)
