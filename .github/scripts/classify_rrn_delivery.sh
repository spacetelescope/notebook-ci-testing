#!/usr/bin/env bash

set -euo pipefail

base_ref=${1:?base ref is required}
head_ref=${2:?head ref is required}

delivery_mode=spec
reason="Only notebook content or documentation changed"

while IFS= read -r file; do
    case "$file" in
        *.ipynb|*.md|*.rst|*.png|*.jpg|*.jpeg|*.gif|*.svg|CITATION.cff|_toc.yml|_config.yml)
            ;;
        *)
            delivery_mode=image
            reason="Image-affecting or unclassified file changed: $file"
            break
            ;;
    esac
done < <(git diff --name-only "$base_ref" "$head_ref")

printf 'delivery_mode=%s\n' "$delivery_mode"
printf 'reason=%s\n' "$reason"
