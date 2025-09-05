# Pull Request Template (PR.md)

## Title

<!-- Use imperative tone, concise summary -->

`fix(game): prevent double merge in 2048 left move`

---

## Summary

<!-- What this PR does in plain English -->

---

## Context / Why

<!-- Why this change is needed, reference bug/issue if exists -->

---

## Changes

* [ ] List the main code changes
* [ ] Mention new helpers/utilities
* [ ] Include docs/tests added

---

## How to Test

1. Commands to run tests (`npm test`, `pytest`, etc.)
2. Manual steps to reproduce and verify fix/feature
3. Expected vs actual output examples

---

## Risk & Rollback

* [ ] Low / Medium / High risk
* [ ] How to rollback if issues occur (e.g., revert commit SHA)

---

## Related

* Closes #<issue-number>
* References <docs or discussions>

---

# Git Workflow Cheatsheet (step-by-step)

## Setup

```bash
# Clone repo
git clone <repo-url>
cd <repo>

# Create new branch
git checkout -b feature/<short-name>
```

## During Work

```bash
# Stage changes
git add <files>

# Commit (use conventional commits style)
git commit -m "fix(game): enforce single merge rule"

# Run tests before pushing
npm test   # or pytest
```

## Sync with Upstream (before PR)

```bash
git fetch origin
git rebase origin/main
# Resolve conflicts if any, then:
git rebase --continue
```

## Push & Open PR

```bash
# Push branch
git push origin feature/<short-name>

# Create PR (GitHub CLI example)
gh pr create --fill \
  --base main \
  --head feature/<short-name> \
  --title "fix(game): prevent double merge" \
  --body-file PR.md
```

## Review Loop

```bash
# After feedback
# Make changes, stage and commit again
git add <files>
git commit -m "chore(review): address reviewer feedback"

# Push updates
git push origin feature/<short-name>
```

## After Merge

```bash
git checkout main
git pull --rebase

# Clean up branch
git branch -D feature/<short-name>
git push origin --delete feature/<short-name>
```
