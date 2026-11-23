# The Command Helper That Missed a Near Match

A fictional label helper gets `deply`. Its approved labels include `deploy`, but no suggestion appears. Repair only `edit_distance(left, right)` in `distance.py`. This helper displays labels; it never runs commands or changes systems.

## Run locally

Python 3.11+, standard library only, from this repository:

```sh
python monitor.py
python -m unittest discover -v
```

The starter intentionally fails. Keep `support.py`, fixtures, tests, monitor and public signature unchanged; additional regression tests are welcome. Submit a PR against `main` with passing checks and a brief explanation of a regression beyond the visible typo.

## Contract

Return the minimum total cost to turn `left` into `right`: inserting, deleting or substituting one code point each costs one. Matching code points cost zero. An adjacent swap is not a separate operation. Return the exact built-in integer distance, not a similarity percentage or a threshold-capped answer.

Both arguments must be exact built-in strings, each at most 256 code points; otherwise raise `ValueError`. Keep the supplied validation call before computing. Empty strings are valid. Compare Python string elements exactly: no trimming, case conversion, Unicode normalization or grapheme clustering. Strings are immutable; retain no state between calls. Use bounded polynomial work, not enumeration of all edit sequences. No timing claim is made for a production service.

The monitor tests `deply` against frozen labels `deploy`, `status`, `logs` with threshold 1. Fix the distance function rather than widening the threshold or special-casing a label.

## Scope

This authored local exercise covers a distance metric, not shell parsing, execution, semantic command correctness or a complete search engine. Local checks do not prove hosted GetIn integration. The maintainer reference is kept outside this learner repository.
