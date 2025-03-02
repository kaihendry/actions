# https://aur.archlinux.org/packages/goredo/
# http://www.goredo.cypherpunks.su/

FROM golang
RUN curl -O http://www.goredo.cypherpunks.su/download/goredo-2.6.4.tar.zst
RUN apt-get update && \
    apt-get install -y --no-install-recommends zstd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN tar --use-compress-program unzstd -xvf goredo-2.6.4.tar.zst --strip-components=1 -C /tmp
WORKDIR /tmp/src
RUN go build -mod=vendor
RUN ./goredo -symlinks

FROM debian
COPY --from=0 /tmp/src/goredo /tmp/src/redo* /bin/
ENTRYPOINT ["/bin/redo"]
