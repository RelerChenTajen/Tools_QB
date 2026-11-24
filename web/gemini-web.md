# Gemini 網頁版：exam-to-qb 安裝與操作

> **Gems 正由 Skills 取代。** 滿 18 歲的個人帳號，Gems 已於 2026-11-17 轉為唯讀（不能使用、編輯或新增），2026-12-17 移除。教育版 Workspace 為 2027 年 6 月，商業、企業與非營利版為 2027 年 3 月。

## 使用資格

| 帳號 | 做法 |
|------|------|
| 個人 Google 帳號，滿 18 歲（免費可用） | [方式 A：安裝技能](#方式-a安裝技能) |
| 學校或公司的 Workspace 帳號 | Skills 尚未開放，用[方式 B：匯入 GitHub](#方式-b匯入-github) |
| Gemini Enterprise（另一項產品） | [方式 C：Gemini Enterprise](#方式-cgemini-enterprise) |

## 方式 A：安裝技能

以下為電腦瀏覽器的步驟。

1. 下載 [`exam-to-qb-gemini.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb-gemini.zip)，不要解壓縮。
2. 登入 <https://gemini.google.com>，側邊欄 **Customize**（沒看到先按 **More**）→ **Skills**。
3. **Create** → **Upload**，選取 ZIP，按 **Open**。
4. 檢查內容後按 **Create**，並確認技能為啟用狀態。
5. 開新對話，附上考題，輸入 `/`（部分帳號為 `@`）選 `exam-to-qb`，再輸入：
   ```
   把附件轉成題庫 CSV，類別填「資訊安全」，並產生 Big5 版。
   請實際執行 build.py 產生檔案；若無法執行 Python，請直接告訴我。
   ```
6. 若能執行：下載 CSV，依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。
   若不能執行：改做[備用流程](#備用流程gemini-不能執行-python-時)。

**更新**：技能頁 **More > Replace skill**，上傳新的整包 ZIP。
**分享**：Skills 頁 → **More > Share skill**，檔案也要一併分享。

## 方式 B：匯入 GitHub

每個對話都要重新匯入。個人帳號須滿 18 歲並開啟 **Keep Activity**；學校帳號須有符合的 Workspace 版本並由管理者開放。

1. 在電腦瀏覽器登入 <https://gemini.google.com>。
2. 輸入框 **More Uploads → Import code**，貼上 `https://github.com/RelerChenTajen/Tools_QB`，按 **Import**。
3. 附上考題，輸入：
   ```
   請閱讀 skill/exam-to-qb/SKILL.md，依其規則解析附件考題。
   ```
4. 接著做[備用流程](#備用流程gemini-不能執行-python-時)。匯入的是當下快照，不會跟著 GitHub 更新。

## 方式 C：Gemini Enterprise

管理者須先開啟 Skills。Standard、Plus、Pay-as-you-go 可上傳，Frontline 不行。

1. 登入 Gemini Enterprise 網頁版，導覽選單 **Skills**。
2. 按新增圖示 → **Upload skill**，選 `exam-to-qb-gemini.zip`，按 **Import**。
3. 官方支援技能內的 Python，但未說明能否下載產出的 CSV；不行時改做備用流程。

## 備用流程：Gemini 不能執行 Python 時

Google 的個人版說明只寫可以上傳 `.py`，**沒有寫明會執行**。這時由 Gemini 解析題目，由自己的電腦轉檔：

1. 輸入：
   ```
   請依 SKILL.md 的格式，把全部題目輸出成 TSV，放在一個程式碼區塊裡。
   每題一行，欄位以 TAB 分隔，欄位內換行寫成 \n，不要加表頭。
   ```
2. 複製程式碼區塊，用純文字編輯器存成 `rows.tsv`（UTF-8）。確認欄位間是 TAB，不是空白。
3. 電腦安裝 Python 3.7 以上，解壓安裝檔，把 `rows.tsv` 放在同一個資料夾，執行：
   ```bash
   python build.py --tsv rows.tsv --out exam.csv --category "資訊安全" --big5
   ```
4. 依[匯入前檢查](README.md#匯入前檢查)核對。

不想在電腦上執行 Python，請改用 [Claude 網頁版](claude-web.md)。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 找不到 Customize 或 Skills | 可能是學校帳號、未滿 18 歲，或尚未登入 |
| 上傳失敗 | 確認用的是 `-gemini.zip`，`SKILL.md` 要在 ZIP 最外層 |
| 技能沒有作用 | 確認已啟用，且沒有同時開 Canvas 或 Deep Research |

## 官方參考

- [Create & manage skills](https://support.google.com/gemini/answer/17094296)
- [Gems 轉換為 Skills 的時程](https://support.google.com/gemini/answer/18560919)
- [Import a GitHub repository](https://support.google.com/gemini/answer/16176929)
- [Attach & analyze files](https://support.google.com/gemini/answer/14903178)
- [Gemini Enterprise：Skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills)

查證日期 2026-11-24，選單名稱可能隨改版變動。
