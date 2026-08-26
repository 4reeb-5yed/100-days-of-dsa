# 100 Days of DSA — an Autonomous CI/CD Pipeline Demo

[![CI](https://github.com/4reeb-5yed/100-days-of-dsa/actions/workflows/ci.yml/badge.svg)](https://github.com/4reeb-5yed/100-days-of-dsa/actions/workflows/ci.yml)
[![Tests](https://img.shields.io/badge/tests-165%20passed-brightgreen)]()

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

**Day 56 of 100** ████████████████████████████░░░░░░░░░░░░░░░░░░░░░░ 56%

| # | Problem | Topic | Level |
|---|---------|-------|-------|
| 001 | Two Sum | array-hashing | 🟢 easy |
| 002 | Contains Duplicate | array-hashing | 🟢 easy |
| 003 | Valid Anagram | array-hashing | 🟢 easy |
| 004 | Best Time to Buy and Sell Stock | array-hashing | 🟢 easy |
| 005 | Product of Array Except Self | array-hashing | medium |
| 006 | Find Minimum in Rotated Sorted Array | binary-search | medium |
| 007 | Search in Rotated Sorted Array | binary-search | medium |
| 008 | 3Sum | two-pointers | medium |
| 009 | Container With Most Water | two-pointers | medium |
| 010 | Trapping Rain Water | two-pointers | hard |
| 011 | Longest Consecutive Sequence | array-hashing | easy |
| 012 | Subarray Sum Equals K | two-pointers | medium |
| 013 | Find Peak Element | binary-search | medium |
| 014 | Reverse Linked List | linked-lists | easy |
| 015 | Maximum Depth of Binary Tree | trees | easy |
| 016 | Invert Binary Tree | trees | easy |
| 017 | Combination Sum | backtracking | medium |
| 018 | Valid Parentheses | stacks | easy |
| 019 | Implement Trie | tries | medium |
| 020 | Kth Largest Element | heaps | medium |
| 021 | Jump Game | greedy | medium |
| 022 | Find All Numbers Disappeared | array-hashing | easy |
| 023 | Number of Islands | graphs | medium |
| 024 | House Robber | dynamic-programming | medium |
| 025 | Merge Two Sorted Lists | linked-lists | easy |
| 026 | Longest Substring Without Repeating Characters | sliding-window | medium |
| 027 | Single Number | bit-manipulation | easy |
| 028 | Coin Change | dynamic-programming | medium |
| 029 | Move Zeroes | array-hashing | easy |
| 030 | Sort Colors | two-pointers | medium |
| 031 | Merge Intervals | intervals | easy |
| 032 | Word Break | dynamic-programming | hard |
| 033 | N-Queens | backtracking | hard |
| 034 | Clone Graph | graphs | hard |
| 035 | Regular Expression Matching | dynamic-programming | hard |
| 036 | Evaluate Reverse Polish Notation | stacks | medium |
| 037 | Binary Tree Level Order Traversal | trees | medium |
| 038 | Number of Provinces | graphs | medium |
| 039 | Course Schedule | graphs | medium |
| 040 | Pacific Atlantic Water Flow | graphs | medium |
| 041 | Minimum Genetic Mutation | graphs | hard |
| 042 | Integer to Roman | math | medium |
| 043 | Trapping Rain Water II | heaps | hard |
| 044 | Evaluate Division | graphs | medium |
| 045 | K Closest Points to Origin | heaps | medium |
| 046 | Longest Increasing Path in Matrix | dynamic-programming | hard |
| 047 | Maximum Sum Circular Subarray | dynamic-programming | hard |
| 048 | Insert Delete GetRandom O(1) | design | medium |
| 049 | Fizz Buzz | math | easy |
| 050 | Find Minimum in Rotated Sorted Array II | binary-search | hard |
| 051 | Combination Sum II | backtracking | medium |
| 052 | Permutations | backtracking | medium |
| 053 | Subsets | backtracking | medium |
| 054 | Word Search | backtracking | hard |
| 055 | Binary Tree Right Side View | trees | medium |
| 056 | Count Good Nodes in Binary Tree | trees | medium |
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
