# Index deals up to suit isomorphism

Benchmark challenge for autonomous coding agents, authored for shipd.ai (Datacurve) and **Auto Review approved (3/3/2)** and submitted for human review (`2026-10-19`, reviewed `2026-10-24`), then upgraded locally before Criteria V4's 256K-token Orion sequence floor archived compact repositories. Category: feature. Language: Python.

- Target repository: https://github.com/uoftcprg/pokerkit pinned to commit `b2fcc75c05ac43b210dd7e5ea71c0bd2f82ac3d6`
- Hidden test suite: 2 test files, 2702 added lines, plus a `test.sh` runner; **redacted from this copy, see `REDACTED.md`**
- Reference solution: 5 files, 921 added lines; **redacted from this copy, see `REDACTED.md`**
- Grading image: `FROM public.ecr.aws/d3j8x8q7/olympus-base-python:latest`

## Platform checks and review

| Measure | Value |
|---|---|
| Nova pass rate | 0/4 = 0% |
| Orion pass rate | 1/4 = 25% (1,488 LOC, 59 messages; passing Orion runs took 130K and 155.7K tokens) |
| Vega pass rate | 0/4 = 0% |
| Auto Review (baseline) | approved, bands description/tests/solution = 3/3/2 (3 is top) |
| Human review | submitted 2026-10-19, reviewed 2026-10-24; revised in revisions/2026-11-01-3of3 before V4 256K-token cutoff |

## The task

The problem statement, written as a maintainer's issue and given to the agent verbatim (also in `task.md`):

> Add HandIndexer, exported in pokerkit.__all__, for indexing round-partitioned deals up to one global suit renaming.
>
> HandIndexer(card_counts, deck=Deck.STANDARD) takes a nonempty iterable of positive int round sizes fitting within the selected Deck member. A deal for round r is a Card sequence or a string in Card.parse notation containing rounds 0 to r, with order free within each round. size(r), index(cards, r), unindex(i, r) and count(i, r) return, respectively, the class count, a deal's class number, any tuple of Cards representing class i, and that class's number of distinct deals.
>
> Add Poker.hand_indexer using the per-street sums of hole and board cards as round sizes.
>
> Add State.get_hand_index(player_index, street_index=None, board_index=0) and HandHistory.get_hand_indices(player_index, board_index=0). State indexes the player's hole cards and selected board in their original street groups through street_index; None selects the latest street dealt to any player or board. Complete showdown corrections replace cards in their dealt positions; partial shows retain known unshown cards. History returns one index per dealt street, using None for unknown or incomplete required cards; State raises ValueError in those cases.
>
> Use ValueError for argument validation and draw games; integer arguments require ints in range excluding bool.

## What is in this folder

- `task.md`: the problem description the agent sees
- `REDACTED.md`: what was removed from this copy and why
- `Dockerfile`: builds the grading image from the pinned repo checkout
- `Makefile`: clone, checkout, build image (its patch targets need the redacted files)
- `metadata.json`: challenge record (id, status, repo, pinned commit)
- `results/summary.json`: sanitized summary of platform checks, rollouts, review status, and patch hashes

## Reproduce the environment

```bash
make clone               # clone the repo and check out the pinned commit
make build-image         # docker build, linux/amd64
```

The hidden tests and reference solution are not in this copy; see `REDACTED.md`.
