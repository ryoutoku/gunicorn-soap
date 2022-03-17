# gunicorn-soap

python による SOAP サーバ実装サンプル

## 構成

```bash
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── docker-compose.yaml
└── src
    ├── app.py            # アプリケーション定義
    ├── client_sample.py  # クライアント実行サンプル
    ├── models.py         # カスタムパラメータサンプル実装
    ├── service.py        # サービス実装
    └── wsgi.py           # WSGI エントリーポイント
```

## 実行

- docker-compose ver.3.8 実行を想定
- ポートは 80 を使用

```bash
# コンテナ内でlocalhost:80でサーバが起動
docker-compose up

# コンテナ内でクライアント実行
docker-compose exec web python src/client_sample.py

# クライアント実行結果
['Hello, dummy_name', 'Hello, dummy_name', 'Hello, dummy_name']
=====================
['Hello, dummy_name', 'Hello, dummy_name', 'Hello, dummy_name']
=====================
{
    'name': 'dummy_name',
    'times': 3
}
<class 'zeep.objects.RequestParameter'>
```

## 使用パッケージ

### サーバ側

- spyne
  - SOAP サーバのパッケージ
  - http://spyne.io/#inprot=HttpRpc&outprot=JsonDocument&s=rpc&tpt=WsgiApplication&validator=true
- lxml
  - input 時に xml に対して validate する際に必要(らしい)パッケージ
- gunicorn
  - WSGI サーバのパッケージ

### クライアント側

- zeep
  - SOAP クライアントパッケージ
  - https://docs.python-zeep.org/en/master/
