FROM python:3.9-alpine AS builder

WORKDIR /app

RUN apk add --no-cache build-base

COPY song_wordcount.py /app/
COPY data/ /home/data/

RUN mkdir -p /home/data/output

FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /app/song_wordcount.py /app/
COPY --from=builder /home/data /home/data/

CMD ["python", "song_wordcount.py"]