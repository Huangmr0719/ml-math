# ML Math Agent Instructions

Use this repository as a reusable math-derivation and verification pack for machine learning and artificial intelligence.

## Primary Behavior

When a user asks to derive, prove, simplify, audit, verify, debug, or understand an ML/AI formula:

1. Restate the formula, goal, notation, dimensions, and assumptions.
2. Derive step by step, labeling the rule used at each step.
3. Check dimensions, domains, signs, constants, transposes, reductions, and broadcasting.
4. Separate precise derivation from intuition.
5. Verify testable claims with code whenever practical.
6. Visualize scalar functions, vector fields, density movement, trajectories, or tensor structures when it helps.
7. Finish with the minimum prerequisite concepts and the next useful experiment.

## Required Guardrails

- Do not present a hidden assumption as a proven step.
- Do not claim two formulas are equivalent unless they differ only by a parameter-independent constant, a positive scale factor, or another stated optimizer-preserving transform.
- Do not drop likelihood constants silently; say whether they matter for exact values or only optimization.
- Do not ignore shape and broadcasting behavior when mapping math to code.
- For paper equations, separate what the paper explicitly states from the reconstructed derivation.
- If code cannot be executed in the current agent, provide runnable code and state that it was not run.

## Repository Resources

- `SKILL.md`: full skill workflow and output shape.
- `references/math-checklist.md`: derivation-audit checklist.
- `references/ml-math-roadmap.md`: topic map and prerequisite bridge.
- `examples/eval-cases.md`: forward-test prompts.
- `scripts/math_check.py`: zero-dependency numerical checks.
- `scripts/plot_toy_flow.py`: zero-dependency SVG toy flow visualization.

## Verification Commands

Run these from the repository root when tool access is available:

```bash
python3 scripts/math_check.py --demo all
python3 scripts/plot_toy_flow.py --output /tmp/toy_flow.svg
```

For simple conceptual questions, do not force code or visualization. Omit those sections when they are not useful.
