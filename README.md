# 空间锁＋摄影机轴线锁

`scene-spatial-lock` v0.1.1。公开试用版，保留既有方法与功能边界。

## 用途与输入

提供场景图及明确设定；本地编译需要Python 3。编译器校验结构和依赖，不能替代看图，也不自带视频模型。人物未提供不等于无人；反向机位需要背面依据。

## 安装

```sh
npx skills add Lonc2100/scene-spatial-lock --skill scene-spatial-lock
```

也可在 Releases 下载同版本ZIP，解压后将整个`scene-spatial-lock`目录放入客户端实际支持的Skill目录。安装后确认客户端识别该名称，再提供自己的输入；复制成功不等于已完成实际调用。

## 前置条件

- [ ] 客户端支持读取本地SKILL.md和相对引用文件。
- [ ] 提供自己有权使用的参考图及明确设定。
- [ ] 若执行脚本或生图，已具备相应运行环境及授权。

## 你可以直接这样说

> 请使用 scene-spatial-lock，查看我提供的全景图与正反面设定，输出空间锁和摄影机轴线锁两段正文。未知区域不要补造。

## 验证与边界

包内测试可运行`python -m unittest discover -s tests`。开发者如使用技能工厂，可用其`validate_skill.py <本目录>`做结构检查；该工厂不是本包运行依赖。触发报告仅为关键词边界冒烟检查，不代表模型真实选择能力。

## Troubleshooting

未识别Skill时，检查目录中是否直接含SKILL.md，并重新加载客户端；不能运行脚本时先检查Python及依赖。生图结果漂移时比较同一部位，保留原图并拒绝不合格候选，不用更锐代替身份验收。

## 许可证

MIT，见[LICENSE](LICENSE)。包内不含原片、私人图片、密钥、字体文件或模型权重；输入素材权利由使用者自行确认。

## 原有详细说明

# scene-spatial-lock 0.1.1

个人试行Skill，按作者最新范例产出两段提示词，而非环境美术合同。主模型先审图片、核来源，脚本负责检查结构和编译；不宣称脚本具有视觉理解。

输入scene.json：reference_image绝对路径，time_place文字，anchors数组（id/name/relation/evidence），axis_lock文字，unknown_regions字符串数组，shots数组（id/camera/prompt）。可选route/light/state_locks/author_source。

0.1.1修正：省略route不再变成“无人”；不再把同侧机位当通用限制。可选axis_mode为declared_in_text/same_side/reverse_views。reverse_views须提供view_references至少两张现有图片，或明确back_view_basis作者设定。visual_review仅记录真实传入的审读状态；不传时保持未提供，不自动声明主模型看过图。

- 设计优势：原图可见事实、作者设定、命名约定与未知分开；先检查是否有权定义画外。
- 已验证范围：本期书房的提示词结构及来源核对；文本审核不能证明生成视频保持空间。
- 待验证：跨模型/多机位视频控制效果；不能从一次静态图推断80%成功率。

已查看environment-look-lock本机入口，并对照作者原图。另读Scene Spatial Anchor Skill公开一手示例（2026-11-04）：https://gist.github.com/fantasytubasa/63c04d1a5a35e1b0d1aaada278875b38 ，借鉴固定场景坐标与锚点机制；不复制原代码/全文、不机械套H3专用规则。该材料不是作者给定原文的替代品。

缺失证据：未做全网Skill评级/目录安装量审计，无跨宿主自动加载保证。不发布，不新增付费调用。

适配目标只表示SKILL.md格式面向这些客户端，不代表所有客户端已实际运行通过。
