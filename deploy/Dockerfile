# Build the site with Hugo, serve it from nginx.
#
#   docker compose up --build
#     arcanebyte -> http://localhost:8090
#
# The standard (not extended) Hugo release is enough: the site uses plain CSS,
# and image processing is in the standard build. The binary is pure Go, so it
# runs on alpine without glibc.

FROM alpine:3.20 AS build
ARG HUGO_VERSION=0.165.0
ARG TARGETARCH
RUN apk add --no-cache curl tar \
 && case "$TARGETARCH" in \
      amd64) HUGO_ARCH=linux-amd64 ;; \
      arm64) HUGO_ARCH=linux-arm64 ;; \
      *) echo "unsupported arch: $TARGETARCH" >&2; exit 1 ;; \
    esac \
 && curl -fsSL -o /tmp/hugo.tar.gz \
      "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_${HUGO_ARCH}.tar.gz" \
 && tar -xzf /tmp/hugo.tar.gz -C /usr/local/bin hugo \
 && hugo version

WORKDIR /src
COPY themes/ ./themes/
COPY sites/ ./sites/
RUN hugo --source sites/arcanebyte --minify --destination /out/arcanebyte

FROM nginx:1.27-alpine
COPY --from=build /out/arcanebyte /usr/share/nginx/arcanebyte
COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
