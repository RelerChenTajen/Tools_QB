# exam-to-qb 網頁版安裝總覽

在瀏覽器裡就能用 exam-to-qb 把考題檔轉成題庫 CSV（Gemini 的最後一步要在自己的電腦執行）。請依您使用的 AI 選一份說明：

| AI 網頁版 | 誰可以安裝技能 | 安裝檔 | 操作說明 |
|-----------|---------------|--------|----------|
| **Claude** | 免費與所有付費方案 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [claude-web.md](claude-web.md) |
| **ChatGPT** | 官方列出 Business、Enterprise、Edu、Healthcare；其他方案改用附件方式 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [chatgpt-web.md](chatgpt-web.md) |
| **Gemini**（只產生 TSV，再用電腦上的 Python 轉 CSV） | 滿 18 歲的個人 Google 帳號（免費可用）；學校帳號改用附件方式 | [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip) | [gemini-web.md](gemini-web.md) |

**不知道選哪個？** 建議先用 Claude：免費帳號就能安裝技能，而且技能本來就以開啟程式碼執行為前提。

> 要上傳安裝的 ZIP **不要解壓縮**。也不要用 GitHub 的「Download ZIP」，那是整個專案，不是技能安裝檔。

## 三種都適用

### 先用範例練習

第一次使用請先拿範例走一遍，確認安裝成功再轉自己的考題：

1. 下載 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx)，用它當附件。
2. 依各說明的步驟轉換，類別填「資訊安全」。
3. 與[範例對照表](#範例對照表)或成果檔 [`sample.csv`](../sample.csv)、[`sample_big5.csv`](../sample_big5.csv) 比對。

#### 範例對照表

| 列 | 題型 | 題目 | 答案欄 | 難易度 |
|:--:|------|------|--------|:--:|
| 1 | 1 是非 | 使用同一組密碼登入所有網站… | `2`（否） | 1 |
| 2 | 1 是非 | 開啟多因素驗證後… | `1`（是） | 1 |
| 3 | 2 單選 | 收到自稱銀行的電子郵件… | `2` | 1 |
| 4 | 2 單選 | 備份的「3-2-1 原則」… | `3` | 2 |
| 5 | 3 複選 | 資訊安全的三大要素？ | `1,2,3` | 2 |
| 6 | 3 複選 | 降低勒索軟體造成的損害？ | `1,2,4` | 2 |
| 7 | 4 填充 | HTTPS…連接埠號碼是 `[*443*]` | 空白（選項1、2 為 `1`、`1`） | 2 |
| 8 | 4 填充 | CIA…`[*Confidentiality*]`…`[*Integrity*]` | 空白（選項1、2 為 `1`、`2`） | 3 |
| 9 | 5 問答 | 如何辨識釣魚郵件？ | 三點參考答案，分三行 | 3 |

題型、答案、選項與難易度應完全一致；標點或空白略有不同可以接受。

### 提示詞範本

適用 Claude 與 ChatGPT；Gemini 請用[它的說明](gemini-web.md#第-3-步請-gemini-產生-tsv)裡的提示詞。

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

## 查證與測試狀態（2026-11-25）

| 項目 | 狀態 |
|------|------|
| 方案資格、選單路徑 | 已於 2026-11-24 對照三家官方說明頁（連結在各說明文末） |
| `exam-to-qb.zip` 內容 | 已測試：解開後執行 `build.py`，輸出與正本逐位元相同（52 題，UTF-8 與 Big5） |
| Gemini 安裝含腳本的舊版 | 已實測：**不能執行**，Gemini 回覆不支援含程式碼的自訂技能 |
| Gemini 純文字新版 | 技能內的範例已測試可由 `build.py` 轉出；在 Gemini 的完整流程**尚無實測紀錄** |
| Claude、ChatGPT 實際上傳安裝 | **尚未實測** |
| 題庫系統匯入網頁版產出的 CSV | **尚未實測** |

## 維護者：更新安裝檔

安裝檔一律由正本 [`skill/exam-to-qb/`](../skill/exam-to-qb/) 產生，不要手動改 ZIP：

```bash
python web/pack.py           # 重新打包
python web/pack.py --check   # 檢查 ZIP 是否落後正本
```

改了正本後要重新打包、commit、push，並通知使用者重新上傳，網頁版不會自動更新。

- `exam-to-qb.zip`：完整技能（含 Python），外層為 `exam-to-qb/`，供 Claude、ChatGPT 與 Gemini 使用者的電腦端使用。
- `exam-to-qb-gemini.zip`：只有 `SKILL.md`，由 [`gemini/SKILL.template.md`](gemini/SKILL.template.md) 產生；「題庫格式」與「解析規則」自動取自正本，其餘文字改範本。
- `build.ps1` 與 `examples/` 在網頁版用不到，不打包。
- 打包時會檢查 `description` 不超過 200 字（Claude 網頁版的上限，三家已知上限中最嚴）。

[`archive/`](archive/) 保留本說明的原始稿，僅供參考，請勿用來安裝。
