FROM alpine:3.23

# hadolint ignore=DL3018
RUN apk upgrade --no-cache \
    && apk add --no-cache python3

WORKDIR /app
COPY --chown=10001:10001 src/app.py /app/app.py

USER 10001
EXPOSE 8080
CMD ["python3", "/app/app.py"]
