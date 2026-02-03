#!/usr/bin/env python3
"""
Generate a report of notebook execution errors from GitHub Actions workflows.

This script fetches recent workflow runs from the GitHub Actions API and generates
a comprehensive report of notebook execution failures.

Usage:
    python generate_error_report.py [--token GITHUB_TOKEN] [--runs N] [--workflow WORKFLOW_ID]

Requirements:
    - requests library (pip install requests)
    - GITHUB_TOKEN environment variable or --token argument
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)


class NotebookErrorReporter:
    """Generate reports of notebook execution errors from GitHub Actions."""

    REPO_OWNER = "spacetelescope"
    REPO_NAME = "notebook-ci-testing"
    
    # Workflow IDs for notebook CI
    WORKFLOWS = {
        "scheduled": 172161028,
        "main-branch": 172161025,
        "on-demand": 172161026,
        "pull-request": 172161027,
    }

    def __init__(self, token: Optional[str] = None):
        """Initialize the reporter with GitHub token."""
        self.token = token or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            print("Warning: No GitHub token provided. API rate limits will be restrictive.")
        
        self.session = requests.Session()
        if self.token:
            self.session.headers.update({
                "Authorization": f"token {self.token}",
                "Accept": "application/vnd.github.v3+json"
            })

    def get_workflow_runs(self, workflow_id: int, max_runs: int = 10) -> List[Dict]:
        """Fetch recent workflow runs for a specific workflow."""
        url = f"https://api.github.com/repos/{self.REPO_OWNER}/{self.REPO_NAME}/actions/workflows/{workflow_id}/runs"
        params = {"per_page": max_runs}
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("workflow_runs", [])
        except requests.RequestException as e:
            print(f"Error fetching workflow runs: {e}")
            return []

    def get_failed_jobs(self, run_id: int) -> List[Dict]:
        """Fetch failed jobs for a specific workflow run."""
        url = f"https://api.github.com/repos/{self.REPO_OWNER}/{self.REPO_NAME}/actions/runs/{run_id}/jobs"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            data = response.json()
            jobs = data.get("jobs", [])
            return [job for job in jobs if job.get("conclusion") in ["failure", "cancelled"]]
        except requests.RequestException as e:
            print(f"Error fetching jobs for run {run_id}: {e}")
            return []

    def get_job_logs(self, job_id: int) -> Optional[str]:
        """Fetch logs for a specific job."""
        url = f"https://api.github.com/repos/{self.REPO_OWNER}/{self.REPO_NAME}/actions/jobs/{job_id}/logs"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching logs for job {job_id}: {e}")
            return None

    def extract_error_info(self, log_content: str) -> Dict[str, any]:
        """Extract relevant error information from job logs."""
        if not log_content:
            return {}
        
        errors = []
        lines = log_content.split('\n')
        
        # Look for common error patterns
        error_patterns = [
            "ERROR",
            "FAILED",
            "Error:",
            "Exception:",
            "Traceback",
            "##[error]",
            "CRITICAL",
        ]
        
        for i, line in enumerate(lines):
            for pattern in error_patterns:
                if pattern in line:
                    # Get context around the error (5 lines before and after)
                    start = max(0, i - 5)
                    end = min(len(lines), i + 6)
                    context = '\n'.join(lines[start:end])
                    errors.append({
                        "line_number": i + 1,
                        "pattern": pattern,
                        "context": context[:500]  # Limit context size
                    })
                    break
        
        return {
            "error_count": len(errors),
            "errors": errors[:10]  # Limit to first 10 errors
        }

    def generate_report(self, workflow_name: str = None, max_runs: int = 10, 
                       include_logs: bool = False) -> str:
        """Generate a comprehensive error report."""
        report_lines = [
            "# Notebook Actions Execution Error Report",
            f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}",
            f"\nRepository: {self.REPO_OWNER}/{self.REPO_NAME}",
            "\n" + "=" * 80,
        ]

        workflows_to_check = {}
        if workflow_name and workflow_name in self.WORKFLOWS:
            workflows_to_check[workflow_name] = self.WORKFLOWS[workflow_name]
        else:
            workflows_to_check = self.WORKFLOWS

        for wf_name, wf_id in workflows_to_check.items():
            report_lines.append(f"\n## Workflow: {wf_name.upper()}")
            report_lines.append(f"\nWorkflow ID: {wf_id}")
            
            runs = self.get_workflow_runs(wf_id, max_runs)
            if not runs:
                report_lines.append("\n⚠️  No workflow runs found or unable to fetch data.")
                continue
            
            failed_runs = [r for r in runs if r.get("conclusion") in ["failure", "cancelled"]]
            total_runs = len(runs)
            failed_count = len(failed_runs)
            
            report_lines.append(f"\nRecent runs analyzed: {total_runs}")
            report_lines.append(f"Failed/Cancelled runs: {failed_count} ({failed_count/total_runs*100:.1f}%)")
            
            if not failed_runs:
                report_lines.append("\n✅ No failures in recent runs!")
                continue
            
            report_lines.append("\n### Failed Runs:")
            
            for run in failed_runs[:5]:  # Show details for last 5 failed runs
                run_id = run["id"]
                created_at = run.get("created_at", "Unknown")
                conclusion = run.get("conclusion", "unknown")
                display_title = run.get("display_title", "Untitled")
                
                report_lines.append(f"\n#### Run #{run['run_number']} - {display_title}")
                report_lines.append(f"- **ID**: {run_id}")
                report_lines.append(f"- **Status**: {conclusion.upper()}")
                report_lines.append(f"- **Date**: {created_at}")
                report_lines.append(f"- **URL**: {run['html_url']}")
                
                failed_jobs = self.get_failed_jobs(run_id)
                if failed_jobs:
                    report_lines.append(f"- **Failed Jobs**: {len(failed_jobs)}")
                    
                    for job in failed_jobs[:3]:  # Show first 3 failed jobs
                        job_name = job.get("name", "Unknown job")
                        job_conclusion = job.get("conclusion", "unknown")
                        
                        # Extract notebook name from job name if possible
                        notebook = "N/A"
                        if "process-notebooks" in job_name and "(" in job_name:
                            notebook = job_name.split("(")[-1].rstrip(")")
                        
                        report_lines.append(f"\n  **Job**: {job_name}")
                        report_lines.append(f"  - Conclusion: {job_conclusion}")
                        report_lines.append(f"  - Notebook: {notebook}")
                        
                        if include_logs:
                            logs = self.get_job_logs(job["id"])
                            if logs:
                                error_info = self.extract_error_info(logs)
                                if error_info.get("error_count", 0) > 0:
                                    report_lines.append(f"  - Errors found: {error_info['error_count']}")
                                    if error_info.get("errors"):
                                        report_lines.append("  - Sample error:")
                                        first_error = error_info["errors"][0]
                                        report_lines.append(f"```\n{first_error.get('context', 'No context')}\n```")
            
            report_lines.append("\n" + "-" * 80)
        
        report_lines.append("\n## Summary")
        report_lines.append("\nThis report shows recent notebook execution failures from GitHub Actions workflows.")
        report_lines.append("For detailed logs, visit the GitHub Actions page for each run.")
        
        return '\n'.join(report_lines)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate notebook execution error report from GitHub Actions"
    )
    parser.add_argument(
        "--token",
        help="GitHub personal access token (or use GITHUB_TOKEN env var)",
        default=None
    )
    parser.add_argument(
        "--runs",
        type=int,
        default=10,
        help="Number of recent runs to analyze per workflow (default: 10)"
    )
    parser.add_argument(
        "--workflow",
        choices=["scheduled", "main-branch", "on-demand", "pull-request"],
        help="Specific workflow to analyze (default: all workflows)"
    )
    parser.add_argument(
        "--include-logs",
        action="store_true",
        help="Include error log excerpts in the report (slower)"
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: print to stdout)"
    )
    
    args = parser.parse_args()
    
    reporter = NotebookErrorReporter(token=args.token)
    report = reporter.generate_report(
        workflow_name=args.workflow,
        max_runs=args.runs,
        include_logs=args.include_logs
    )
    
    if args.output:
        try:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        except IOError as e:
            print(f"Error writing report to file: {e}")
            sys.exit(1)
    else:
        print(report)


if __name__ == "__main__":
    main()
