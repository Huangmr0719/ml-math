# Agent Installation

`ml-math` is intended to work as a portable instruction pack, not only as a Codex skill.

## Codex

Install as a Codex skill:

```bash
git clone https://github.com/Huangmr0719/ml-math.git ~/.codex/skills/ml-math
```

Restart Codex after installation.

## Claude Code

Install as a Claude Code skill:

```bash
git clone https://github.com/Huangmr0719/ml-math.git ~/.claude/skills/ml-math
```

Project-local skill installation:

```bash
git clone https://github.com/Huangmr0719/ml-math.git .claude/skills/ml-math
```

For project-level instructions, copy or commit `AGENTS.md` and `CLAUDE.md` into a project. `CLAUDE.md` imports `AGENTS.md` so Claude Code and other agents can share the same core instructions without duplicating content.

## OpenCode

Install as a global OpenCode skill:

```bash
git clone https://github.com/Huangmr0719/ml-math.git ~/.config/opencode/skills/ml-math
```

Alternative OpenCode-compatible global location:

```bash
git clone https://github.com/Huangmr0719/ml-math.git ~/.agents/skills/ml-math
```

Project-local skill installation:

```bash
git clone https://github.com/Huangmr0719/ml-math.git .opencode/skills/ml-math
```

Alternative project-local agent-compatible location:

```bash
git clone https://github.com/Huangmr0719/ml-math.git .agents/skills/ml-math
```

For project-level rules without installing a skill, copy or commit `AGENTS.md` into the project root.

For a project-local OpenCode subagent, copy:

```bash
.opencode/agents/ml-math.md
```

Then invoke it in OpenCode with:

```text
@ml-math derive the softmax cross-entropy gradient and verify it numerically
```

## Generic Agents

For agents that do not have a native skill system:

1. Use `AGENTS.md` as the compact shared instruction file.
2. Use `SKILL.md` as the full workflow.
3. Use `references/math-checklist.md` for long derivation audits.
4. Run scripts manually when the agent can execute shell commands.

Example prompt:

```text
Use the instructions in AGENTS.md and SKILL.md to derive this ML formula. Verify any testable claim with code.
```
