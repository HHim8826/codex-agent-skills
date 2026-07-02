[English](./README.md) | 繁體中文

# Codex Agent Skills

這個儲存庫提供可重複使用的 skills，協助以 agent 驅動的軟體專案保持容易
理解、能夠驗證並且易於維護。每個 skill 都遵循 Agent Skills 目錄格式，並以
`SKILL.md` 作為進入點。

## 選擇 skill

這兩個 skills 處理儲存庫生命週期中彼此相關、但階段不同的問題：

- 使用 [`harness-engineering`](./harness-engineering/SKILL.md) 建立或改善
  coding agent 用來規劃、實作、檢查、驗證、review 與交接工作的操作環境。
- 使用 [`entropy-gc`](./entropy-gc/SKILL.md) 找出累積的漂移、排列優先順序、
  清理一個聚焦範圍，並防止相同問題再次發生。

## Harness engineering

`harness-engineering` 把儲存庫視為 agent 的操作環境。它讓專案意圖、命令、
架構、執行階段證據、驗證方式與 Git 狀態足夠明確，使 agent 能安全工作。

### 功能細項

這個 skill 為下列領域提供工作流程與參考資料：

- **從零建立 harness：** 檢查空白或不清楚的儲存庫、起草暫定計畫、每次解決
  一個決策，並只建立最小且有用的 agent-ready 成品。
- **Agent 可讀性：** 把領域用語、工作流程、不變條件、架構、產品規格與進行中
  的計畫保存在容易找到且受版本控制的檔案中。
- **應用程式可讀性：** 讓 agent 能檢查本機網址、worktree 執行個體、種子資料、
  UI 狀態、日誌、指標、追蹤資料與診斷資訊。
- **功能開發：** 定義精簡的功能摘要、把工作切成垂直切片、確認所需的 harness
  支援，並在行為變更時更新長期文件。
- **測試驅動開發：** 選擇一項可觀察行為、先寫一個失敗測試、實作最小的通過
  行為，然後重複這個循環。
- **品質關卡：** 定義穩定的驗證命令，並要求提供行為、架構、測試、執行狀態、
  文件與風險的證據。
- **Review 循環：** 分別執行規格、harness 與架構 review，再把重複意見轉成
  測試、腳本或規則。
- **Git 檢查點：** 記錄起始狀態、提交完整且通過驗證的切片、保護 worktree
  邊界、依需求 push，並回報精確的阻擋原因。
- **工作階段交接：** 只保留恢復工作所需的目前狀態、決策、Git 檢查點、執行
  證據、阻擋項目與下一步。
- **維護：** 找出過時文件、架構漂移、可觀測性不足、缺少執行證據與重複出現
  的 review 問題。

### 使用流程

一般的功能開發或儲存庫改善流程如下：

1. 檢查儲存庫、文件、執行階段進入點與 Git 狀態。
2. 選擇符合任務的參考流程，例如從零規劃、功能開發、應用程式可讀性或維護。
3. 解決會影響計畫的關鍵決策，並保存最小且有用的摘要或執行計畫。
4. 選擇一項可觀察行為，完成一個 red-green-refactor 垂直切片。
5. 使用可重現的證據驗證測試、架構、文件與執行階段行為。
6. Review 規格符合度、harness 品質與架構漂移。
7. 提交完整成果、在流程需要時 push，並只在仍有工作時留下精簡 handoff。

### 使用範例

當你要明確載入這個 skill 時，可以直接在 prompt 中指定。對新的儲存庫，先要求
Codex 建立最小可用的 harness，再開始寫產品程式碼：

```text
使用 $harness-engineering 把這個空白儲存庫改造成 agent-ready 專案。先檢查
現有資訊，執行內建規劃訪談，並提出最小的驗證與執行階段檢查命令。
```

對既有專案的功能工作，可以同時寫明完成條件：

```text
使用 $harness-engineering 新增帳務健康檢查端點。建立精簡的功能摘要、完成一個
垂直 TDD 切片、在執行階段驗證端點、通過 review 與品質關卡，最後提交並 push
通過驗證的檢查點。
```

第二個範例會要求 skill 檢查既有儲存庫、定義可觀察的端點行為、只新增該功能
需要的 harness 支援、保留驗證證據，並以明確的 Git 結果收尾。

