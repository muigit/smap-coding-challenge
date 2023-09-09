# Docker 環境

Django 4 + Docker

## コンテナ構成

1. Django

- Python 3.11.\*
- Django 4.2.\*
- COPY は、変更がされにくいファイルと変更されやすいファイルで Layer を分けて実行
- RUN は && で Layer を 1 つにしてイメージサイズを最小限に抑える
- ルートレスユーザー

## 環境を起動する手順

1. Docker を起動する

```sh
$ docker compose up --build
```
