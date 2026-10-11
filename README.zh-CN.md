<p align="center" dir="ltr">
  <a href="README.sv.md" lang="sv">Svenska</a> · <strong>简体中文</strong> · <a href="README.de.md" lang="de">Deutsch</a> · <a href="README.ar.md" lang="ar" dir="rtl">العربية</a> · <a href="README.ru.md" lang="ru">Русский</a> · <a href="README.th.md" lang="th">ไทย</a> · <a href="README.tr.md" lang="tr">Türkçe</a> · <a href="README.md" lang="en">English</a>
</p>

# tibtre-ledger

**tibtre** 是 YuriPlanet 合作社的贡献货币，这里是它的大本营。本仓库存放着相关政策、只追加不修改的账本、自动生成的余额，以及让系统中每一个数字都能被独立核验的工具。

## 为什么要有 tibtre

Yrvera 由贡献者共同打造，我们最初的理念是：它应当*属于*这些贡献者。在这件事真正变得重要之前，tibtre 就让这一理念落到了实处：

- **公平先行。** 如果 Yrvera 将来成立法律实体，或有收入需要分配，那个难题——*这是谁做的，各做了多少？*——早已有了答案：从第一天起就公开、可核验。本账本就是任何此类分配的既定依据。
- **现在就有真正的话语权。** 关于 Yrvera 发展方向的决策按 tibtre 加权，但设有上限，任何单个持有者都无法一家独大（[`voteweight.py`](voteweight.py)）。
- **永久的记录。** 贡献按公开规则估值（[评分标准](docs/grading-rubric.md)），被永久记录，任何人都能核验——包括贡献者本人，而且无需信任任何人（[`identity.py`](identity.py)）。

1 tibtre ≈ 为 Yrvera 真正需要的事情做一小时高质量的工作。质量和价值都算数，两者都按公开规则定价。无需申请：做出贡献，获得估值，记录在案。

## 文件一览

| 文件 / 文件夹 | 说明 |
|---|---|
| `RULES.md` | 政策：tibtre 是什么、如何获得、价值几何 |
| `LEDGER.csv` | 只追加不修改的发放账本，以贡献者 ID 为键——唯一的事实来源 |
| `CONTRIBUTORS.csv` | ID → 公开显示名（可选，可修改；留空 = 匿名，只显示 ID） |
| `BALANCES.md` | 自动生成的余额表——编辑账本后运行 `python tally.py` |
| `tally.py` | 根据 `LEDGER.csv` 重新生成 `BALANCES.md` |
| `voteweight.py` | 按每人 25% 的上限计算投票中实际计入的权重（`--demo` 查看示例） |
| `identity.py` | 生成和核验公开的身份承诺——无需信任任何人，就能证明某个 ID 属于你 |
| `docs/granting-guide.md` | 供审批人记录发放的分步指南 |
| `assets/` | 已采纳的社区美术作品及其他非代码成果的存档 |

## 约定

- 账本**只追加不修改**：绝不编辑或删除过去的行。更正时新增一行（允许负数金额，并附上说明原因的备注）。
- 账本**只包含贡献者 ID**（随机生成，如 `T-83DE`），从不包含姓名。显示名保存在 `CONTRIBUTORS.csv` 中，可随时修改或清空，不会影响历史记录。
- ID 与真实身份的对应关系保存在**单独的私有文件夹**（`../vera20k-tibtre-private/`）中，绝不能公开。
- 每次修改都会提交到 git——提交历史*就是*审计记录。
- 今后所有与 tibtre 相关的文档都放在 `docs/` 中。
- 已采纳的美术作品放在 `assets/` 中，命名为 `YYYY-MM-DD_T-XXXX_short-title.ext`（用 ID，绝不用姓名——文件名是公开且永久的）。

本文件译自 [README.md](README.md)；如有出入，以英文版为准。
