# Gemini 網頁版：exam-to-qb 安裝與操作

安裝一次技能後，附上考題、說一句話，就能拿到題庫 CSV。不必安裝 Python，也不必在電腦上執行程式。

> 選項以**繁體中文介面**為準，括號內是英文介面的名稱（查得到才附）。

## 使用資格

個人 Google 帳號，滿 18 歲（免費可用）。學校或公司的 Workspace 帳號尚未開放技能，請改用 [Claude 網頁版](claude-web.md)。

## 安裝技能（只需一次）

以下為電腦瀏覽器的步驟。

1. 下載 [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip)，**不要解壓縮**。
2. 登入 <https://gemini.google.com>，按側邊欄的「**自訂**」（Customize）；沒看到就先按「**更多**」（More）。
3. 在頁面上方選「**技能**」（Skills）。
4. 已安裝過舊版的，先把滑鼠移到該技能上，按「**更多**」（More）→「**刪除**」（Delete）。刪除後無法復原。
5. 按「**建立**」（Create）→「**上傳**」（Upload），選取 ZIP，按「**開啟**」（Open）。
6. 不必新增其他檔案；若出現「**上傳**」（Upload）按鈕就按下。
7. 檢查內容後，按頁面上方的「**建立**」（Create），並確認技能沒有停用。已停用時，選「**啟用**」（Activate）。

## 使用

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 練習，再與[範例對照表](README.md#範例對照表)比對。

1. 按左上角「**新的對話**」（New chat）。
2. 按輸入框的「**新增檔案**」→「**上傳檔案**」，選考題（`.docx`、`.pdf` 或文字檔；舊版 `.doc` 請先另存成 `.docx`）。
3. 輸入 `@` 選 `exam-to-qb`，再輸入：
   ```
   請把附件轉成題庫 CSV，類別：資訊安全
   ```
   不需要類別就省略「，類別：資訊安全」。完成後按「**提交**」。
4. 下載 Gemini 產生的 `.csv`。用記事本開啟，第一列應為 `version: 4` 開頭；不是的話，見[常見問題](#常見問題)第一項。
5. 看完 Gemini 回報的疑問題號，依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

### 沒有檔案，或下載連結打不開

1. 輸入：
   ```
   請把完整 CSV 放在一個程式碼區塊
   ```
2. 按程式碼區塊下方的「**複製**」（Copy），貼到記事本。
3. 記事本「**檔案 > 另存新檔**」：檔名 `exam.csv`、存檔類型「**所有檔案**」、編碼「**UTF-8**」。

### 題庫系統只收 Big5

用記事本開啟 CSV，「**檔案 > 另存新檔**」，編碼選「**ANSI**」（繁體中文 Windows 的 ANSI 就是 Big5）。若跳出「部分字元會遺失」的警告，先把 `≥`、`≤` 改成 `≧`、`≦`，再找出其他特殊字元改寫。

> 不要用 Excel 開啟後直接存檔，換行與編碼可能被改掉。

## 換一句話就能做的事

| 需求 | 輸入 |
|------|------|
| 依章節分類 | `請把附件轉成題庫 CSV，類別用各章節標題` |
| 修改一題 | `第 5 題答案改成 (C)，重新產生 CSV` |
| 補上確認過的答案 | `第 8 題答案是 (B)，重新產生 CSV` |
| 檢查一次 | `請逐題核對題數、答案和 27 欄，有錯就修正並重新產生 CSV` |

## 常見問題

| 狀況 | 處理 |
|------|------|
| CSV 第一列不是 `version: 4`，或無法匯入 | 技能沒有生效。到「技能」頁刪除（「**更多**」→「**刪除**」），依安裝步驟重新建立（實測有效），建議按「**新的對話**」重做 |
| Gemini 說不支援執行程式或腳本 | 安裝到舊版；刪除技能後，下載新的 ZIP 重新上傳 |
| 找不到「自訂」或「技能」 | 可能是學校帳號、未滿 18 歲，或尚未登入 |
| 上傳失敗 | 確認用的是 `exam-to-qb-gemini.zip`，且沒有解壓後重壓 |
| 技能沒有作用 | 確認已啟用並用 `@` 選取，且沒有同時開 Canvas 或 Deep Research |
| 產生的是 Google 試算表或 Excel | 輸入「請改成純文字 CSV 檔」 |
| 題目很多，內容不完整 | 每次附 50 題以內，或請它「從第 N 題繼續」 |
| 匯入時欄位錯位 | 輸入上表「檢查一次」那句，或改用 [Claude 網頁版](claude-web.md) |

## 與 Claude、ChatGPT 版的差別

Gemini 版的 CSV 由 AI 直接寫出，**沒有經過 `build.py` 的格式檢查**，所以匯入前要核對得更仔細。重要考試或大量題目，建議用 [Claude 網頁版](claude-web.md)。

## 官方參考

- [建立及管理技能](https://support.google.com/gemini/answer/17094296?hl=zh-Hant&co=GENIE.Platform%3DDesktop)
- [Gemini 在對話中產生檔案（英文）](https://blog.google/innovation-and-ai/products/gemini-app/generate-files-in-gemini/)
- [上傳及分析檔案](https://support.google.com/gemini/answer/14903178?hl=zh-Hant&co=GENIE.Platform%3DDesktop)
- [使用 Gemini 系列應用程式](https://support.google.com/gemini/answer/13275745?hl=zh-Hant&co=GENIE.Platform%3DDesktop)

選項名稱取自 Google 繁體中文說明，查證於 2026-11-25；該說明註明可能含 AI 翻譯，與實際畫面略有不同時，以括號內英文和位置為準。官方未說明技能與產生檔案能否並用；2026-11-25 實測可產生 CSV 並匯入題庫系統。
