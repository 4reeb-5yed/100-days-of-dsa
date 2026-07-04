# 100 Days of DSA — an autonomous CI/CD pipeline demo

This repo is the visible output of a scheduled, multi-repo GitHub Actions
pipeline. A private orchestrator repo clones a pre-validated content bank,
writes new files here, runs tests locally, opens a pull request, waits for
an independent CI check to genuinely pass, and only then merges —
automatically, once a day, with no manual intervention after setup.

The project was built to explore:
- Secure credential scoping across multiple repositories (separate
  least-privilege tokens for build-time vs. runtime use)
- Fail-closed CI gating — broken code is structurally prevented from
  reaching `main`, verified via two independent test runs
- Branch-protection-respecting automated merges (no bypass flags)
- Debugging real pipeline failures: an import-path/module-naming bug, a
  merge-logic bug that silently ignored failing CI checks, and a
  fork-PR secret-exposure consideration

The daily content itself (DSA solutions) comes from a private, pre-written
question bank — the interesting engineering here is the pipeline that
delivers and verifies it, not live problem-solving.

## Progress

| Day | Problem | Topic | Difficulty | Date |
|-----|---------|-------|------------|------|
<!-- PROGRESS_TABLE_START -->
| 001 | Two Sum | array-hashing | easy | 2026-07-04 |
| 002 | Contains Duplicate | array-hashing | easy | 2026-07-04 |
| 003 | Valid Anagram | array-hashing | easy | 2026-07-04 |
<!-- PROGRESS_TABLE_END -->

## About This Project

This repository tracks my 100-day journey learning Data Structures and Algorithms. Each day, a new problem solution is automatically added to this repository via GitHub Actions.

Problems are sourced from a private question bank and include:
- Real, correct Python solutions
- Comprehensive test cases
- Difficulty ratings (easy, medium, hard)
- Topic categorization

## Running Tests

```bash
pip install -r requirements.txt
pytest
```
