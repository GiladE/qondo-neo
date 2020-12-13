Tweet Sentiment
---

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

## Endpoints

### GET `/`

Returns frontend html

### GET `/api`

Healthcheck endpoint for api

### GET `/api/sentiments`

Returns single tweet as json

### POST `/api/sentiments`

Returns single tweet as json

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
  - attribute - sentiment - enum (positive/negative/skip)
  - attribute - integer - tweet_id
  - relationship - belongs_to - tweet
```

## Deployment

Single AWS EC2 Instance in `public subnet` (so as to avoid nat requirements and to support demo)
Single AWS RDS Instance in `public subnet` (so as to avoid nat requirements and to support demo)

RDS + EC2 instance secured by security group limited to my rough ip range

No load balancer (for simplicity)
No ECS / docker deployment (for simplicity)

bootstrap script to setup machine
