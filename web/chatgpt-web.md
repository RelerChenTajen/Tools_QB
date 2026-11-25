# ChatGPT 網頁版：exam-to-qb 安裝與操作

兩種方式擇一：

| 方式 | 適合 | 做法 |
|------|------|------|
| [A：私人外掛](#方式-a私人外掛) | Plus，常常使用 | 建立一次，之後只要附上考題，用 `@` 選外掛 |
| [B：附件](#方式-b附件) | 偶爾使用，或不能建立外掛 | 每次新對話附上 ZIP 和考題 |

> 選項以**中文介面**為準，括號內是英文介面的名稱。要切換語言：個人資料圖示 →「**設定**」（Settings）→「**一般**」（General）→「**語言**」（Language）。

## 使用資格

| 帳號 | 狀態 |
|------|------|
| Plus | 可用：2026-11-25 兩種方式都已實測，`sample.docx` 產出的 CSV 都與 `sample.csv` 逐位元相同，並成功匯入題庫系統 |
| 免費帳號 | 尚未實測。方式 B 可以上傳檔案，但每天只能上傳 3 個，每次轉換會用掉 2 個（ZIP 與考題） |
| 其他方案 | 尚未實測 |

開啟 ZIP 與執行 Python 需要資料分析（Data Analysis）功能，官方說明未列明各方案是否都有。

若 ChatGPT 回覆無法執行 Python，請改用 [Claude 網頁版](claude-web.md)或 [Gemini 網頁版](gemini-web.md)。

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 當考題練習，再與[範例對照表](README.md#範例對照表)比對。

## 方式 A：私人外掛

### 建立外掛（只需一次）

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)（**不要解壓縮**）與範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx)。
   ZIP 的內容：
   ```text
   exam-to-qb/
     SKILL.md
     build.py
     extract.py
     header.csv
   ```
2. 登入 <https://chatgpt.com> 的**個人帳號與個人工作區**，開啟 ChatGPT Work。
3. 在輸入框附上 `exam-to-qb.zip` 和 `sample.docx`，再輸入 `@`，選取 **Plugin Creator**（外掛程式建立工具）。
   找不到時，先到側邊欄「**外掛程式**」（Plugins）的目錄安裝。
4. 在同一則訊息輸入並送出：
   ```
   請將我上傳的 Skill ZIP 封裝成私人外掛，顯示名稱為「考題轉題庫 CSV」。
   SKILL.md、Python 腳本和 header.csv 請原封不動保留，不要改寫、精簡或重新產生。
   建立前請用 sample.docx 實際執行轉換，確認能輸出 UTF-8 無 BOM 與 Big5（CP950）兩版 CSV。
   建立後請提供外掛連結。
   ```
   > 「不要改寫」很重要：ChatGPT 曾自行重寫程式與表頭，產出就不再與正本一致。
5. Plugin Creator 會把技能和支援檔放進 `skills/exam-to-qb/`，產生 `plugin.json`，建立為私人外掛，存在您的**個人帳號**。
6. 開啟它提供的外掛連結；若顯示「**安裝外掛程式**」（Install plugin），按下安裝。
   外掛連結屬於個人，請不要公開張貼。

### 使用外掛

1. 在 ChatGPT Work **開新對話**，附上考題檔，例如 `sample.docx`。
2. 在同一則訊息輸入 `@`，搜尋並點選「**考題轉題庫 CSV**」。也可以從輸入框的「**＋**」選單選取外掛。
3. 接著輸入並送出：
   ```
   請將上傳的考題轉成 27 欄題庫 CSV，類別填「資訊安全」。請實際執行 build.py，並提供 UTF-8 無 BOM 與 Big5（CP950）兩個版本的下載檔。
   ```
4. 下載 CSV。用記事本開啟，第一列應以 `version: 4` 開頭。
5. 依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

`@` 清單找不到時，請用**建立外掛的個人帳號與個人工作區**，到「外掛程式」的「**個人**」（Personal）分頁開啟「考題轉題庫 CSV」。若顯示「安裝外掛程式」，先安裝，再回到 Work 對話選取。

### 更新外掛

技能更新時，在 Work 輸入 `@` 選 **Plugin Creator**，附上新的 `exam-to-qb.zip`，說明「請用附件更新『考題轉題庫 CSV』外掛，檔案原封不動取代」。更新後用 `sample.docx` 再驗證一次。

## 方式 B：附件

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)，**不要解壓縮**（只需下載一次）。
2. 登入 <https://chatgpt.com>，開新對話。
3. 按輸入框的「**＋**」→「**新增相片與檔案**」（Add photos & files），選取 **ZIP 與考題檔，共 2 個檔案**。
   考題可用 `.docx`、`.pdf` 或文字檔；舊版 `.doc` 請先另存成 `.docx`。
4. 輸入：
   ```
   請解壓縮 exam-to-qb.zip，閱讀 SKILL.md，依其流程把考題檔轉成題庫 CSV。
   類別填「資訊安全」，並產生 Big5 版。
   請實際執行 build.py 產生檔案；若無法執行 Python，請直接告訴我，不要用聊天文字代替。
   ```
5. 下載 CSV。用記事本開啟，第一列應以 `version: 4` 開頭。
6. 依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

### 附件方式：用專案重複使用

1. 按側邊欄「**新增專案**」（New project），輸入名稱。
2. 進入專案，用「**新增檔案**」加入解壓後的 `SKILL.md`、`build.py`、`extract.py`、`header.csv` 4 個檔案。
3. 之後在該專案裡開對話，只要附上考題，輸入：
   ```
   請依專案檔案 SKILL.md 的流程，把考題檔轉成題庫 CSV，類別填「資訊安全」，並產生 Big5 版。
   請實際執行 build.py 產生檔案；若無法執行 Python，請直接告訴我。
   ```

專案用法尚未實測。

專案檔案上限為 Free 5 個、Go／Plus 25 個、Pro 以上 40 個。免費帳號受每日 3 個上傳的限制，要分兩天加完。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 找不到「外掛程式」或 Plugin Creator | 帳號方案或工作區未開放；改用方式 B |
| 外掛產出的內容與 `sample.csv` 不同 | 外掛裡的檔案可能被改寫；依〈更新外掛〉重新放入 ZIP |
| 上傳數量已達上限 | 免費帳號每天 3 個；改天再試，或改用其他網頁版 |
| 找不到 `header.csv` | 提示「執行 build.py 時用 `--header` 指定 header.csv 的實際路徑」 |
| 只給文字、沒有檔案 | 要求「實際執行 build.py 並提供下載連結」 |
| 出現 `INVALID question N` | N 是第幾題；對照原稿確認答案後告訴 ChatGPT 修正，再重新產生 |

## 官方參考

- [ChatGPT 中的外掛程式](https://help.openai.com/zh-hant/articles/20001256)
- [將檔案和音訊上傳至 ChatGPT](https://help.openai.com/zh-hant/articles/8555545)
- [使用 ChatGPT 進行資料分析](https://help.openai.com/zh-hant/articles/8437071-data-analysis-with-chatgpt)
- [ChatGPT 中的專案](https://help.openai.com/zh-hant/articles/10169521-projects-in-chatgpt)
- [變更語言設定](https://help.openai.com/zh-hant/articles/8357869)

選項名稱取自 OpenAI 繁體中文說明，查證於 2026-11-25；該說明為機器翻譯，與實際畫面略有不同時，以括號內英文和位置為準。
