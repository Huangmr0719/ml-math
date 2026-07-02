#!/usr/bin/env python3
"""Reusable zero-dependency numerical checks for ML math derivations."""

import argparse
import math
import random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def mat_vec(matrix, vector):
    return [dot(row, vector) for row in matrix]


def vec_sub(a, b):
    return [x - y for x, y in zip(a, b)]


def finite_difference_grad(f, x, eps=1e-6):
    grad = []
    for i in range(len(x)):
        xp = list(x)
        xm = list(x)
        xp[i] += eps
        xm[i] -= eps
        grad.append((f(xp) - f(xm)) / (2 * eps))
    return grad


def inverse_2x2(matrix):
    (a, b), (c, d) = matrix
    det = a * d - b * c
    return [[d / det, -b / det], [-c / det, a / det]]


def cholesky_2x2(matrix):
    a = math.sqrt(matrix[0][0])
    b = matrix[1][0] / a
    c = math.sqrt(matrix[1][1] - b * b)
    return [[a, 0.0], [b, c]]


def normal_pair(rng):
    u1 = max(rng.random(), 1e-12)
    u2 = rng.random()
    radius = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2
    return radius * math.cos(theta), radius * math.sin(theta)


def demo_gaussian_kl():
    rng = random.Random(7)
    mu = [rng.gauss(0.0, 1.0) for _ in range(4)]
    logvar = [rng.gauss(0.0, 0.2) for _ in range(4)]
    var = [math.exp(v) for v in logvar]

    analytic = 0.5 * sum(v + m * m - 1.0 - lv for m, v, lv in zip(mu, var, logvar))

    total = 0.0
    n = 120_000
    for _ in range(n):
        z = [rng.gauss(m, math.sqrt(v)) for m, v in zip(mu, var)]
        log_q = -0.5 * sum(math.log(2 * math.pi) + lv + ((zi - m) ** 2) / v for zi, m, v, lv in zip(z, mu, var, logvar))
        log_p = -0.5 * sum(math.log(2 * math.pi) + zi * zi for zi in z)
        total += log_q - log_p
    estimate = total / n

    print("Gaussian KL q=N(mu,var) || p=N(0,I)")
    print(f"analytic={analytic:.6f}")
    print(f"monte_carlo={estimate:.6f}")
    print(f"abs_error={abs(analytic - estimate):.6f}")


def demo_softmax_grad():
    rng = random.Random(3)
    logits = [rng.gauss(0.0, 1.0) for _ in range(5)]
    target = 2

    def loss(x):
        shift = max(x)
        exp_values = [math.exp(v - shift) for v in x]
        log_sum_exp = shift + math.log(sum(exp_values))
        return -(x[target] - log_sum_exp)

    shift = max(logits)
    exp_values = [math.exp(v - shift) for v in logits]
    probs = [v / sum(exp_values) for v in exp_values]
    analytic = list(probs)
    analytic[target] -= 1.0
    numeric = finite_difference_grad(loss, logits)

    print("Softmax cross-entropy gradient")
    print(f"analytic={[round(v, 6) for v in analytic]}")
    print(f"numeric ={[round(v, 6) for v in numeric]}")
    print(f"max_abs_error={max(abs(a - n) for a, n in zip(analytic, numeric)):.6e}")


def demo_score_gaussian():
    rng = random.Random(11)
    mu = [1.0, -0.5]
    sigma = [[1.4, 0.2], [0.2, 0.7]]
    inv_sigma = inverse_2x2(sigma)
    x = [rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)]

    def log_density(v):
        delta = vec_sub(v, mu)
        return -0.5 * dot(delta, mat_vec(inv_sigma, delta))

    analytic = [-v for v in mat_vec(inv_sigma, vec_sub(x, mu))]
    numeric = finite_difference_grad(log_density, x)

    print("Gaussian score grad_x log p(x)")
    print(f"x={[round(v, 6) for v in x]}")
    print(f"analytic={[round(v, 6) for v in analytic]}")
    print(f"numeric ={[round(v, 6) for v in numeric]}")
    print(f"max_abs_error={max(abs(a - n) for a, n in zip(analytic, numeric)):.6e}")


DEMOS = {
    "gaussian-kl": demo_gaussian_kl,
    "softmax-grad": demo_softmax_grad,
    "score-gaussian": demo_score_gaussian,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", choices=[*DEMOS.keys(), "all"], default="all")
    args = parser.parse_args()

    names = DEMOS.keys() if args.demo == "all" else [args.demo]
    for name in names:
        DEMOS[name]()
        print()


if __name__ == "__main__":
    main()
