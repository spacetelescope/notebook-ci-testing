# Release Guide for Maintainers (Non-Technical)

This guide explains how to run the **Cut release** GitHub Action and what it does for you.
It is written for maintainers who need a clear checklist, not implementation details.

## What This Action Is

The **Cut release** action is the repository's release button.
When you run it, it:

1. Chooses the next release version number.
2. Updates package version references used by notebooks.
3. Commits and pushes those version updates to `main`.
4. Builds and publishes the package to PyPI.
5. Creates release tags.
6. Creates a GitHub Release with auto-generated notes.

In short: it performs the release steps automatically and keeps versioning consistent.

## When to Use It

Run this action when you are ready to publish a new official release.

Typical triggers:

- Approved changes are already merged to `main`.
- You want a new release entry in GitHub.
- You want updated package and notebook dependency versions published.

## Before You Run It

Use this quick checklist:

1. Confirm the PRs intended for the release are merged to `main`.
2. Confirm required repository secrets are set (especially PyPI publishing credentials).
3. Confirm no one else is currently cutting a release.
4. Decide release type:
   - **minor**: normal planned release.
   - **major**: bigger milestone release.

## How to Run It

1. Open the repository on GitHub.
2. Go to **Actions**.
3. Select **Cut release**.
4. Click **Run workflow**.
5. Choose `release_type`:
   - `minor`
   - `major`
6. Run the workflow.

## What Happens During the Run

You will see workflow steps execute automatically. In plain language, the action does the following:

1. Calculates the next release versions.
   - Internal SemVer tag (for CI/version tracking).
   - Calendar-style product version (shown in release naming).
2. Updates the package version and notebook requirements to match the new release.
3. Commits those version updates.
4. Pushes the commit to `main`.
5. Builds and publishes the package to PyPI.
6. Creates and pushes release tags.
7. Creates a GitHub Release marked as latest, with generated release notes.

## What You Should See After Success

After a successful run, you should have:

1. A completed **Cut release** workflow in GitHub Actions.
2. A new release commit on `main` (version bump).
3. New tags (both internal SemVer and calendar-style version).
4. A new GitHub Release page entry.
5. A new package version published to PyPI.

## How to Explain Versioning to Stakeholders

Use this simple wording:

- The project keeps **two version labels** for different purposes.
- One is a technical internal tracker (SemVer).
- One is a release-facing label based on the year (CalVer style).
- Both labels point to the same release content.

## If the Workflow Fails

1. Open the failed workflow run in **Actions**.
2. Expand the first failed step and read the error message.
3. Common causes:
   - Missing/expired PyPI credential.
   - Version conflict (tag already exists).
   - No version-change files were detected.
4. Fix the issue and run the workflow again.
5. If still blocked, contact a repository admin.

## Confluence-Ready Summary (Copy/Paste)

**Release process for maintainers**

- Use the **Cut release** action in GitHub Actions.
- Select `minor` for standard releases; `major` for milestone releases.
- The action automatically updates versions, commits to `main`, publishes to PyPI, creates tags, and creates the GitHub Release page.
- After completion, verify: workflow success, new tags, new release entry, and published package version.
- If it fails, review the failed step in Actions, resolve the issue, and rerun.
