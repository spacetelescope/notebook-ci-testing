# Using the On-Demand Error Report Generator

This guide shows you how to use the GitHub Actions workflow to generate error reports for notebook execution failures.

## Quick Start

### Step 1: Navigate to Actions

1. Go to the [notebook-ci-testing repository](https://github.com/spacetelescope/notebook-ci-testing)
2. Click on the **Actions** tab at the top
3. In the left sidebar, click on **"Notebook CI - On-Demand Actions"**

### Step 2: Run the Workflow

1. Click the **"Run workflow"** dropdown button (top right)
2. You'll see a form with several options:

### Step 3: Configure the Report

**Action to perform:** Select **"generate-error-report"** from the dropdown

**Optional Configuration:**

- **Python version**: Leave as default (3.11) or choose your preferred version
- **Workflow to analyze**: 
  - `all` (default) - Analyzes all workflow types
  - `scheduled` - Only the weekly scheduled runs
  - `main-branch` - Only main branch pushes
  - `on-demand` - Only manually triggered runs
  - `pull-request` - Only PR workflows
  
- **Number of recent runs**: How many runs to analyze per workflow (default: 10)
  - Use 5 for a quick check
  - Use 20-30 for deeper analysis
  - Higher numbers take longer but provide more historical context
  
- **Include detailed error logs**: 
  - `false` (default) - Quick summary only
  - `true` - Includes error excerpts from logs (slower but more informative)

### Step 4: Submit and Wait

1. Click the green **"Run workflow"** button at the bottom
2. The page will refresh and show your workflow run at the top
3. Click on the run to see progress
4. Wait for the workflow to complete (usually 1-2 minutes)

### Step 5: Download the Report

1. Scroll down to the **Artifacts** section at the bottom of the workflow run page
2. Click on **"notebook-error-report"** to download
3. Extract the ZIP file to get `error_report.md`
4. Open `error_report.md` in any markdown viewer or text editor

### Step 6: View Summary in GitHub

The workflow also displays a quick preview in the GitHub Actions summary:

1. On the workflow run page, look for the **"Display report summary"** step
2. Click on it to expand
3. You'll see the first 50 lines of the report directly in GitHub

## Configuration Examples

### Example 1: Quick Weekly Check
```
Action: generate-error-report
Workflow: scheduled
Number of runs: 5
Include logs: false
```
**Use case**: Weekly maintenance check to see if scheduled runs are working

### Example 2: Deep Dive Investigation
```
Action: generate-error-report
Workflow: all
Number of runs: 20
Include logs: true
```
**Use case**: Investigating patterns across all workflows with detailed error information

### Example 3: PR Stability Check
```
Action: generate-error-report
Workflow: pull-request
Number of runs: 10
Include logs: false
```
**Use case**: Verify that PR workflows are stable before merging changes

### Example 4: Main Branch Health
```
Action: generate-error-report
Workflow: main-branch
Number of runs: 15
Include logs: true
```
**Use case**: Check if recent main branch deployments have introduced failures

## Understanding the Report

The generated report includes:

### 1. Header Section
- Generation timestamp
- Repository information
- Configuration used

### 2. Per-Workflow Analysis
For each workflow analyzed:
- **Workflow ID** and name
- **Total runs** analyzed
- **Failure rate** (percentage)
- List of failed runs with:
  - Run number and title
  - Direct link to GitHub Actions page
  - Timestamp
  - Failed job details
  - Notebook paths that failed
  - Error excerpts (if enabled)

### 3. Summary Section
- Overall findings
- Recommendations (if patterns detected)

## Tips and Best Practices

### When to Generate Reports

- **Weekly**: Use scheduled workflow reports to track stability over time
- **Before releases**: Check all workflows before major releases
- **After infrastructure changes**: Verify no regressions after CI/CD updates
- **When investigating issues**: Deep dive with logs enabled

### Choosing Parameters

**Number of runs:**
- **5 runs**: Quick health check
- **10 runs** (default): Good balance for weekly monitoring
- **20-30 runs**: Comprehensive analysis for troubleshooting
- **50+ runs**: Historical trend analysis (slow with logs enabled)

**Include logs:**
- **false**: Fast, good for high-level overview
- **true**: Slower, use when you need to diagnose specific errors

**Workflow selection:**
- **all**: General health check
- **scheduled**: Most important for production stability
- **pull-request**: Check CI quality
- **main-branch**: Monitor deployment health

### Automating Report Generation

You can set up automated report generation:

1. Create a scheduled workflow that runs the error report generator
2. Email or post the report to a monitoring channel
3. Create GitHub issues for high failure rates

Example workflow snippet:
```yaml
name: Weekly Error Report

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM

jobs:
  generate-report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements-reporting.txt
      - run: python generate_error_report.py --workflow scheduled --output report.md
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/upload-artifact@v4
        with:
          name: weekly-report
          path: report.md
```

## Troubleshooting

### Workflow fails immediately
- Check that all required files are present in the repository
- Verify `requirements-reporting.txt` exists
- Check `generate_error_report.py` exists and is executable

### Report shows "No data"
- Ensure workflows have actually run in the selected timeframe
- Try increasing the number of runs to analyze
- Verify your GitHub token has proper permissions

### Workflow times out
- Reduce the number of runs to analyze
- Disable log inclusion (set to false)
- Focus on a single workflow instead of all

### Can't find the artifact
- Make sure the workflow completed successfully (green checkmark)
- Scroll to the bottom of the workflow run page
- Look for the "Artifacts" section
- The artifact is automatically deleted after 30 days

## Next Steps

After reviewing your report:

1. **Identify patterns**: Look for notebooks that fail frequently
2. **Check recent changes**: Use git blame on failing notebooks
3. **Review logs**: Click the GitHub Actions links in the report
4. **Fix issues**: Address the most critical failures first
5. **Re-run**: Generate another report after fixes to verify

## Command Line Alternative

If you prefer to run locally instead of using GitHub Actions:

```bash
# Install dependencies
pip install -r requirements-reporting.txt

# Set your GitHub token
export GITHUB_TOKEN=your_token_here

# Generate report
python generate_error_report.py --workflow scheduled --output report.md

# Open report
cat report.md
```

## Support

For issues with the error reporting tool:
- Open an issue on GitHub
- Submit a [JWST Help Desk Ticket](https://jwsthelp.stsci.edu)
- Check the [REPORTING.md](REPORTING.md) documentation
