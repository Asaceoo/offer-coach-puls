# offer-coach

> 求职全流程教练：**先看懂岗位，再决定怎么投。**
> 岗位截图/JD 分析 · 简历匹配诊断 · 定制简历 · 55 题左右八类面试题库 · 面试辅导计划 · 面试复盘 · 多岗位题库汇总 · 谈薪与试用期护航。

[![Release](https://img.shields.io/github/v/release/Asaceoo/offer-coach-puls)](https://github.com/Asaceoo/offer-coach-puls/releases)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

---

## 它解决什么问题

找工作最贵的成本不是投递，是**投错**：花三天准备的岗位，面试时才发现职责是坑、薪资低于底线、公司正在欠税。offer-coach 把"投递决策"变成一份可验证的报告——**在投之前**回答七个问题：这个岗位到底做什么、公司真正想招什么人、我匹配度如何、值不值得投、面试重点准备什么、有哪些风险要提前确认。

## 五阶段全景

![五阶段全景](docs/diagrams/flow.svg)

| 阶段 | 触发 | 产出 |
|---|---|---|
| ① 定位 | 首次使用，5 问一次答齐 | `positioning.md`（岗位第一道筛子）+ `story-cards.md`（故事卡弹药库） |
| ② 岗位分析 | 发岗位截图/JD | **六部分岗位报告 PDF**（51~60 题八类题库）+ 定制简历 |
| ③ 备战 | 收到面试通知 | D-3/D-1/D-0 备战计划 + 押题重点 + 可选自动提醒 |
| ④ 面试+复盘 | 面完口述情况 | 复盘卡（押题命中率/卡点/下一场第一个要改的动作）→ 反哺话术库与题库 |
| ⑤ 终局 | 收到 offer / 被拒 / 入职 | 谈薪准备（总包视角）/ 拒因三层归因 / 30-60-90 天试用期计划 |

跨阶段沉淀越用越厚：`master.md` 简历事实源、故事卡、playbook 话术库与顽固卡点、岗位池与投递漏斗。

## 报告长什么样

![报告六部分结构](docs/diagrams/report-structure.svg)

**铁律：一个 JD = 一份独立报告**，绝不把多个岗位混写进同一份报告；跨岗位统计只存在于岗位池索引与汇总导出。

## 四条红线（为什么它的输出可信）

1. **反虚构**——所有建议引用简历原文（`master.md` 锚点），缺数据标【待补】不代编
2. **无匹配百分比**——差距用"直接匹配/可迁移/关键缺口"三分法表达
3. **面试题给参考答案结构示范，不给背诵稿**——参考答案用你的真实素材装填，亲历细节由你核实替换
4. **不做自动投递**——只帮你准备，不碰招聘账号

## 数据契约

![数据契约](docs/diagrams/data-contract.svg)

技能层只读、工作区读写、**全部本地存储不上云**。

## 安装

```bash
# 方式一：下载 Release zip
# https://github.com/Asaceoo/offer-coach-puls/releases → 解压 offer-coach-vX.Y.Z.zip

# 方式二：源码
git clone https://github.com/Asaceoo/offer-coach-puls.git
cp -r offer-coach-puls/offer-coach ~/.workbuddy/skills/
```

放置到 `~/.workbuddy/skills/`（用户级）或工作区 `.workbuddy/skills/`（项目级），重启会话即可触发。触发词极宽：**找工作、看岗位、发来职位截图或 JD、简历匹配、改简历、面试准备、面试通知、面经、复盘面试、要 offer**——即使你没点名 offer-coach。

## 打包与发布

```bash
python scripts/package.py           # patch 递增（v1.5.2 → v1.5.3）并产出 dist zip
python scripts/package.py --minor   # minor 递增
python scripts/package.py --no-bump # 不递增重打包
```

脚本自动同步 `docs/用户手册.md` 与 `docs/技术手册.md` 首页版本行。

## 文档

- [用户手册](docs/用户手册.md)——怎么用、产出什么、每类题长什么样
- [技术手册](docs/技术手册.md)——架构、数据契约、设计决策、质量验证记录

## 质量验证

9 轮迭代记录：鲁班工具闭环（SkillOps/Sentinel/HASP/CASCADE/Distill 全绿）+ 三视角对抗审查（工具实现者/审查者/AI 使用方）+ 独立真机测试（中英文 JD、多岗位并行、全生命周期链路、虚构公司调研纪律、定位筛边界值）。详见[技术手册 §5](docs/技术手册.md)。

## License

MIT
