#!/usr/bin/env bash

set -euo pipefail

: "${GH_TOKEN:?GH_TOKEN is required}"
: "${RRN_SOURCE_REPOSITORY:?RRN_SOURCE_REPOSITORY is required}"
: "${RRN_SOURCE_REF:?RRN_SOURCE_REF is required}"
: "${RRN_SOURCE_VERSION:?RRN_SOURCE_VERSION is required}"
: "${RRN_VERSION_KIND:?RRN_VERSION_KIND is required}"
: "${RRN_TARGET_ENVIRONMENT:?RRN_TARGET_ENVIRONMENT is required}"
: "${RRN_DELIVERY_MODE:?RRN_DELIVERY_MODE is required}"
: "${RRN_SOURCE_SHA:?RRN_SOURCE_SHA is required}"
: "${RRN_RELEASE_URL:?RRN_RELEASE_URL is required}"
: "${RRN_CORRELATION_ID:?RRN_CORRELATION_ID is required}"

spi_repository=${SPI_REPOSITORY:-spacetelescope/science-platform-images}
spi_workflow=${SPI_WORKFLOW:-build-roman-research-nexus.yml}

gh workflow run "$spi_workflow" \
    --repo "$spi_repository" \
    --ref main \
    -f source_repository="$RRN_SOURCE_REPOSITORY" \
    -f roman_notebooks_ref="$RRN_SOURCE_REF" \
    -f roman_notebooks_version="$RRN_SOURCE_VERSION" \
    -f roman_notebooks_version_kind="$RRN_VERSION_KIND" \
    -f target_environment="$RRN_TARGET_ENVIRONMENT" \
    -f roman_notebooks_delivery_mode_recommendation="$RRN_DELIVERY_MODE" \
    -f roman_notebooks_sha="$RRN_SOURCE_SHA" \
    -f roman_notebooks_release_url="$RRN_RELEASE_URL" \
    -f correlation_id="$RRN_CORRELATION_ID"

run_id=""
for _ in {1..60}; do
    run_id=$(
        gh run list \
            --repo "$spi_repository" \
            --workflow "$spi_workflow" \
            --event workflow_dispatch \
            --limit 50 \
            --json databaseId,displayTitle \
            --jq ".[] | select(.displayTitle | contains(\"[$RRN_CORRELATION_ID]\")) | .databaseId" \
            | head -n1
    )
    if [[ -n "$run_id" ]]; then
        break
    fi
    sleep 10
done

if [[ -z "$run_id" ]]; then
    echo "Could not locate the dispatched SPI workflow run." >&2
    exit 1
fi

run_url="https://github.com/${spi_repository}/actions/runs/${run_id}"
echo "SPI workflow run: $run_url"
echo "rrn_run_url=$run_url" >> "$GITHUB_OUTPUT"

gh run watch "$run_id" --repo "$spi_repository" --exit-status
