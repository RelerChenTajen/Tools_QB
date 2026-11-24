# Gemini Web 介面使用 GitHub SKILL 指南

GitHub 上的這類 **SKILL 專案**（例如包含 `SKILL.md` 結構與配套腳本/規範的儲存庫，如 `https://github.com/RelerChenTajen/Tools_QB.git`）主要是遵循開放的 Agent Skills 標準設計，專為 **Gemini CLI** 或 **Antigravity IDE** 等本地開發環境的 Agent 擴充所打造。

針對 **Gemini 網頁版（Web 介面）** 的使用資格與操作方式，依帳號類型與使用情境整理如下：

---

## 1. 使用資格：需要付費訂閱嗎？

這取決於您使用的 Gemini 網頁版環境與匯入方式：

* **一般個人版 Gemini 網頁介面（`gemini.google.com`）— 免費版即可，不強制訂閱**
  * **直接匯入 GitHub 儲存庫（Import code）：** 免費版帳號只要年滿 18 歲並開啟「保留活動記錄（Keep Activity）」，即可在網頁版透過「匯入程式碼」功能掛載公開的 GitHub Repo（上限 5,000 個檔案、100 MB）。
  * **建立 Gems 模擬 Skill：** 若要在個人版長期重複使用該 Skill 的指令，可透過 **Gems** 功能將 `SKILL.md` 設為自訂指令（個人免費版亦可使用自訂 Gems，若需進階模型或更大上下文容量則建議訂閱 Google One AI Premium）。
* **企業版 / 教育版（Gemini Enterprise Web App）— 需具備對應授權方案**
  * 若使用組織帳號登入 **Gemini Enterprise** 網頁版，其內建原生的 **Skills 管理介面**，可直接上傳 `SKILL.md` 或 ZIP 壓縮檔，此功能需具備支援的 Google Workspace / Gemini Enterprise 企業訂閱授權。

> **註：** 若目標為私人（Private）GitHub 儲存庫，無論免費或付費帳號，都必須先在 Gemini 設定的「已連結的應用程式（Connected Apps）」中綁定您的 GitHub 帳號才能讀取。

---

## 2. 使用方式：在 Gemini Web 介面如何操作？

由於一般消費端 `gemini.google.com` 網頁版不像本地端（如 Gemini CLI 或 Antigravity）能自動讀取 `.agents/skills` 資料夾並執行本地 Terminal 腳本，在網頁介面有以下三種對應的操作方式：

### 方法 A：單次對話直接掛載 GitHub Repo
*適用情境：單次任務執行、直接針對專案提問或分析*

1. 在電腦瀏覽器開啟 **`gemini.google.com`**。
2. 點擊底部輸入框左側的 **`+`（新增檔案 / 上傳）** $\rightarrow$ 選擇 **「匯入程式碼（Import code）」**。
3. 貼上網址 `https://github.com/RelerChenTajen/Tools_QB.git`（或該 Repo 網頁網址）並點擊 **匯入**。
4. 匯入完成後，直接在對話框下指令，例如：
   > 「請讀取專案中的 `SKILL.md` 規範，並依照該技能的流程幫我處理以下任務……」

> **注意事項：** 網頁版匯入的是當下的快照，不會自動同步 GitHub 後續的 Commit 更新；此外網頁版僅能讀取檔案內容，無法直接執行該 Skill 內的本地 Python / Shell 腳本。

### 方法 B：建立專屬 Gem
*適用情境：長期重複使用、免去每次重新匯入的步驟*

1. 開啟 GitHub 專案中的核心指令檔（`SKILL.md`）與必要的參考規範檔，複製其內容（建議移除最上方給 CLI 判讀的 YAML Frontmatter 區塊，只保留核心角色設定、執行步驟與輸出格式）。
2. 在 `gemini.google.com` 左側選單點擊 **「探索 Gems（Explore Gems）」** $\rightarrow$ **「新增 Gem（New Gem）」**。
3. 將複製的 Skill 指令貼入 **「指令（Instructions）」** 欄位；若該 Skill 附帶範本或參考文件（如 `references/` 或 `examples/` 內的 `.md` 檔），可一併上傳至 Gem 的 **「知識（Knowledge）」** 檔案區。
4. 儲存後，日後只要開啟該 Gem 對話，就能直接套用這套 Skill 規範。

### 方法 C：Gemini Enterprise 網頁版原生上傳
*適用情境：企業 / 組織授權帳號*

1. 登入 **Gemini Enterprise** 網頁版，在左側導覽列點擊 **「Skills」**。
2. 點擊新增圖示並選擇 **「Upload skill（上傳技能）」**。
3. 直接上傳該專案內的 `SKILL.md`（若包含 `scripts/` 或 `references/` 等子資料夾，需打包成包含 `SKILL.md` 的 ZIP 檔上傳）。
4. 匯入並啟用後，在對話框輸入 **`/`** 或 **`@技能名稱`** 即可直接呼叫。