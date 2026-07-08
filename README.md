# 100 Days of DSA — an Autonomous CI/CD Pipeline Demo

[![CI](https://github.com/4reeb-5yed/100-days-of-dsa/actions/workflows/ci.yml/badge.svg)](https://github.com/4reeb-5yed/100-days-of-dsa/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-16%20passed-brightgreen)]()

📖 **[Pipeline Build Guide](https://4reeb-5yed.github.io/100-days-of-dsa/)** — Step-by-step instructions to build this CI/CD system

## Related Repos

| Repo | Role |
|------|------|
| **[dsa-bot](https://github.com/4reeb-5yed/dsa-bot)** | Orchestrator — picks problems, writes files, opens PRs, merges after CI |
| **[dsa-question-bank](https://github.com/4reeb-5yed/dsa-question-bank)** | Content bank — 120 DSA problems with solutions & tests |

This repo is the visible output of a scheduled, multi-repo GitHub Actions
pipeline. The orchestrator (`dsa-bot`) clones a pre-validated content bank,
writes new files here, runs tests locally, opens a pull request, waits for
an independent CI check to genuinely pass, and only then merges —
automatically, once a day, with no manual intervention after setup.

## Progress

**Day 7 of 100** ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 7%

| # | Problem | Topic | Level |
|---|---------|-------|-------|
| 001 | Two Sum | array-hashing | 🟢 easy |
| 002 | Contains Duplicate | array-hashing | 🟢 easy |
| 003 | Valid Anagram | array-hashing | 🟢 easy |
| 004 | Best Time to Buy and Sell Stock | array-hashing | 🟢 easy |
| 005 | Product of Array Except Self | array-hashing | medium |
| 006 | Find Minimum in Rotated Sorted Array | binary-search | medium |
| 007 | Search in Rotated Sorted Array | binary-search | medium |
<!-- PROGRESS_TABLE_END -->

## Repository Structure

```
├── .github/workflows/ci.yml   # Independent CI verification gate
├── solutions/                 # DSA problem solutions (auto-generated)
│   └── day_XXX_*.py
├── tests/                     # Pytest test cases
│   └── test_day_XXX_*.py
├── pytest.ini                 # Python path configuration
├── requirements.txt           # Dependencies (pytest)
└── index.html                 # Full pipeline documentation
```

## The Engineering Story

This project was built to explore:
- **Secure credential scoping** across multiple repositories (separate
  least-privilege tokens for build-time vs. runtime use)
- **Fail-closed CI gating** — broken code is structurally prevented from
  reaching `main`, verified via two independent test runs
- **Branch-protection-respecting automated merges** (no bypass flags)
- **Real pipeline debugging**: import-path/module-naming bugs, merge-logic
  bugs that silently ignored failing CI checks, and fork-PR secret-exposure
  considerations

The daily content (DSA solutions) comes from a pre-written question bank
— the interesting engineering here is the pipeline that delivers and
verifies it, not live problem-solving.

## Running Tests

```bash
pip install -r requirements.txt
python -m pytest
```
