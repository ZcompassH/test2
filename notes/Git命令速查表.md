# Git 命令速查表

> 整理日期：2026-11-18
> 排序原则：**按使用频率从高到低**。第 1 档背下来，第 3 档存着救命，第 5 档知道有这回事就行。

---

## 0. 先记住这张图

```
工作区（你在编辑的文件）
    │  git add
    ▼
暂存区（下次提交的快照）
    │  git commit
    ▼
本地仓库（版本库，历史记录）
    │  git push
    ▼
远程仓库（GitHub / Gitee）
```

**所有命令都在回答一个问题：我在把东西从哪挪到哪。**

| 现象 | 原因 |
|---|---|
| 提交上去的是旧版 | 改了文件但**没再 `git add`**，commit 只拿暂存区 |
| 同一个文件在两个列表出现 | `add` 之后又改了它 |
| 推送推不上去 | 走网络，看第 4 档 |

---

## 1. 每天必用（6 条）

| 命令 | 作用 | 什么时候敲 | 坑 |
|---|---|---|---|
| `git status` | 现在是什么状态 | **每次动手前先敲** | `git status -s` 是精简版 |
| `git add <文件>` | 把文件放进暂存区 | 改完、提交前 | `git add .` 加全部（注意别把垃圾也加进去） |
| `git commit -m "说明"` | 把暂存区存成一次历史 | 一个完整的小改动做完 | **只提交暂存区**，没 add 的不会进 |
| `git push` | 推到远程 | 提交完 | 只这一步走网络 |
| `git pull` | 拉远程最新并合并 | 推送前、每天开工前 | 有冲突要先解决 |
| `git log --oneline -5` | 最近 5 次提交 | 确认提交成功没 | 按 `q` 退出 |

### 最常用的完整流程（背下来）

```powershell
git status
git add .
git commit -m "feat: 完成 python-basics-8 八道题"
git push
```

---

## 2. 看差异、后悔药（很常用）

| 命令 | 作用 | 坑 |
|---|---|---|
| `git diff` | 工作区 vs 暂存区：**还没 add 的改动** | |
| `git diff --staged` | 暂存区 vs 上次提交：**即将提交的内容** | 老写法 `--cached` |
| `git diff HEAD` | 工作区 vs 最后一次提交：**所有未提交改动** | |
| `git restore <文件>` | 丢弃工作区改动，恢复成暂存区版本 | ⚠️ **改动永久丢失**，不进回收站 |
| `git restore --staged <文件>` | 从暂存区撤回，**改动保留**在工作区 | 老写法 `git reset HEAD <文件>` |
| `git show <commit>` | 看某次提交改了什么 | |
| `git log --oneline --graph --all` | 看分支图 | |

> **方向别搞反**：`git add` 是"新的覆盖旧的"（把工作区推进暂存区）；`git restore` 是"旧的覆盖新的"（把暂存区/历史拉回工作区）。

---

## 3. 建仓库、接仓库、分支

| 命令 | 作用 | 什么时候用 |
|---|---|---|
| `git init` | 在文件夹里建一个新仓库 | 从零开始 |
| `git clone <url>` | 把远程仓库整个下载下来 | 接别人的项目 / 换电脑 |
| `git remote add origin <url>` | 给本地仓库绑一个远程地址 | 本地建好了要推上去 |
| `git remote -v` | 看当前绑的地址 | 推不上去时先看这个 |
| `git push -u origin main` | 首次推送并记住上游 | 第一次推某个分支 |
| `git branch` | 看所有本地分支 | |
| `git switch -c 新分支` | 新建并切过去 | 想做实验又怕搞坏主线 |
| `git switch main` | 切回 main | |
| `git merge 分支名` | 把某个分支合并进来 | 实验成功、要合回主线 |
| `git branch -d 分支名` | 删掉已合并的分支 | |
| `git stash` | 把没提交的改动"暂存起来"，工作区变干净 | 临时要切分支、又不想提交半成品 |
| `git stash pop` | 把暂存的改动拿回来 | |

---

## 4. 出问题救命（记住有这些）

| 命令 | 作用 | 坑 |
|---|---|---|
| `git reset --soft HEAD~1` | 撤销最后一次 **commit**，改动留在暂存区 | 安全，只是拆掉提交 |
| `git reset HEAD~1` | 撤销 commit，改动退回工作区（默认 mixed） | 安全 |
| `git reset --hard HEAD~1` | 撤销 commit **并删掉改动** | ⚠️ **危险**，改动没了 |
| `git reflog` | **后悔药**：看到 HEAD 走过的每一步 | 上面 `--hard` 删错了，用它找回 commit |
| `git commit --amend -m "新说明"` | 改最后一次提交的说明 / 补文件 | 只改**还没 push** 的提交 |
| `git rm --cached <文件>` | 不再跟踪，但**文件保留在磁盘** | 配合 `.gitignore` 用 |
| `git fetch` | 只下载远程更新，**不合并** | 想先看看有什么变化时用 |
| `git blame <文件>` | 每一行是谁、哪次改的 | 多人协作时用 |
| `git config --global user.name "名字"` | 设置提交者名字 | 只做一次 |
| `git config --global user.email "邮箱"` | 设置提交者邮箱 | 只做一次 |

### 卡住了先查这三个

```powershell
# ① 有没有残留的锁文件（会让所有 git 操作静默卡住）
ls .git\index.lock        # 有就删：del .git\index.lock（确认没有 git 进程在跑）

# ② 凭据有没有配好
git config --global credential.helper manager

# ③ 网络问题（只影响 push/pull/fetch）
git config --global http.proxy http://127.0.0.1:7890    # 有代理时
git config --global --unset http.proxy                  # 用完关掉
```

---

## 5. 知道就行（现在用不到）

| 命令 | 干什么的 |
|---|---|
| `git tag v1.0.0` | 给某次提交打版本标签 |
| `git rebase` | 把提交历史"搬"到另一个基础上（改写历史，团队慎用） |
| `git cherry-pick <commit>` | 把某一次提交单独摘到当前分支 |
| `git bisect` | 二分查找哪次提交引入了 bug |
| `git submodule` | 在一个仓库里嵌另一个仓库 |
| `git add -p` | 一个文件里的改动，挑着加 |

---

## 6. 提交说明怎么写

格式：**类型: 一句话说清做了什么**

| 前缀 | 用于 |
|---|---|
| `feat:` | 新功能 |
| `fix:` | 修 bug |
| `docs:` | 只改文档 |
| `refactor:` | 重构，行为不变 |
| `chore:` | 杂事（配置、依赖） |
| `test:` | 加测试 |

好的：
- `feat: 完成 python-basics-8 八道题`
- `fix: 修正词频统计没处理大写字母`
- `docs: 补充第 3 周 CSV 清洗说明`

坏的：
- `更新` / `改了一下` / `111` / `asdf`

**判断标准**：三个月后你自己看 `git log`，能不能想起这次改了什么。

---

## 7. 今天这个场景，完整走一遍

```powershell
git status                      # 看到 Q1.py 同时在两个列表里
git add exercises/day15/Q1.py   # 把最新版放进暂存区（覆盖旧的）
git status                      # 确认它只出现在 "Changes to be committed"
git diff --staged               # 再确认一下要提交的内容对不对
git commit -m "fix: 修正 Q1 的实现"
git log --oneline -3            # 确认提交成功
git push                        # 推到远程
```

---

## 8. .gitignore 必写内容

```
.venv/
__pycache__/
*.pyc
.vscode/
```

建完仓库第一件事就是写它——**已经提交过的文件，加进 .gitignore 不管用**，得先 `git rm --cached` 再提交一次。
