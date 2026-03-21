# 船长清单（ShipMate）

一款面向中文用户的「AI 日计划 + 专注 + 复盘」iOS 应用。

## 为什么选这个方向
- 榜单长期稳定需求：效率/生产力 + 习惯养成 + AI 助手
- 商业化清晰：订阅制（高级 AI 次数、模版、数据导出）
- 技术风险低：MVP 可在 2-3 周完成并上架 TestFlight

## MVP 核心能力（可上架）
1. 今日三件事（MIT）
2. 番茄专注计时（25/5）
3. AI 晚间复盘（自动生成总结与明日建议）
4. 本地数据存储 + iCloud 同步预留

## 技术栈
- Flutter 3.x（iOS 首发，后续可扩 Android）
- 本地存储：Hive/Isar（二选一，先 Hive）
- AI：可插拔（先接 OpenAI 兼容接口）
- 埋点：Firebase Analytics（MVP 可选）

## 目录
- PRD.zh-CN.md：产品需求文档
- appstore/metadata-template.md：上架素材模板
- roadmap.md：执行排期与里程碑
