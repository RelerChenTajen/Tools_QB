# exam-to-qb 網頁版安裝總覽

不必安裝任何程式，在瀏覽器裡就能用 exam-to-qb 把考題檔轉成題庫 CSV。請依您使用的 AI 選一份說明：

| AI 網頁版 | 誰可以安裝技能 | 安裝檔 | 操作說明 |
|-----------|---------------|--------|----------|
| **Claude** | 免費與所有付費方案 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [claude-web.md](claude-web.md) |
| **ChatGPT** | 官方列出 Business、Enterprise、Edu、Healthcare；其他方案改用附件方式 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [chatgpt-web.md](chatgpt-web.md) |
| **Gemini** | 滿 18 歲的個人 Google 帳號（免費可用）；學校帳號尚未開放 | [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip) | [gemini-web.md](gemini-web.md) |

**不知道選哪個？** 建議先用 Claude：免費帳號就能安裝技能，而且技能本來就以開啟程式碼執行為前提。

> ZIP 下載後**不要解壓縮**，直接上傳。也不要用 GitHub 的「Download ZIP」，那是整個專案，不是技能安裝檔。

## 三種都適用

### 提示詞範本

```
請使用 exam-to-qb 技能，把附件轉成題庫 CSV。
類別填「資訊安全」，同時產生 UTF-8 無 BOM 與 Big5 兩個版本。
請實際執行 build.py 產生檔案，不要用聊天文字代替。
保留原始題幹、選項與答案，缺答案或有矛盾的題目請列出來，不要自行補上。
```

### 匯入前檢查

1. 題數與原稿相同。
2. 逐題核對答案。轉換程式會擋下答案缺漏、答案編號超過選項數等格式錯誤，但**格式正確而答案錯誤的題目檢查不出來**。
3. 填充題的答案寫在題目裡，格式為 `[*答案*]`。
4. Big5 檔沒有出現原稿沒有的 `?`。
5. 先用非正式考題在題庫系統試匯入一次。

### 資料安全

- 未經授權的正式考題、學生個資、系統密碼不要上傳。
- 不要把考題提交到公開的 GitHub。
- 校內資料請先確認學校對各 AI 服務的使用規範。

## 查證與測試狀態（2026-11-24）

| 項目 | 狀態 |
|------|------|
| 方案資格、選單路徑 | 已對照三家官方說明頁（連結在各說明文末） |
| 安裝檔內容 | 已測試：兩個 ZIP 解開後執行 `build.py`，輸出與正本逐位元相同（52 題，UTF-8 與 Big5） |
| 三家網頁實際上傳安裝 | **尚未實測** |
| 題庫系統匯入網頁版產出的 CSV | **尚未實測** |

## 維護者：更新安裝檔

安裝檔一律由正本 [`skill/exam-to-qb/`](../skill/exam-to-qb/) 產生，不要手動改 ZIP：

```bash
python web/pack.py           # 重新打包
python web/pack.py --check   # 檢查 ZIP 是否落後正本
```

改了正本後要重新打包、commit、push，並通知使用者重新上傳，網頁版不會自動更新。

- 兩個 ZIP 內容相同，差別在 Gemini 要求 `SKILL.md` 放在 ZIP 的主要資料夾，Claude 則要求外層有 `exam-to-qb/`。
- `build.ps1` 與 `examples/` 在網頁版用不到，不打包。
- 打包時會檢查 `description` 不超過 200 字（Claude 網頁版的上限，三家已知上限中最嚴）。

[`archive/`](archive/) 保留本說明的原始稿，僅供參考，請勿用來安裝。
