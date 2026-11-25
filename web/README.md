# exam-to-qb 網頁版安裝總覽

在瀏覽器裡就能用 exam-to-qb 把考題檔轉成題庫 CSV。請依您使用的 AI 選一份說明：

| AI 網頁版 | 誰可以用 | ZIP | 操作說明 |
|-----------|---------------|--------|----------|
| **Claude**（安裝技能） | 付費帳號已實測可用；官方說明免費帳號也可用，尚未實測 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [claude-web.md](claude-web.md) |
| **ChatGPT**（私人外掛，或每次附上） | Plus 已實測，兩種方式都可匯入；免費與其他方案尚未實測 | [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) | [chatgpt-web.md](chatgpt-web.md) |
| **Gemini**（安裝技能） | 滿 18 歲的個人 Google 帳號（免費可用）；學校帳號尚未開放 | [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip) | [gemini-web.md](gemini-web.md) |

**不知道選哪個？** 有個人 Google 帳號可用 Gemini（已實測可匯入）；想要程式檢查格式，可用 Claude（付費帳號）或 ChatGPT 附件方式（Plus），都已實測可匯入。

### 介面語言與選項名稱

| AI 網頁版 | 介面 | 說明裡的寫法 |
|-----------|------|--------------|
| Gemini | 繁體中文 | 「中文」（英文），中文取自 Google 繁體中文說明 |
| ChatGPT | 中文 | 「中文」（英文），中文取自 OpenAI 繁體中文說明（機器翻譯） |
| Claude | 官方未列中文介面 | **英文**（中文意思） |

畫面與說明不同時，請以選項的位置和英文名稱為準，並回報給維護者更新。

> 要上傳的 ZIP **不要解壓縮**。也不要用 GitHub 的「Download ZIP」，那是整個專案，不是技能安裝檔。

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

適用 Claude；ChatGPT 與 Gemini 請用[ChatGPT 說明](chatgpt-web.md)、[Gemini 說明](gemini-web.md#使用)裡的提示詞。

```
請使用 exam-to-qb 技能，把附件轉成題庫 CSV。
類別填「資訊安全」，同時產生 UTF-8 無 BOM 與 Big5 兩個版本。
請實際執行 build.py 產生檔案，不要用聊天文字代替。
保留原始題幹、選項與答案，缺答案或有矛盾的題目請列出來，不要自行補上。
```

### 匯入前檢查

1. 題數與原稿相同。
2. 逐題核對答案。Claude 與 ChatGPT 的轉換程式會擋下答案缺漏、答案編號超過選項數等格式錯誤，但**格式正確而答案錯誤的題目檢查不出來**。Gemini 沒有這道程式檢查，格式也要自己核對。
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
| 方案資格、選單路徑 | 已於 2026-11-24～25 對照三家官方說明頁（連結在各說明文末）；中文選項名稱**未逐一對照實際畫面** |
| `exam-to-qb.zip` 內容 | 已測試：解開後執行 `build.py`，輸出與正本逐位元相同（52 題，UTF-8 與 Big5） |
| Gemini 安裝含腳本的舊版 | 已實測：**不能執行**，Gemini 回覆不支援含程式碼的自訂技能 |
| Gemini 純文字新版 | 以另一個 AI 模型代測（不准執行程式、一句 prompt）：9 題範例與 40 題單選，題目列全為 27 欄且內容與既有成果相同（40 題未測類別），表頭只少了行尾空白 |
| Gemini 純文字新版（在 Gemini 實測） | 2026-11-25 以 `sample.docx` 產生的 CSV，11 列 27 欄內容與 `sample.csv` 完全相同（UTF-8 無 BOM、LF 換行），**可匯入題庫系統**。第一次測試技能未生效，產出 10 欄的通用格式；刪除技能重新建立後正常 |
| ChatGPT 附件方式 | 2026-11-25 以 Plus 帳號實測，`sample.docx` 產出的 CSV 與 `sample.csv` **逐位元相同**，**可匯入題庫系統** |
| ChatGPT 私人外掛 | 2026-11-25 以 Plus 帳號實測，`sample.docx` 產出的 CSV 與 `sample.csv` **逐位元相同**，**可匯入題庫系統**；Big5 版也**可匯入題庫系統**（未與 `sample_big5.csv` 比對） |
| Claude 安裝技能 | 2026-11-25 以付費帳號實測，`sample.docx` 產出的 CSV 與 `sample.csv` 只差第 8 題填空前的 2 個空白，其餘各格相同，**可匯入題庫系統** |
| 題庫系統匯入網頁版產出的 CSV | Claude（付費帳號）、ChatGPT（Plus）、Gemini 都已實測可匯入 |

## 維護者：更新安裝檔

安裝檔一律由正本 [`skill/exam-to-qb/`](../skill/exam-to-qb/) 產生，不要手動改 ZIP：

```bash
python web/pack.py           # 重新打包
python web/pack.py --check   # 檢查 ZIP 是否落後正本
```

改了正本後要重新打包、commit、push，並通知使用者重新上傳，網頁版不會自動更新。

- `exam-to-qb.zip`：完整技能（含 Python），外層為 `exam-to-qb/`，供 Claude、ChatGPT 使用。
- `exam-to-qb-gemini.zip`：只有 `SKILL.md`，由 [`gemini/SKILL.template.md`](gemini/SKILL.template.md) 產生；「題庫格式」「解析規則」與 CSV 表頭自動取自正本，其餘文字改範本。打包時會檢查樣板列都是 27 欄。
- `build.ps1` 與 `examples/` 在網頁版用不到，不打包。
- 打包時會檢查 `description` 不超過 200 字（Claude 網頁版的上限，三家已知上限中最嚴）。

[`archive/`](archive/) 保留本說明的原始稿，僅供參考，請勿用來安裝。
