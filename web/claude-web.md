# Claude 網頁版：exam-to-qb 安裝與操作

## 使用資格

Free、Pro、Max、Ultra、Team、Enterprise 都可以用，但要開啟程式碼執行。

| 帳號 | 開啟方式 |
|------|----------|
| 個人方案 | **Settings > Capabilities**，打開 **Code execution and file creation**（新版介面稱 Create and edit files） |
| Team／Enterprise | 由組織 Owner 在 **Organization settings > Plugins & skills > Policy** 打開 **Cloud code execution and file creation** 與 **Skills**（Team 預設已開） |

## 安裝（只需一次）

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)，不要解壓縮。
2. 登入 <https://claude.ai>，進入 **Customize > Skills**。
3. 按 **+** → **+ Create skill** → **Upload a skill**，選取 ZIP。
4. 確認清單裡的 `exam-to-qb` 已啟用。

## 使用

第一次請先下載範例 [`sample.docx`](https://github.com/RelerChenTajen/Tools_QB/raw/main/sample.docx) 練習，再與[範例對照表](README.md#範例對照表)比對。

1. 開新對話，附上考題檔（`.docx`、`.pdf`、`.txt`、`.md`；舊版 `.doc` 請先另存成 `.docx`）。
2. 輸入：
   ```
   請使用 exam-to-qb 技能，把附件轉成題庫 CSV，類別填「資訊安全」，並產生 Big5 版。
   ```
3. 下載產生的 CSV，依[匯入前檢查](README.md#匯入前檢查)核對後再匯入。

## 更新與移除

- **更新**：開啟該技能，先關閉，再從 **⋯ > Delete** 刪除，然後上傳新的 ZIP。
- **分享給同事**：Team／Enterprise 可用技能選單的 **Share**（組織要先開放）。個人帳號請同事自行上傳 ZIP。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 找不到 Skills 或 Upload | 程式碼執行沒開，或組織關閉了使用者自建技能 |
| 上傳失敗 | 確認上傳的是 `exam-to-qb.zip`，不是 GitHub 的 Download ZIP，也沒有解壓後重壓 |
| Claude 沒有用到技能 | 提示詞寫明「請使用 exam-to-qb 技能」 |
| 掃描 PDF 讀不完整 | 先轉成 Word 或文字檔 |

## 官方參考

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

官方說明查證於 2026-11-24，選單名稱可能隨改版變動。2026-11-25 實測可產生 CSV 並匯入題庫系統。
