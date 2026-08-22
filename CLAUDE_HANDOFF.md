# いやしのおうち HP｜引き継ぎ（HANDOFF）

**最終更新**：2026-08-22 13:22  
**ユーザー**：Resume（加賀谷徹）  
**目的**：女性専用グループホーム「いやしのおうち」公式HPの更新と公開

このファイルを読んだら、まず進捗を確認し、**次の一手だけ**提案してから着手すること。一度に全部やらない。

新しいチャットの最初にユーザーが貼る文（任意）:

```text
いやしのおうちのHPの続きをしたいです。
etc/iyashinouchi-site/CLAUDE_HANDOFF.md を読んで、次の一手だけ進めてください。
```

---

## いまの位置

**公式HPは公開済み。** チラシ確定情報・定員4名・見出しの太さまで GitHub に送済み。

| 項目 | 状態 |
|---|---|
| 公式リポジトリ | https://github.com/resumecor-lang/iyashinouchi-site |
| 公開URL | https://resumecor-lang.github.io/iyashinouchi-site/ |
| 作業フォルダ（正本） | `etc/iyashinouchi-site/` |
| Jekyll試作 | `etc/iyashi-no-ouchi/`（GitHubに上げない） |
| 最終push | `d502e1b`（お問い合わせフォームを公開） |

ユーザーが「続きをやって」と言ったら、下の「次にやること」の**先頭1件だけ**進める。

---

## 2つのフォルダ（混ぜない）

| フォルダ | 役割 |
|---|---|
| **`etc/iyashinouchi-site/`** | **公式。** 静的HTML。GitHub Pages で公開中。編集・commit・push はここだけ |
| `etc/iyashi-no-ouchi/` | Jekyll分割の試作。Ruby/Jekyll は入っている。公開の正本ではない |

---

## 確定事項（崩さない）

- 事業所名：いやしのおうち
- 種別：共同生活援助（**女性専用**）
- **定員：4名**（7名に戻さない）
- 所在地：〒574-0011 大阪府大東市北条5-8-31
- 最寄り：JR学研都市線「四条畷駅」徒歩約13分（「野崎駅」徒歩約23分）
- TEL：080-6619-2027（受付 9:00〜18:00／土日祝も可）
- メール：iyashiya.a1@gmail.com
- 開設予定：2026年10月
- 運営：株式会社 癒し家／代表：加賀谷 徹（臨床心理士）
- 本店：大阪府大阪市天王寺区上汐3丁目6-14-505C
- 料金目安：家賃 39,000円〜、朝食 6,900円、昼食 13,800円（任意）、夕食 13,800円、光熱費 15,000円、日用品 5,000円〜、敷金 0円、家賃補助 −10,000円、補助後合計 **70,130円〜（昼食なし）**
- 1日の流れ：7:00 朝食 → 9:00 日中活動 → 16:00 帰宅 → 18:00 夕食 → 21:00 就寝・見守り

---

## 次にやること（優先順・1回1件）

1. **Google検索登録** … Search Console でサイト所有権確認＋sitemap送信＋インデックス登録リクエスト（ユーザー作業。手順は README）
2. **施設写真** … `about.html` はプレースホルダのまま。写真をもらったら `images/` へ
3. **LINE URL** … 友だち追加URLが来たら差し替え（いまはメールにしている）
4. **採用の給与** … 金額が来たら `recruit.html` の「お問い合わせください」を置き換え
5. 不要ファイル `index.html.html` の削除は、確認してから
6. **お問い合わせフォーム** … 済み（`https://formspree.io/f/xzepkwvy`）。公開済み `d502e1b`
7. **検索向けファイル** … `robots.txt` / `sitemap.xml` / TOPのメタ・構造化データ 済み（このセッション）

GitHub へ送るときはユーザーが「GitHubに上げて」と言ってから。対象は `etc/iyashinouchi-site/` のみ。検索ヒット目的でSEOを直した直後は、公開のため push してよい。

---

## 手段（この案件）

- 着手: **Cursor**（文言・見た目）
- 追加: **GitHub CLI（`gh`）** … ログイン済み（`resumecor-lang`）
- Pages が 404 でも API が `built` のときは、再ビルドする:

```powershell
gh api -X POST repos/resumecor-lang/iyashinouchi-site/pages/builds
```

- このPCの git に user.name が無い。`git config` は変更しない。commit するときは環境変数で1回だけ渡す:

```powershell
$env:GIT_AUTHOR_NAME = 'resumecor-lang'
$env:GIT_AUTHOR_EMAIL = '256546003+resumecor-lang@users.noreply.github.com'
$env:GIT_COMMITTER_NAME = $env:GIT_AUTHOR_NAME
$env:GIT_COMMITTER_EMAIL = $env:GIT_AUTHOR_EMAIL
```

- Cursor Origin（origin.cursor.com）は使わない（Windows非対応・別ホスト）

---

## 必読

1. この HANDOFF
2. `etc/iyashinouchi-site/README.md`
3. `routing/MATRIX.md` / `routing/CATALOG.md`
4. 振り返り: `routing/history/2026-08-19-iyashi-github-pages.md`

作業範囲は `C:\Users\saxop\OneDrive\Desktop\cursor` 配下のみ。