## Entropy GC

`entropy-gc` 把儲存庫清理轉成以證據為基礎的維護循環。掃描結果只是需要人工
確認的訊號，不是自動重構的授權。

### 功能細項

這個 skill 提供聚焦清理與防止漂移的工作流程：

- **機械式稽核：** 掃描大型檔案、過時標記、型別或 lint 逃生出口、重複 helper
  名稱、缺少的 harness 成品與文件 placeholder。
- **人工稽核：** 檢查重複 review 意見、分歧的 helper、不一致的領域用語、過時
  計畫、薄弱測試與無法有效診斷問題的資訊。
- **風險排序：** 優先處理使用者可見與資料風險，其次是安全性、可靠性、agent
  混淆、review 成本與清理成本。
- **聚焦 collect：** 選擇一個發現或最多三個相關發現，不混入大範圍格式化或
  無關的行為變更。
- **防護升級：** 把重複漂移轉成測試、lint 規則、架構檢查、文件規則、掃描
  模式、CI 關卡或 review checklist。
- **Golden principles：** 記錄三到七條具體的儲存庫規則，每條規則都連到一種
  執行方式或預定的自動化步驟。
- **品質追蹤：** 維護可採取行動的品質分數與技術債追蹤器，記錄證據、風險、
  負責區域與下一個最小清理項目。
- **週期排程：** 只有在本機命令穩定，且 false positives 有 review 流程後，
  才加入人工、CI 或 cron 排程。

### 使用流程

完整的 entropy-GC 循環如下：

1. 執行內附的 scanner，並檢查它提供的證據。
2. 人工檢查靜態模式無法偵測的漂移。
3. 依使用者風險、營運風險、agent 混淆與成本排列發現。
4. 記錄 false positives，並選擇一個小而訊號明確的清理切片。
5. 保持公開行為不變、完成清理，並在可行時加入防止復發的 guardrail。
6. 執行相關驗證，並更新 entropy 報告、品質分數或技術債追蹤器。
7. 記錄剩餘技術債，並只在掃描結果穩定後加入排程。

### 使用範例

需要先取得風險排序報告、還不打算修改程式碼時，可以要求執行 audit：

```text
使用 $entropy-gc 稽核這個儲存庫。執行保守的 scanner、對照程式碼與專案意圖
確認結果、排列風險，並建議一個小型清理切片，但先不要實作。
```

如果 skill 安裝在儲存庫的 `.agents/skills`，可以直接執行內附 scanner：

```shell
python .agents/skills/entropy-gc/scripts/entropy_scan.py .
python .agents/skills/entropy-gc/scripts/entropy_scan.py . --json
```

確認發現後，可以要求執行聚焦的 collect：

```text
使用 $entropy-gc 整併 entropy 報告中重複的 API 回應 adapters。保持公開行為
不變、加入回歸 guardrail、執行相關驗證，並記錄剩餘技術債。
```

## 安裝

若要為單一專案安裝全部 skills，請把這個儲存庫 clone 到該專案的
`.agents/skills` 目錄：

```shell
git clone https://github.com/HHim8826/codex-agent-skills.git .agents/skills
```

如果 `.agents/skills` 已存在，請先把儲存庫 clone 到其他位置，再只複製需要的
skill 目錄。每個 `SKILL.md` 必須位於
`.agents/skills/<skill-name>/SKILL.md`。

## 叫用 skill

當請求符合 `description` frontmatter 中的觸發條件時，Codex 會載入對應 skill。
你也可以在 prompt 中直接使用 `$harness-engineering` 或 `$entropy-gc` 指定 skill。

開啟所選 skill 的 `SKILL.md` 可查看操作規則。只載入與目前任務相符的參考流程
檔案。

## 儲存庫驗證

發布變更前，請在這個儲存庫的根目錄執行下列檢查：

```shell
python harness-engineering/scripts/check_workflow_contract.py
python -m py_compile harness-engineering/scripts/check_workflow_contract.py
python -m py_compile entropy-gc/scripts/entropy_scan.py
python entropy-gc/scripts/entropy_scan.py --help
```

## 授權

這個儲存庫採用 [MIT License](./LICENSE)。
