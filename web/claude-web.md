# Claude 網頁版：exam-to-qb 安裝與操作

> **Claude 官方列出的介面語言不含中文**（2026-10-23 版說明），所以下面的選項保留英文，括號內是中文意思。
> 對話不受影響，用中文下指令、Claude 用中文回覆都可以。

## 使用資格

官方說明 Free、Pro、Max、Ultra、Team、Enterprise 都可以用，但要開啟程式碼執行。付費帳號已實測可用（2026-11-25），免費帳號尚未實測。

| 帳號 | 開啟方式 |
|------|----------|
| 個人方案 | **Settings**（設定）→ **Capabilities**（功能），打開 **Code execution and file creation**（程式碼執行與建立檔案）；新版介面稱 **Create and edit files**（建立與編輯檔案） |
| Team／Enterprise | 由組織擁有者在 **Organization settings**（組織設定）→ **Plugins & skills**（外掛與技能）→ **Policy**（政策），打開 **Cloud code execution and file creation**（雲端程式碼執行與建立檔案）與 **Skills**（技能）；Team 的技能預設已開 |

## 安裝（只需一次）

1. 下載 [`exam-to-qb.zip`](https://github.com/RelerChenTajen/Tools_QB/raw/main/web/dist/exam-to-qb.zip)，不要解壓縮。
2. 登入 <https://claude.ai>，進入 **Customize**（自訂）→ **Skills**（技能）。
3. 按 **＋** → **+ Create skill**（建立技能）→ **Upload a skill**（上傳技能），選取 ZIP。
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

- **更新**：開啟該技能，先關閉，再從 **⋯** → **Delete**（刪除）移除，然後上傳新的 ZIP。
- **分享給同事**：Team／Enterprise 可用技能選單的 **Share**（分享），組織要先開放。個人帳號請同事自行上傳 ZIP。

## 常見問題

| 狀況 | 處理 |
|------|------|
| 找不到 **Skills**（技能）或 **Upload a skill**（上傳技能） | 程式碼執行沒開，或組織關閉了使用者自建技能 |
| 上傳失敗 | 確認上傳的是 `exam-to-qb.zip`，不是 GitHub 的 Download ZIP，也沒有解壓後重壓 |
| Claude 沒有用到技能 | 提示詞寫明「請使用 exam-to-qb 技能」 |
| 掃描 PDF 讀不完整 | 先轉成 Word 或文字檔 |

## 官方參考

- [Use skills in Claude（英文）](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom skills（英文）](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [如何以您偏好的語言使用 Claude](https://support.claude.com/zh-TW/articles/10769299)

選項名稱查證於 2026-11-24（英文說明），可能隨改版變動。2026-11-25 以付費帳號實測，可產生 CSV 並匯入題庫系統。
