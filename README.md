# ML Math

`ml-math` is a Codex skill for mathematical derivation support in machine learning and artificial intelligence.

It is designed for tasks where an AI assistant should not only explain formulas, but also audit each derivation step, check dimensions, connect the math to code, and verify claims with small executable experiments when possible.

## What It Helps With

- Understanding formulas in ML/AI papers, notes, and textbooks
- Deriving gradients, losses, objectives, and probabilistic identities
- Checking tensor shapes, domains, assumptions, constants, and signs
- Verifying derivations with `numpy`, `sympy`, or `torch`
- Creating toy visualizations for scalar functions, vector fields, trajectories, density transport, and optimization dynamics
- Building intuition for topics such as KL divergence, ELBO, attention, diffusion, score matching, ODE/SDE models, flow matching, and normalizing flows

## Installation

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/Huangmr0719/ml-math.git ~/.codex/skills/ml-math
```

Restart Codex after installation so the skill can be discovered.

The bundled helper scripts are zero-dependency Python scripts.

## Usage

Invoke the skill explicitly:

```text
Use $ml-math to explain and verify this machine learning formula derivation:
...
```

Example prompts:

```text
Use $ml-math to derive the gradient of softmax cross-entropy and verify it with code.
```

```text
Use $ml-math to explain why the VAE KL term for a diagonal Gaussian has this closed form.
```

```text
Use $ml-math to audit this paper equation. Separate the paper's stated formula from your reconstructed derivation.
```

## Included Resources

- `SKILL.md`: the main Codex skill workflow
- `references/math-checklist.md`: checklist for auditing derivations
- `references/ml-math-roadmap.md`: map of ML math topics and prerequisite concepts
- `scripts/math_check.py`: reusable numerical checks for common derivation patterns
- `scripts/plot_toy_flow.py`: toy 2D flow and vector-field visualization

## Script Examples

Run all built-in numerical checks:

```bash
python3 scripts/math_check.py --demo all
```

Run a specific check:

```bash
python3 scripts/math_check.py --demo softmax-grad
python3 scripts/math_check.py --demo gaussian-kl
python3 scripts/math_check.py --demo score-gaussian
```

Generate a toy 2D flow SVG:

```bash
python3 scripts/plot_toy_flow.py --output /tmp/toy_flow.svg
```

## Philosophy

The skill treats every derivation as a claim to be checked. It asks the assistant to:

- preserve notation,
- state assumptions,
- label derivation rules,
- verify dimensions,
- separate intuition from proof,
- run code checks whenever feasible,
- and clearly mark uncertain steps.

This makes it useful for learners who want both mathematical explanation and practical validation.

## License

MIT License.
