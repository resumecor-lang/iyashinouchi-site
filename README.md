# いやしのおうち 公式サイト

障がい者グループホーム「いやしのおうち」の公式ウェブサイトです。

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

## 編集が必要な箇所

### 全ページ共通
- `XXX-XXXX-XXXX` … 電話番号に置き換え
- `〒XXX-XXXX 大阪府○○市○○町X-X-X` … 実際の住所
- `0000000000` … 電話番号のtel:リンク（ハイフンなし）
- LINEボタンの `href="#"` … LINE友だち追加URL

### TOPページ (index.html)
- メインビジュアル画像
- 特徴アイコン

### ホームのご案内 (about.html)
- 施設写真6枚
- 基本情報テーブル（所在地・最寄り駅・定員等）

### ご入居・費用 (use.html)
- 実費負担金額（家賃・食費・光熱水費）

### 採用情報 (recruit.html)
- 給与額

### お問い合わせ (contact.html)
- `https://formspree.io/f/YOUR_FORM_ID` … Formspreeで取得したフォームURL
- Googleマップ埋め込みコード

## フォームの設定方法（Formspree）

無料のフォームサービス「Formspree」を使ってお問い合わせを受け取れます。

1. https://formspree.io にアクセスして登録
2. 新しいフォームを作成して、受信用メールアドレスを設定
3. 発行されたURL（例：`https://formspree.io/f/abc123xyz`）をコピー
4. `contact.html` の `YOUR_FORM_ID` 部分を置き換える

## GitHub Pagesでの公開方法

1. GitHubでリポジトリを作成
2. このフォルダの全ファイルをアップロード
3. Settings → Pages → Source を main ブランチに設定
4. 数分後に `https://[ユーザー名].github.io/[リポジトリ名]/` で公開

## ローカルでの確認方法

`index.html` をダブルクリックするだけでブラウザで開けます。
