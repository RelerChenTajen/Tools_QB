# ChatGPT 網頁版：exam-to-qb 操作說明

不必安裝，每次新對話附上 ZIP 和考題，說一句話，就能拿到題庫 CSV。

## 使用資格

各方案的帳號都可以上傳檔案。開啟 ZIP 與執行 Python 需要 Data Analysis 功能，官方說明未列明各方案是否都有；若 ChatGPT 回覆無法執行，請改用 [Claude 網頁版](claude-web.md)或 [Gemini 網頁版](gemini-web.md)。

免費帳號每天只能上傳 3 個檔案。

## 使用

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 當考題練習，再與[範例對照表](README.md#範例對照表)比對。

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)，**不要解壓縮**（只需下載一次）。
2. 登入 <https://chatgpt.com>，開新對話，上傳 **ZIP 與考題檔，共 2 個檔案**。
   考題可用 `.docx`、`.pdf` 或文字檔；舊版 `.doc` 請先另存成 `.docx`。
3. 輸入：
   ```
   請解壓縮 exam-to-qb.zip，閱讀 SKILL.md，依其流程把考題檔轉成題庫 CSV。
   類別填「資訊安全」，並產生 Big5 版。
   請實際執行 build.py 產生檔案；若無法執行 Python，請直接告訴我，不要用聊天文字代替。
   ```
4. 下載 CSV。用記事本開啟，第一列應以 `version: 4` 開頭。
5. 依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

## 想重複使用

建立 Project，加入解壓後的 `SKILL.md`、`build.py`、`extract.py`、`header.csv` 4 個檔案，之後在該 Project 裡只要附上考題。

專案檔案上限為 Free 5 個、Go／Plus 25 個、Pro 以上 40 個。免費帳號受每日 3 個上傳的限制，要分兩天加完。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 上傳數量已達上限 | 免費帳號每天 3 個；改天再試，或改用其他網頁版 |
| 找不到 `header.csv` | 提示「執行 build.py 時用 `--header` 指定 header.csv 的實際路徑」 |
| 只給文字、沒有檔案 | 要求「實際執行 build.py 並提供下載連結」 |
| 出現 `INVALID question N` | N 是第幾題；對照原稿確認答案後告訴 ChatGPT 修正，再重新產生 |

## 官方參考

- [Uploading files](https://help.openai.com/en/articles/8555545)
- [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

官方說明查證於 2026-11-24，選單名稱可能隨改版變動。
