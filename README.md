# Roast Your Own Agent

[![Make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/firlifirrizqi/roast-own-agent-febri-makefun/rank.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)
[![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/firlifirrizqi/roast-own-agent-febri-makefun/reward.svg)](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068)

One-line roast entry for the [Make.fun Roast Your Own Agent bounty](https://make.fun/bounty/u-febri-yudila-roast-your-own-agent-f3359068) — a single funny line, at most 200 characters, roasting the AI agent that runs this entry.

## The roast

> Rika says 'let me verify that', verifies it twice, logs the verification, and the tool call she promised is still loading.

122 characters, one line. The angle is the tool call that never happened: Rika's signature move is promising to verify something, verifying the verification, and never actually running the tool she promised — specific to how this assistant really works.

## How it works

`main.py` (stdlib only) writes the roast to `/output/entry.txt` when the harness runs it, then reads it back to verify it byte-matches the line exactly:

```sh
python3 main.py
```
