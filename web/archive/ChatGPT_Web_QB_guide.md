# Tools_QB：ChatGPT Web 教師操作手冊

2026-11-24｜Web 移植測試版（非原始專案完整鏡像）

## 適用資格
正式 Skills：官方列出符合資格的 Business、Enterprise、Edu、Healthcare，須符合工作區權限。Free、Go、Plus、Pro 可嘗試附件方式，受檔案與程式執行額度限制，非正式安裝。

## A. 正式安裝
1. 下載 skill.zip，毋須解壓縮。
2. 登入 ChatGPT 並選擇有權限的工作區。
3. 左側 Plugins → Skills → Create → Upload from your computer。
4. 選取 ZIP，等待安全掃描結果；若 Needs Review，先審查；Blocked 不可使用。
5. 在新對話上傳考題，輸入下方提示詞。若需分享，Skills 中選取該技能的更多選項 → Share，依權限設定。

## B. 免費帳號／Projects
1. 將 skill.zip 解壓縮，取得 SKILL.md、scripts/build.py、scripts/extract.py、assets/header.csv。
2. 在 ChatGPT 新對話上傳這四個檔案及考題；若檔案限制不足，可嘗試上傳 ZIP 與考題，並要求解壓。若支援 Projects，可將資源加入專案、將 SKILL.md 規則放入專案指令，重複使用。
3. 要求依 SKILL.md 執行，若附件平鋪而非原目錄，執行 build.py 時明確指定 --header 的實際路徑。
4. 若不支援 Python 執行，不得把聊天文字當成已驗證 CSV；改用校方核准環境。

## 提示詞
請依 exam-to-qb 技能轉換附件，類別填「資訊安全」，同時提供 UTF-8 無 BOM 及 Big5（CP950）CSV。保留題幹、選項與原始答案，不得自行補造；列出缺漏、難度推估及編碼異常。驗證版本列及每筆 27 欄後提供下載。

## 驗收
- 檔案有 version: 4 版本列及 27 欄表頭，每筆題目 27 欄。
- 題數及答案與原稿一致，填充題答案以 [*答案*] 表示。
- 類別為選填，線上測驗匯入不支援類別。
- UTF-8 無 BOM；CP950 若發生無法映射字元，以 ? 取代並警告，不應未審查即匯入。
- 使用非正式考題在校方測試環境試匯入，確認格式與題型正確。

## 資安
禁止上傳未經授權的正式考題、學生個資及系統密碼。不要將考題提交至公開 GitHub。先依校方規範確認資料處理權限。

## 技術說明
本包依公開 SKILL.md、build.py、extract.py、header.csv 可讀內容重新實作 Web 版，未取得完整 Git clone，並非原始程式逐位元複製。已通過本地封裝驗證與五題型合成資料測試（含多選、換行、UTF-8、CP950、無效答案拒絕及純文字擷取）。尚未實際於 ChatGPT Skills UI 安裝或校方題庫試匯入，正式發行前須測試。GitHub 原專案未修改。

來源：
- https://github.com/RelerChenTajen/Tools_QB
- https://help.openai.com/en/articles/20001066-skills-in-chatgpt
