# Notebook Actions Execution Error Report

Generated: 2026-02-03 18:15:00 UTC

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

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/WFSS/JWPipeNB-niriss-wfss.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/WFSS/JWPipeNB-niriss-wfss.ipynb

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/Imaging/JWPipeNB-niriss-imaging.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/Imaging/JWPipeNB-niriss-imaging.ipynb

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/SOSS/JWPipeNB-niriss-soss.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/SOSS/JWPipeNB-niriss-soss.ipynb
  - Error: Memory usage exceeded 85% during pipeline execution (Cell 32/52)
  - Details: Runner received shutdown signal during heavy memory operations

--------------------------------------------------------------------------------

#### Run #57 - Notebook CI - Scheduled
- **ID**: 21325813016
- **Status**: FAILURE
- **Date**: 2026-01-25T02:55:45Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/21325813016
- **Failed Jobs**: 3

  **Job**: execute-all / process-notebooks (notebooks/MIRI/MRS/JWPipeNB-MIRI-MRS.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/MRS/JWPipeNB-MIRI-MRS.ipynb

  **Job**: execute-all / process-notebooks (notebooks/NIRCAM/Imaging/JWPipeNB-nircam-imaging.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRCAM/Imaging/JWPipeNB-nircam-imaging.ipynb

  **Job**: execute-all / process-notebooks (notebooks/NIRSPEC/IFU/JWPipeNB-NIRSpec-IFU.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRSPEC/IFU/JWPipeNB-NIRSpec-IFU.ipynb

--------------------------------------------------------------------------------

#### Run #56 - Notebook CI - Scheduled
- **ID**: 21104875982
- **Status**: FAILURE
- **Date**: 2026-01-18T02:52:42Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/21104875982
- **Failed Jobs**: 2

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/AMI/JWPipeNB-niriss-ami.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/AMI/JWPipeNB-niriss-ami.ipynb

  **Job**: execute-all / process-notebooks (notebooks/MIRI/Coronagraphy/JWPipeNB-MIRI-Coron.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/Coronagraphy/JWPipeNB-MIRI-Coron.ipynb

--------------------------------------------------------------------------------

#### Run #55 - Notebook CI - Scheduled
- **ID**: 20888383827
- **Status**: FAILURE
- **Date**: 2026-01-11T02:53:42Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/20888383827
- **Failed Jobs**: 5

  **Job**: execute-all / process-notebooks (notebooks/NIRISS/WFSS/JWPipeNB-niriss-wfss.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRISS/WFSS/JWPipeNB-niriss-wfss.ipynb

  **Job**: execute-all / process-notebooks (notebooks/NIRCAM/Coronagraphy/JWPipeNB-nircam-coronagraphy.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRCAM/Coronagraphy/JWPipeNB-nircam-coronagraphy.ipynb

  **Job**: execute-all / process-notebooks (notebooks/MIRI/Imaging/JWPipeNB-MIRI-imaging.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/Imaging/JWPipeNB-MIRI-imaging.ipynb

--------------------------------------------------------------------------------

#### Run #54 - Notebook CI - Scheduled
- **ID**: 20686597182
- **Status**: FAILURE
- **Date**: 2026-01-04T02:54:10Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/20686597182
- **Failed Jobs**: 3

  **Job**: execute-all / process-notebooks (notebooks/NIRSPEC/BOTS/JWPipeNB-NIRSpec-BOTS.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRSPEC/BOTS/JWPipeNB-NIRSpec-BOTS.ipynb

  **Job**: execute-all / process-notebooks (notebooks/MIRI/LRS-slit/JWPipeNB-MIRI-LRS-slit.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/LRS-slit/JWPipeNB-MIRI-LRS-slit.ipynb

  **Job**: execute-all / process-notebooks (notebooks/MIRI/Imaging-TSO/JWPipeNB-MIRI-imaging-TSO.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/Imaging-TSO/JWPipeNB-MIRI-imaging-TSO.ipynb

--------------------------------------------------------------------------------

## Workflow: MAIN-BRANCH

Workflow ID: 172161025

Recent runs analyzed: 10
Failed/Cancelled runs: 3 (30.0%)

### Failed Runs:

#### Run #42 - Add baseurl for GitHub Pages
- **ID**: 21447933553
- **Status**: CANCELLED
- **Date**: 2026-01-28T17:07:37Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/21447933553
- **Failed Jobs**: 0

--------------------------------------------------------------------------------

#### Run #41 - Update workflows to test new jupyterbook v2 for testing
- **ID**: 21442716158
- **Status**: CANCELLED
- **Date**: 2026-01-28T14:43:43Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/21442716158
- **Failed Jobs**: 0

--------------------------------------------------------------------------------

## Workflow: ON-DEMAND

Workflow ID: 172161026

Recent runs analyzed: 10
Failed/Cancelled runs: 2 (20.0%)

### Failed Runs:

#### Run #140 - Notebook CI - On-Demand Actions
- **ID**: 20970401135
- **Status**: FAILURE
- **Date**: 2026-01-13T19:50:07Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/20970401135
- **Failed Jobs**: 2

  **Job**: execute-all / process-notebooks (notebooks/NIRSPEC/MOS/JWPipeNB-NIRSpec-MOS.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRSPEC/MOS/JWPipeNB-NIRSpec-MOS.ipynb

  **Job**: execute-all / process-notebooks (notebooks/MIRI/LRS-slitless-TSO/JWPipeNB-MIRI-LRS-slitless-TSO.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/MIRI/LRS-slitless-TSO/JWPipeNB-MIRI-LRS-slitless-TSO.ipynb

--------------------------------------------------------------------------------

#### Run #139 - Notebook CI - On-Demand Actions
- **ID**: 20858702743
- **Status**: FAILURE
- **Date**: 2026-01-09T16:37:59Z
- **URL**: https://github.com/spacetelescope/notebook-ci-testing/actions/runs/20858702743
- **Failed Jobs**: 1

  **Job**: execute-all / process-notebooks (notebooks/NIRSPEC/FSlit/JWPipeNB-NIRSpec-FS.ipynb)
  - Conclusion: failure
  - Notebook: notebooks/NIRSPEC/FSlit/JWPipeNB-NIRSpec-FS.ipynb

--------------------------------------------------------------------------------

## Workflow: PULL-REQUEST

Workflow ID: 172161027

Recent runs analyzed: 10
Failed/Cancelled runs: 0 (0.0%)

✅ No failures in recent runs!

--------------------------------------------------------------------------------

## Summary

This report shows recent notebook execution failures from GitHub Actions workflows.
For detailed logs, visit the GitHub Actions page for each run.

### Key Findings:

1. **Scheduled Workflow** has the highest failure rate (70% of last 10 runs)
   - Most common failures: NIRISS/SOSS, NIRISS/WFSS, NIRISS/Imaging notebooks
   - Primary issue: Memory constraints during pipeline execution

2. **Main Branch Workflow** shows 30% cancellation rate
   - Runs were manually cancelled, not failed

3. **On-Demand Workflow** has a 20% failure rate
   - Sporadic failures across various notebooks

4. **Pull Request Workflow** is stable with no recent failures

### Recommendations:

1. Investigate memory usage in NIRISS/SOSS notebook (Cell 32/52)
2. Review resource allocation for scheduled workflow runners
3. Consider splitting long-running notebooks into smaller chunks
4. Add memory monitoring and early warnings to prevent runner shutdowns
