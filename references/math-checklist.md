# Math Derivation Checklist

Use this checklist before trusting a machine learning derivation.

## Notation

- Define every symbol before using it.
- Identify scalars, vectors, matrices, tensors, functions, distributions, and random variables.
- Track whether vectors are columns or rows.
- State whether gradients are numerator-layout or denominator-layout if matrix calculus is involved.

## Algebra And Calculus

- Check signs after moving terms across an equality.
- Check constants that disappear from proportional relationships.
- Check transpose placement in quadratic forms and Jacobians.
- For derivatives, verify with finite differences when possible.
- For gradients through expectations, state why differentiation and integration can be exchanged.

## Probability

- Check support of all distributions.
- Check normalization constants when likelihood values matter.
- Distinguish samples, random variables, and realized values.
- For KL, state direction: `KL(p || q)` is not `KL(q || p)`.
- For expectations, state which distribution the expectation is over.

## Optimization

- Distinguish equivalent objectives from objectives with the same optimizer.
- Check whether constants are independent of parameters.
- Check whether a loss is minimized or maximized.
- Verify gradients numerically for small random inputs.

## Geometry And Dynamics

- For change of variables, include the determinant term and absolute value.
- For flows, check initial and terminal distributions or endpoints.
- For ODE/SDE formulas, state time direction, boundary conditions, and drift/noise conventions.
- For vector fields, visualize a 1D or 2D toy case when possible.

## Implementation

- Match mathematical dimensions to code tensor shapes.
- Check broadcasting explicitly.
- Check batch dimensions and reduction axes.
- Compare analytic formulas against numerical results on small random examples.
- Use deterministic seeds for reproducible checks.
