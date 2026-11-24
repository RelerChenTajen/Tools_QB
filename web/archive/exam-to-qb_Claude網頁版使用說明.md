# exam-to-qb 技能：Claude 網頁版使用說明

來源 repo：<https://github.com/RelerChenTajen/Tools_QB>
技能位置：`skill/exam-to-qb/`（作用是把考題檔轉成 27 欄的題庫 CSV）

---

## 一、使用資格：不需要付費訂閱

- **方案：** Skills 開放給 Free、Pro、Max、Ultra、Team 和 Enterprise 方案的使用者，所以免費帳號也能用。
- **唯一的前提：** 需要開啟程式碼執行。個人方案要到「設定」裡確認 **Code execution and file creation（建立與編輯檔案）** 已打開。
- **Team／Enterprise 帳號：** 這個設定和 Skills 的開關由組織的 Owner 控制。學校如果是用組織帳號，要先請管理者打開。

## 二、在 Claude 網頁版的使用方式

1. **上傳技能：** 到 **Customize > Skills**，選 **Upload a skill**，上傳包含技能資料夾的 ZIP 檔。網頁版不能直接貼 GitHub 網址安裝，一定要上傳 ZIP。ZIP 最外層必須是 `exam-to-qb/` 資料夾，裡面放 `SKILL.md`：

   ```
   exam-to-qb.zip
   └── exam-to-qb/
       ├── SKILL.md
       ├── build.py
       ├── extract.py
       ├── build.ps1
       ├── header.csv
       └── examples/
   ```

2. **確認已啟用：** 上傳後，在 **Customize > Skills** 裡啟用這個技能。
3. **直接用就好：** 開新對話、附上考題檔，然後說「把這份考題轉成題庫 CSV」。只要你描述的工作符合技能的名稱或描述，Claude 就會自動載入它。

## 三、讓學生或同事自己安裝時要注意

- **ZIP 不要直接用 GitHub 的「Download ZIP」**：那樣下載的最外層會是 `Tools_QB-main/`，而且包含題庫資料，上傳會失敗或不正確。建議在 repo 的 Releases 放一份只含 `exam-to-qb/` 的 ZIP，或在 README 加一段網頁版的安裝說明。
- **README 列的安裝路徑網頁版用不到**：`~/.claude/skills/` 那些路徑和 `install.sh`／`install.ps1` 只適用於 Claude Code、Codex、Gemini CLI。
- **Python 腳本在網頁版可以直接跑**：`build.py` 和 `extract.py` 只用到 Python 標準函式庫，不用額外安裝套件。`build.ps1` 在網頁版的 Linux 環境跑不了，但 SKILL.md 已經寫明新流程一律用 `build.py`，所以沒有影響。
- **`extract.py` 只處理 docx／txt／md**：上傳 PDF 或 .doc 時，Claude 會改用環境裡的其他工具取文字，通常可行，但結果較難預測。如果要給學生用，可以考慮在 SKILL.md 寫明 PDF 的處理方式。

---

## 參考資料

- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Teach Claude your way of working using skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)
