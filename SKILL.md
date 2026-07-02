---
name: ml-math
description: Assist with mathematical derivations in machine learning and artificial intelligence, especially when the user needs to understand formulas, verify reasoning, debug derivation steps, connect equations to code, or build small numerical and visual experiments. Use for ML/AI math involving probability, linear algebra, calculus, optimization, gradients, losses, KL/ELBO, attention, diffusion, flow models, ODE/SDE, information theory, kernels, and related formula reasoning.
---

# ML Math

## Core Rule

Treat every derivation as a claim that should be checked. Explain the math, but prefer executable verification whenever the claim can be tested with symbolic algebra, finite differences, numerical simulation, tensor-shape checks, or toy visualizations.

## Workflow

1. Restate the target formula or concept.
   - Identify what must be shown, what is given, and what assumptions are needed.
   - Preserve the user's notation when possible. Define any missing symbols before using them.

2. Build a derivation map.
   - Write the derivation as numbered steps.
   - Label each step by rule: algebra, chain rule, product rule, Bayes rule, change of variables, expectation identity, Jensen's inequality, matrix calculus, ODE/SDE relation, or approximation.
   - Mark any uncertain or convention-dependent step as a checkpoint, not as a fact.

3. Check dimensions and domains.
   - Track scalar/vector/matrix/tensor shapes for all important quantities.
   - Check probability distributions integrate or sum to one when relevant.
   - Check signs, transpose placement, log bases, constants, and boundary conditions.

4. Explain at two levels.
   - Give a plain-language explanation for the user's intuition.
   - Give the precise mathematical derivation separately. Do not mix intuition with proof.

5. Verify with code.
   - Use Python with `numpy`, `sympy`, or `torch` when available.
   - Prefer finite-difference gradient checks for derivatives.
   - Prefer random numerical tests for claimed equivalent formulas.
   - Prefer toy 1D/2D simulations for distribution transport, ODE/SDE, score fields, or optimization dynamics.
   - If code cannot be run, provide runnable code and clearly state that it was not executed.

6. Visualize when useful.
   - Use plots for scalar functions, loss landscapes, vector fields, density evolution, samples, trajectories, and attention matrices.
   - Keep visualizations toy-sized and diagnostic, not decorative.

7. Finish with a learning bridge.
   - List the minimal prerequisite concepts the user should review.
   - Suggest the next formula or experiment that would strengthen understanding.

## Output Shape

Use this structure for non-trivial tasks:

- **Goal**: the formula or claim being explained.
- **Notation**: symbols, dimensions, and assumptions.
- **Derivation**: numbered steps with rule labels.
- **Checks**: dimension/domain checks and fragile assumptions.
- **Code Verification**: executed code summary, key output, and file path if a script/notebook was created.
- **Visualization**: plot description or generated file path when applicable.
- **Intuition**: a short explanation in accessible language.
- **Review Next**: prerequisite concepts or next experiment.

For simple questions, keep the answer shorter but still include checks when the formula is easy to misuse.

## Verification Scripts

Use `scripts/math_check.py` for quick reusable checks:

```bash
python3 scripts/math_check.py --demo all
python3 scripts/math_check.py --demo gaussian-kl
python3 scripts/math_check.py --demo softmax-grad
python3 scripts/math_check.py --demo score-gaussian
```

Use `scripts/plot_toy_flow.py` when a 2D vector field, particle flow, or trajectory plot would help:

```bash
python3 scripts/plot_toy_flow.py --output /tmp/toy_flow.png
```

Read `references/math-checklist.md` when auditing a long derivation. Read `references/ml-math-roadmap.md` when the user asks what background is needed or how topics connect.

## Guardrails

- Do not present an unverified algebra jump as certain when it depends on a hidden assumption.
- Do not skip constants in losses or likelihoods unless the user only needs optimization-equivalent forms; say which constants were dropped.
- Do not claim two objectives are equivalent unless they have the same optimizer or differ by a constant/positive scaling under stated assumptions.
- Do not ignore tensor broadcasting; explicitly check whether the code implementation matches the math.
- When explaining papers, separate the paper's stated formula from reconstructed derivation.
