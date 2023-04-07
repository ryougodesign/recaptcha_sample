# recaptcha_sample
DjangoのフォームにreCAPTCHA V3を簡単に設定する方法のサンプルコード

# Cloneして動作確認する場合

Cloneして動作確認する場合は、下記の手順でSECRET_KEYとリキャプチャーキーを設定してください。

1. Dockerでコンテナを作成起動

```python
python generate_secret_key.py
> SECRET_KEY = 'SECRET_KEYが生成されるのでコピー'
```
2. pythonでgenerate_secret_key.pyを実行して、SECRET_KEYを生成します
SECRET_KEYはコピーしておいてください

recaptcha_project/settings.py
```python
SECRET_KEY = 'ここに生成したSECRET_KEYを張り付けてください'

RECAPTCHA_PRIVATE_KEY = "シークレットキー値を入力"
RECAPTCHA_PUBLIC_KEY = "サイトキー値を入力"
```
3. 生成したSECRET_KEYをsettings.pyのSECRET_KEYに張り付けてください
4. リキャプチャーキーも同様にご自身で設定したキー値を張り付けてください
5. 設定完了