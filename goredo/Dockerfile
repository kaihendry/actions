# https://aur.archlinux.org/packages/goredo/
# http://www.goredo.cypherpunks.ru/Install.html

FROM golang
RUN curl -O http://www.goredo.cypherpunks.ru/download/goredo-0.11.0.tar.zst
RUN apt-get update && \
    apt-get install -y --no-install-recommends zstd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN tar --use-compress-program unzstd -xvf goredo-0.11.0.tar.zst --strip-components=1 -C /go
ENV GOPATH /go
WORKDIR /go
RUN go build go.cypherpunks.ru/goredo
RUN ./goredo -symlinks

FROM scratch
COPY --from=0 /go/goredo /go/redo* /bin/
