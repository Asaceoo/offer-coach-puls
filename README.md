# offer-coach

求职全流程 WorkBuddy Skill：岗位截图/JD 分析 → 简历匹配诊断 → 定制简历 → 岗位+行业面试题 → 面试辅导计划 → 面试复盘 → 题库汇总。先看懂岗位，再决定怎么投。

## 特性

- **一键全出**：上传岗位截图 + 简历，一次产出五件套（岗位档案 / 匹配诊断 / 定制简历 / 面试题库 / 岗位池索引）
- **反虚构**：所有建议引用简历原文，缺数据标【待补】不代编；无匹配百分比；面试题给框架不给背诵稿
- **可沉淀**：岗位档案、复盘卡、话术库全部本地落盘，跨会话恢复
- **双轨题库**：每岗位 15~20 题（岗位轨 6~8 / 行业轨 5~7 / 通用轨 4~5），支持英文 JD（中文分析 + 术语对照）

## 安装

把 `offer-coach/` 目录整体复制到 `~/.workbuddy/skills/` 下（用户级）或工作区 `.workbuddy/skills/` 下（项目级），重启会话即可触发。或直接安装 Releases 里的 zip 包。

## 打包与发布

```bash
python scripts/package.py            # patch 递增（v1.0.1 -> v1.0.2）并产出 dist zip
python scripts/package.py --minor    # minor 递增
python scripts/package.py --no-bump  # 不递增重打包
```

脚本自动同步 `docs/用户手册.md` 与 `docs/技术手册.md` 首页版本行。

## 文档

- [用户手册](docs/用户手册.md)
- [技术手册](docs/技术手册.md)

## 边界

不做自动投递、不批量操作招聘账号；数据全部本地存储。

## License

MIT
