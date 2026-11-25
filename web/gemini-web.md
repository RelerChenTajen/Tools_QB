# Gemini 網頁版：exam-to-qb 安裝與操作

> **Gemini 不能執行技能裡的程式。** 2026-11-25 實際安裝後，Gemini 回覆不支援執行含程式碼或腳本的自訂技能。
> 所以 Gemini 版分兩段：**Gemini 解析考題成 TSV → 您的電腦把 TSV 轉成 CSV**。
> 不想在電腦上執行程式，請改用 [Claude 網頁版](claude-web.md)。

## 使用資格

| 帳號 | 做法 |
|------|------|
| 個人 Google 帳號，滿 18 歲（免費可用） | [第 2 步的方式 A：安裝技能](#方式-a安裝技能) |
| 學校或公司的 Workspace 帳號 | Skills 尚未開放，用[第 2 步的方式 B：附件](#方式-b附件) |

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 當考題練習：

| 完成後 | 與這個檔案比對 |
|--------|----------------|
| 第 3 步的 TSV | [`sample.tsv`](../sample.tsv) |
| 第 4 步的 CSV | [`sample.csv`](../sample.csv)、[`sample_big5.csv`](../sample_big5.csv)，或[範例對照表](README.md#範例對照表) |

Gemini 還沒裝好也可以先測試電腦：下載 [`sample.tsv`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.tsv)，改名為 `rows.tsv`，直接做第 4 步的第 3 小步。

## 第 1 步：準備電腦（只需一次）

1. 安裝 [Python](https://www.python.org/downloads/) 3.7 以上。Windows 安裝時勾選 **Add python.exe to PATH**。
2. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip) 並**解壓縮**，會得到 `exam-to-qb` 資料夾，裡面有 `build.py` 和 `header.csv`。

## 第 2 步：安裝技能或附上規則

### 方式 A：安裝技能

只需一次，以下為電腦瀏覽器的步驟。

1. 下載 [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip)，**不要解壓縮**。
2. 登入 <https://gemini.google.com>，側邊欄 **Customize**（沒看到先按 **More**）→ **Skills**。
3. 已安裝過舊版的，先在該技能按 **More > Delete** 刪除。
4. **Create** → **Upload**，選取 ZIP，按 **Open**。
5. 檢查內容後按 **Create**，並確認技能為啟用狀態。

### 方式 B：附件

每次新對話都要做。把 `exam-to-qb-gemini.zip` 解壓縮，將裡面的 `SKILL.md` 和考題一起附加到對話。

## 第 3 步：請 Gemini 產生 TSV

1. 開新對話，附上考題（`.docx`、`.pdf` 或文字檔；舊版 `.doc` 請先另存成 `.docx`）。
2. 依第 2 步的方式輸入：
   - **方式 A**：輸入 `/`（部分帳號為 `@`）選 `exam-to-qb`，再輸入
     ```
     請把附件考題轉成題庫，類別填「資訊安全」。
     ```
   - **方式 B**：
     ```
     請依附件 SKILL.md 的規則，把考題轉成題庫 TSV，類別填「資訊安全」。
     ```
3. Gemini 會給一個 TSV 程式碼區塊，以及題數、有疑問的題號。先看完有疑問的題目。

## 第 4 步：在電腦轉成 CSV

1. 按程式碼區塊右上角的**複製**，不要用滑鼠選取，以免 TAB 變成空白。
2. 貼到記事本，**另存新檔**到 `exam-to-qb` 資料夾：檔名 `rows.tsv`、存檔類型「所有檔案」、編碼 **UTF-8**。
   章節類別不同時，Gemini 會多給一個類別區塊，另存成 `rows.cats`。
3. 開啟 `exam-to-qb` 資料夾，在檔案總管的網址列輸入 `cmd` 按 Enter，執行：
   ```
   python build.py --tsv rows.tsv --out exam.csv --category "資訊安全" --big5
   ```
   | 需求 | 改法 |
   |------|------|
   | 不填類別 | 拿掉 `--category "資訊安全"` |
   | 各章類別不同 | 把 `--category "資訊安全"` 換成 `--category-file rows.cats` |
   | 不要 Big5 版 | 拿掉 `--big5` |

   macOS 請在終端機用 `python3`。
4. 看到 `OK -> exam.csv` 就完成了，Big5 版是 `exam_big5.csv`。依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

## 常見問題

| 狀況 | 處理 |
|------|------|
| Gemini 說不支援執行程式或腳本 | 安裝到舊版；刪除技能後，下載新的 `exam-to-qb-gemini.zip` 重新上傳 |
| 找不到 Customize 或 Skills | 可能是學校帳號、未滿 18 歲，或尚未登入；改用方式 B |
| 上傳失敗 | 確認用的是 `exam-to-qb-gemini.zip`，且沒有解壓後重壓 |
| 技能沒有作用 | 確認已啟用，且沒有同時開 Canvas 或 Deep Research |
| TSV 內容不完整 | 輸入「請從第 N 題繼續，格式相同」，再接到檔案後面 |
| 每一題都出現 `INVALID ... type must be 1-5` | TAB 變成空白了；重新用複製鈕複製 |
| 某幾題 `INVALID question N` | N 是第幾題；對照原稿修正 `rows.tsv`，或請 Gemini 重做該題 |
| 原稿本來就缺答案，仍要輸出 | 指令最後加 `--allow-invalid`，匯入前再補上答案 |
| 找不到 `python` 指令 | 重新安裝 Python 並勾選 Add python.exe to PATH，或改用 `py` |
| `rows.tsv` 找不到 | 檔名可能變成 `rows.tsv.txt`；另存時類型要選「所有檔案」 |

## 補充

- **Gems 正由 Skills 取代**：滿 18 歲的個人帳號，Gems 已於 2026-11-17 轉為唯讀，2026-12-17 移除。教育版 Workspace 為 2027 年 6 月，商業、企業與非營利版為 2027 年 3 月。
- **Gemini Enterprise**（另一項產品）：官方列明支援技能內的 Python。管理者開啟 Skills 後，可在 **Skills → 新增圖示 → Upload skill** 上傳完整版 `exam-to-qb.zip`；不能執行時改用本頁流程。Frontline 版不能上傳。

## 官方參考

- [Create & manage skills](https://support.google.com/gemini/answer/17094296)
- [Gems 轉換為 Skills 的時程](https://support.google.com/gemini/answer/18560919)
- [Attach & analyze files](https://support.google.com/gemini/answer/14903178)
- [Gemini Enterprise：Skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills)

官方說明查證於 2026-11-24，選單名稱可能隨改版變動。
