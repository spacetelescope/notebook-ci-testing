# Notebook Actions Execution Error Reporting

This repository includes tools to generate comprehensive reports of notebook execution errors from GitHub Actions workflows.

## Overview

The `generate_error_report.py` script fetches data from the GitHub Actions API and creates a detailed report of:
- Recent workflow runs and their status
- Failed or cancelled runs
- Specific notebook failures
- Error excerpts (optional)

## Quick Start: On-Demand GitHub Action

The **easiest way** to generate an error report is using the on-demand GitHub Action:

1. Go to the [Actions tab](https://github.com/spacetelescope/notebook-ci-testing/actions/workflows/notebook-on-demand.yml) in this repository
2. Click "Run workflow"
3. Select **"generate-error-report"** from the "Action to perform" dropdown
4. Configure options:
   - **Workflow to analyze**: Choose which workflow to analyze (scheduled, main-branch, on-demand, pull-request, or all)
   - **Number of runs**: How many recent runs to analyze (default: 10)
   - **Include logs**: Whether to include detailed error excerpts (slower but more detailed)
5. Click "Run workflow"
6. Wait for the workflow to complete
7. Download the generated report from the workflow artifacts

This method requires no local setup and uses the repository's GitHub token automatically.

## Prerequisites (for local usage)

1. **Python 3.7+** is required
2. **Install dependencies**:
   ```bash
   pip install -r requirements-reporting.txt
   ```

3. **GitHub Personal Access Token** (recommended for higher API rate limits):
   - Go to GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
   - Click "Generate new token"
   - Select the `repo` scope (for accessing workflow runs)
   - Copy the generated token
   - Set it as an environment variable:
     ```bash
     export GITHUB_TOKEN=your_token_here
     ```

## Usage

### Basic Usage

Generate a report for all workflows:
```bash
python generate_error_report.py
```

### Generate Report for Specific Workflow

```bash
# Scheduled workflow only
python generate_error_report.py --workflow scheduled

# Pull request workflow only
python generate_error_report.py --workflow pull-request
```

### Save Report to File

```bash
python generate_error_report.py --output notebook_errors.md
```

### Include Error Log Excerpts

This option fetches and parses job logs to extract error details (slower but more detailed):
```bash
python generate_error_report.py --include-logs
```

### Analyze More Runs

By default, the script analyzes the 10 most recent runs. To analyze more:
```bash
python generate_error_report.py --runs 20
```

### Complete Example

Generate a detailed report of the last 15 scheduled workflow runs with error logs:
```bash
python generate_error_report.py \
  --workflow scheduled \
  --runs 15 \
  --include-logs \
  --output scheduled_errors_report.md
```

## Available Workflows

The script can analyze the following workflows:
- `scheduled` - Weekly scheduled notebook execution
- `main-branch` - Runs on main branch pushes
- `on-demand` - Manually triggered runs
- `pull-request` - Runs on pull requests

## Report Format

The generated report includes:

### Summary Section
- Total runs analyzed
- Number and percentage of failed runs
- Workflow information

### Failed Runs Details
For each failed run:
- Run number and title
- Run ID and URL (direct link to GitHub Actions)
- Timestamp
- List of failed jobs
- Notebook names that failed
- Error excerpts (if `--include-logs` is used)

## Example Report Output

See [SAMPLE_REPORT.md](SAMPLE_REPORT.md) for a complete example of what the generated report looks like.

Quick preview:

```markdown
# Notebook Actions Execution Error Report

Generated: 2026-02-01 15:30:00 UTC
Repository: spacetelescope/notebook-ci-testing
================================================================================

## Workflow: SCHEDULED

Workflow ID: 172161028
Recent runs analyzed: 10
Failed/Cancelled runs: 7 (70.0%)

### Failed Runs:

#### Run #58 - Notebook CI - Scheduled
- **ID**: 21555602895
- **Status**: FAILURE
- **Date**: 2026-02-01T03:10:14Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/21555602895
- **Failed Jobs**: 4

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/SOSS/JWPipeNB-niriss-soss.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/SOSS/JWPipeNB-niriss-soss.ipynb
...
```

## Troubleshooting

### Rate Limit Errors

If you see `403 Forbidden` errors:
- You're hitting GitHub's API rate limit (60 requests/hour without authentication)
- Solution: Use a GitHub Personal Access Token (see Prerequisites)

### Missing Dependencies

If you see `ImportError: No module named 'requests'`:
- Install dependencies: `pip install -r requirements-reporting.txt`

### No Data Returned

If the report shows no workflow runs:
- Check that the repository name and owner are correct in the script
- Verify your GitHub token has the necessary permissions
- Check that workflows have actually been run

## Automation

You can automate report generation using cron jobs or GitHub Actions:

### Example: Weekly Report via Cron

```bash
# Add to crontab (runs every Monday at 9 AM)
0 9 * * 1 cd /path/to/repo && python generate_error_report.py --workflow scheduled --output weekly_report.md
```

### Example: GitHub Actions Workflow

Create `.github/workflows/error-report.yml`:

```yaml
name: Generate Error Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM
  workflow_dispatch:

jobs:
  generate-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements-reporting.txt
      
      - name: Generate report
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python generate_error_report.py --workflow scheduled --output error_report.md
      
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: error-report
          path: error_report.md
```

## Contributing

To improve the error reporting script:
1. Fork the repository
2. Make your changes to `generate_error_report.py`
3. Test thoroughly with different workflows
4. Submit a pull request

## Support

For issues or questions:
- Open an issue on GitHub
- Submit a [JWST Help Desk Ticket](https://jwsthelp.stsci.edu)
