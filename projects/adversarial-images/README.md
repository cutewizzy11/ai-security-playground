# Project: Adversarial Images

An intermediate-to-advanced project exploring adversarial examples against image classifiers.

## Idea

Train or load a simple image classifier (e.g., on MNIST or a similar small dataset), then:
- Generate adversarial images using attacks like FGSM or PGD.
- Visualize original vs adversarial images.
- Measure how accuracy drops under attack.

## Suggested structure

- `src/` – Python modules for:
  - Loading data and models.
  - Implementing attacks.
  - Evaluation helpers.
- `notebooks/` – Interactive experiments and visualizations.

## Contributions

- Implement a basic attack (e.g., FGSM) in `src/` and show it in a notebook.
- Add different norms/constraints (L2, Linf) and compare.
- Explore simple defenses (e.g., adversarial training on a small dataset).

Keep the code readable and well-explained so others can follow the ideas.
