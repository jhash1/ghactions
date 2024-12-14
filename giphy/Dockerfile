FROM alpine:3.10


RUN apk update && \
    apk add --no-cache curl jq

COPY entrypoint.sh /giphy/entrypoint.sh

RUN chmod +x /giphy/entrypoint.sh

ENTRYPOINT ["/giphy/entrypoint.sh"]