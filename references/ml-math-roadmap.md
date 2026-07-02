# ML Math Roadmap

Use this as a navigation map, not as a textbook.

## Foundations

- Linear algebra: vectors, matrices, eigendecomposition, SVD, quadratic forms, norms.
- Calculus: chain rule, gradients, Jacobians, Hessians, Taylor expansion.
- Probability: random variables, density, expectation, variance, conditional probability, Bayes rule.
- Optimization: gradient descent, convexity, Lagrange multipliers, stochastic gradients.

## Core ML Formulas

- Linear/logistic regression: likelihood, cross entropy, gradients.
- Neural networks: backpropagation, activation derivatives, initialization scale.
- Regularization: L2, weight decay, priors, MAP estimation.
- Information theory: entropy, cross entropy, KL divergence, mutual information.

## Representation And Generative Models

- Autoencoders: reconstruction loss, latent representation, bottleneck.
- VAEs: ELBO, reparameterization trick, Gaussian KL, amortized inference.
- Normalizing flows: change of variables, log determinant Jacobian, invertibility.
- Diffusion/score models: forward noising, score function, denoising score matching, probability flow ODE.
- Flow matching: interpolation path, velocity field, continuity equation, transport view.

## Attention And Sequence Models

- Softmax: normalization, temperature, Jacobian, numerical stability.
- Attention: query/key/value dimensions, scaled dot product, mask broadcasting.
- Transformers: residual paths, layer norm, MLP blocks, positional encodings.

## Verification Habits

- For every derivative, run a finite-difference check.
- For every claimed identity, test random numeric inputs.
- For every distribution formula, check normalization or sample behavior.
- For every dynamic process, plot a toy trajectory or vector field.
