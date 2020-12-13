Tweet Sentiment
---

<!--- ![Screenshot](docs/screenshot.png) --->

## Tech

- python
  - flask
  - sqlalchemy
  - psycopg2
  - (pandas)
- javascript + css
  - vuejs
  - axios
  - bootstrap
- postgresql

### Setup

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
pip3 install --upgrade pip
```

```bash
pip3 install flask
```

```bash
pip3 install -r requirements.txt
```

### Development

```bash
FLASK_APP=run.py FLASK_ENV=development SQLALCHEMY_DATABASE_URI=postgresql://u:p@host:5432/qondo_neo flask run
```

## Database

2 models/tables

```
tweets
  - attribute - pk - id
  - attribute - text - tweet-text
  - attribute - integer - external-id
  - relationship - has_many - answers
```

```
answers
  - attribute - pk - id
  - attribute - sentiment - enum (positive/negative/neutral)
  - attribute - integer - tweet_id
  - relationship - belongs_to - tweet
```

## Endpoints

### GET `/`

Returns frontend html

### GET `/api`

Healthcheck endpoint for api

### GET `/api/tweets`

Returns single tweet as json

### POST `/api/answers/<tweetid>`

Create an answer in the database for the given tweet id.
Returns single tweet as json (same as `/api/sentiments/` to avoid the additional request to get the next tweet)

### POST `/api/tweets`

Creates tweets in the db for the provided csv

## Deployment

Single AWS EC2 Instance in `public subnet` (so as to avoid nat requirements and to support demo)
Single AWS RDS Instance in `public subnet` (so as to avoid nat requirements and to support demo)

RDS + EC2 instance secured by security group limited to my rough ip range

No load balancer (for simplicity)
No ECS / docker deployment (for simplicity)

bootstrap script to setup machine
