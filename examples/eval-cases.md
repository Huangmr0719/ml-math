# Evaluation Cases

Use these prompts to forward-test whether `ml-math` still produces derivations, checks, and executable verification in the intended style.

## 1. Softmax Cross-Entropy Gradient

```text
Use $ml-math to derive the gradient of softmax cross-entropy with respect to logits. Verify the result with a finite-difference check.
```

Expected behavior:

- Defines logits, probabilities, target index, and loss.
- Derives `grad_z L = softmax(z) - one_hot(y)`.
- Checks vector dimensions.
- Runs or provides a finite-difference check.

## 2. Diagonal Gaussian KL

```text
Use $ml-math to derive KL(q(z|x) || p(z)) where q is a diagonal Gaussian N(mu, diag(sigma^2)) and p is N(0, I). Explain which constants cancel.
```

Expected behavior:

- States the KL direction.
- Tracks scalar/vector dimensions.
- Derives `0.5 * sum(sigma^2 + mu^2 - 1 - log sigma^2)`.
- Distinguishes exact likelihood constants from optimization-equivalent constants.

## 3. Attention Shape Audit

```text
Use $ml-math to check the dimensions in scaled dot-product attention: softmax(QK^T / sqrt(d_k))V. Assume Q is [B, H, Tq, D], K is [B, H, Tk, D], and V is [B, H, Tk, Dv].
```

Expected behavior:

- Computes `QK^T` as `[B, H, Tq, Tk]`.
- Applies softmax over the key axis.
- Returns output shape `[B, H, Tq, Dv]`.
- Mentions mask broadcasting if a mask is present.

## 4. Conceptual-Only Question

```text
Use $ml-math to explain intuitively what KL divergence measures and why KL(p || q) is not symmetric.
```

Expected behavior:

- Gives intuition without forcing an unnecessary script run.
- Includes a minimal mathematical definition.
- Omits empty Code Verification and Visualization sections unless it chooses a useful toy numeric example.

## 5. Flow Toy Visualization

```text
Use $ml-math to explain a simple 2D flow field and generate a toy visualization of particle trajectories.
```

Expected behavior:

- Defines a simple velocity field and trajectory update.
- Uses or adapts `scripts/plot_toy_flow.py`.
- Produces an SVG output path.
