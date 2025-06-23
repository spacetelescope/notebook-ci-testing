# Migration Status for notebook-ci-testing

## Migration Details
- **Repository**: spacetelescope/notebook-ci-testing
- **Migration Date**: Mon Jun 23 13:36:02 EDT 2025
- **Actions Repository**: spacetelescope/notebook-ci-actions
- **Branch**: migrate-to-centralized-actions

## Pre-Migration Workflows
- .github/workflows-backup/adaptiveTesting.yml
- .github/workflows-backup/ci_auto_toc.yml
- .github/workflows-backup/ci_buildondemand.yml
- .github/workflows-backup/ci_execute_merge_generate.yml
- .github/workflows-backup/ci_execute_single.yml
- .github/workflows-backup/ci_html_build.yml
- .github/workflows-backup/ci_manual_html_deploy.yml
- .github/workflows-backup/ci_manual_single_merge_generate.yml
- .github/workflows-backup/ci_nightly.yml
- .github/workflows-backup/ci_runner.yml
- .github/workflows-backup/ci_scheduled_deprecation_check.yml
- .github/workflows-backup/ci_security_scan.yml
- .github/workflows-backup/ci_unified_actions.yml
- .github/workflows-backup/deprecate_notebook.yml
- .github/workflows-backup/pep8_nb_style_check.yml
- .github/workflows-backup/pep8_script_style_check.yml
- .github/workflows-backup/retry-16gb.yml
- .github/workflows-backup/weekly_broken_link_finder.yml

## New Workflows
- .github/workflows/adaptiveTesting.yml
- .github/workflows/ci_auto_toc.yml
- .github/workflows/ci_buildondemand.yml
- .github/workflows/ci_execute_merge_generate.yml
- .github/workflows/ci_execute_single.yml
- .github/workflows/ci_html_build.yml
- .github/workflows/ci_manual_html_deploy.yml
- .github/workflows/ci_manual_single_merge_generate.yml
- .github/workflows/ci_nightly.yml
- .github/workflows/ci_runner.yml
- .github/workflows/ci_scheduled_deprecation_check.yml
- .github/workflows/ci_security_scan.yml
- .github/workflows/ci_unified_actions.yml
- .github/workflows/deprecate_notebook.yml
- .github/workflows/docs-only.yml
- .github/workflows/notebook-ci-main.yml
- .github/workflows/notebook-ci-on-demand.yml
- .github/workflows/notebook-ci-pr.yml
- .github/workflows/pep8_nb_style_check.yml
- .github/workflows/pep8_script_style_check.yml
- .github/workflows/retry-16gb.yml
- .github/workflows/weekly_broken_link_finder.yml

## Configuration Applied
- Default configuration

## Testing Checklist
- [ ] Manual workflow dispatch test
- [ ] Pull request workflow test  
- [ ] Documentation build test
- [ ] Repository-specific features test

## Migration Notes
- Created by migration script on Mon Jun 23 13:36:02 EDT 2025
- Review and customize workflows as needed
- Test thoroughly before merging to main

## Next Steps
1. Review generated workflows
2. Test with workflow_dispatch
3. Create test PR to verify triggers
4. Update repository secrets if needed
5. Merge after successful testing
