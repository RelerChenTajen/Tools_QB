# ChatGPT 網頁版：exam-to-qb 安裝與操作

## 使用資格

| 帳號 | 做法 |
|------|------|
| Business、Enterprise、Edu、Healthcare | [方式 A：安裝技能](#方式-a安裝技能)（須工作區允許） |
| Free、Go、Plus、Pro | [方式 B：附件](#方式-b附件)。官方的 Skills 適用名單未列這些方案 |

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 當考題練習，再與[範例對照表](README.md#範例對照表)比對。

## 方式 A：安裝技能

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)，不要解壓縮。
2. 登入 <https://chatgpt.com>，切換到有權限的工作區。
3. 側邊欄 **Plugins** → **Skills** 分頁 → **Create** → **Upload from your computer**，選取 ZIP。
4. 等待掃描：

   | 結果 | 意義 |
   |------|------|
   | 正常 | 可以使用 |
   | Needs Review | 先看過提示資訊再使用 |
   | Blocked | 不能使用，請洽工作區管理者 |

5. 開新對話，附上考題，輸入：
   ```
   請使用 exam-to-qb 技能，把附件轉成題庫 CSV，類別填「資訊安全」，並產生 Big5 版。
   ```
6. 下載 CSV，依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

**分享**：Skills 分頁 → 技能的 **⋯ > Share**。同事在 **Shared with me** 找到後按 **⋯ > Install**。

**管理者**：Enterprise／Edu 在 **Permissions & roles** 要開啟 **Enable skills** 與 **Enable skill uploading**；要讓教師分享另開 **Share skills**。

## 方式 B：附件

不算正式安裝，每次新對話都要附上。

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)。
2. 開新對話，上傳 **ZIP 與考題檔，共 2 個檔案**。
   免費帳號每天只能上傳 3 個檔案，所以不要解壓成 4 個檔再傳。
3. 輸入：
   ```
   請解壓縮 exam-to-qb.zip，閱讀 SKILL.md，依其流程把考題檔轉成題庫 CSV。
   類別填「資訊安全」，並產生 Big5 版。
   請實際執行 build.py 產生檔案；若無法執行 Python，請直接告訴我，不要用聊天文字代替。
   ```
4. 下載 CSV，依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

**想重複使用**：建立 Project，加入解壓後的 `SKILL.md`、`build.py`、`extract.py`、`header.csv` 4 個檔案。專案檔案上限為 Free 5 個、Go／Plus 25 個、Pro 以上 40 個。免費帳號受每日 3 個上傳的限制，要分兩天加完。

> 開啟 ZIP 與執行 Python 都需要 Data Analysis 功能，官方說明未列明各方案是否都有。
> 若 ChatGPT 回覆無法執行，請改用 [Claude 網頁版](claude-web.md)。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 找不到 Plugins 或 Skills | 帳號方案不在適用名單，或工作區未開放；改用方式 B |
| 找不到 `header.csv` | 提示「執行 build.py 時用 `--header` 指定 header.csv 的實際路徑」 |
| 只給文字、沒有檔案 | 要求「實際執行 build.py 並提供下載連結」 |

## 官方參考

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)
- [Uploading files](https://help.openai.com/en/articles/8555545)

查證日期 2026-11-24，選單名稱可能隨改版變動。
