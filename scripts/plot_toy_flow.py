#!/usr/bin/env python3
"""Create a zero-dependency SVG of a small 2D vector field and particle flow."""

import argparse
import math
import random


def velocity(point):
    x, y = point
    return (-0.7 * x - 0.6 * y, 0.6 * x - 0.7 * y)


def project(point, size, scale):
    x, y = point
    return size / 2 + x * scale, size / 2 - y * scale


def svg_line(x1, y1, x2, y2, color, width=1.0, opacity=1.0):
    return (
        f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
        f'stroke="{color}" stroke-width="{width}" opacity="{opacity}" '
        'stroke-linecap="round" />'
    )


def svg_circle(x, y, r, color, opacity=1.0):
    return f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{color}" opacity="{opacity}" />'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--steps", type=int, default=80)
    parser.add_argument("--dt", type=float, default=0.04)
    args = parser.parse_args()

    size = 720
    scale = 115
    elements = [
        f'<rect width="{size}" height="{size}" fill="#ffffff" />',
        f'<text x="24" y="36" font-size="24" font-family="Arial" fill="#111827">Toy 2D Flow</text>',
    ]

    grid = [round(-2.4 + i * 0.4, 2) for i in range(13)]
    for x in grid:
        for y in grid:
            vx, vy = velocity((x, y))
            norm = math.sqrt(vx * vx + vy * vy) or 1.0
            length = 0.16
            start = project((x, y), size, scale)
            end = project((x + length * vx / norm, y + length * vy / norm), size, scale)
            elements.append(svg_line(*start, *end, "#6b7280", width=1.2, opacity=0.45))

    rng = random.Random(5)
    particles = [(rng.gauss(1.6, 0.25), rng.gauss(0.8, 0.25)) for _ in range(40)]
    traces = [[p] for p in particles]
    for _ in range(args.steps):
        next_particles = []
        for point in particles:
            vx, vy = velocity(point)
            nxt = (point[0] + args.dt * vx, point[1] + args.dt * vy)
            next_particles.append(nxt)
        particles = next_particles
        for trace, point in zip(traces, particles):
            trace.append(point)

    for trace in traces:
        coords = [project(point, size, scale) for point in trace]
        path = " ".join(f"{x:.2f},{y:.2f}" for x, y in coords)
        elements.append(
            f'<polyline points="{path}" fill="none" stroke="#2563eb" '
            'stroke-width="1.2" opacity="0.35" />'
        )

    for trace in traces:
        sx, sy = project(trace[0], size, scale)
        ex, ey = project(trace[-1], size, scale)
        elements.append(svg_circle(sx, sy, 3, "#dc2626", opacity=0.75))
        elements.append(svg_circle(ex, ey, 3, "#16a34a", opacity=0.75))

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 {size} {size}">\n'
        + "\n".join(elements)
        + "\n</svg>\n"
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg)
    print(args.output)


if __name__ == "__main__":
    main()
