# いやしのおうち 公式サイト

大阪府大東市の女性専用グループホーム「いやしのおうち」の公式ウェブサイトです。

- 作業フォルダ: `etc/iyashinouchi-site/`
- GitHub: https://github.com/resumecor-lang/iyashinouchi-site

## ファイル構成

```
iyashinouchi-site/
├── index.html        … TOPページ
├── about.html        … ホームのご案内
├── day.html          … 1日の流れ
├── use.html          … ご入居の流れ・費用
├── recruit.html      … 採用情報
├── contact.html      … お問い合わせ
├── css/
│   └── style.css     … 共通スタイル
├── images/           … 写真ファイル置き場
└── README.md         … このファイル
```

## 反映済み（チラシ確定情報）

- 事業所: いやしのおうち／共同生活援助（女性専用）／定員4名
- 所在地: 〒574-0011 大阪府大東市北条5-8-31
- 最寄り: JR学研都市線「四条畷駅」徒歩約13分（「野崎駅」徒歩約23分）
- TEL: 080-6619-2027（受付 9:00〜18:00／土日祝も可）
- メール: iyashiya.a1@gmail.com
- 開設予定: 2026年10月
- 運営: 株式会社 癒し家（代表：加賀谷 徹／臨床心理士）
- 実費目安: 家賃 39,000円〜、昼食任意、敷金0円、家賃補助 −10,000円、合計目安 70,130円〜（昼食なし）

## まだ手元の情報が必要な箇所

- `contact.html` の `YOUR_FORM_ID` … Formspree で発行したURL
- LINE友だち追加URL
- 施設写真（`about.html` はプレースホルダのまま）
- 採用の給与額（いまは「お問い合わせください」）

## フォームの設定方法（Formspree）

1. https://formspree.io にアクセスして登録
2. 新しいフォームを作成し、受信用メール（iyashiya.a1@gmail.com）を設定
3. 発行されたURL（例：`https://formspree.io/f/abc123xyz`）をコピー
4. `contact.html` の `YOUR_FORM_ID` 部分を置き換える

## GitHub Pagesでの公開方法

1. https://github.com/resumecor-lang/iyashinouchi-site/settings/pages を開く
2. Source で **Deploy from a branch** を選ぶ
3. Branch を `main`、フォルダを `/ (root)` にして Save
4. 数分後に `https://resumecor-lang.github.io/iyashinouchi-site/` で公開

## ローカルでの確認方法

`index.html` をダブルクリックするだけでブラウザで開けます。
