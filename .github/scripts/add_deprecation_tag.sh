#!/bin/bash

# Function to add deprecation tag
add_deprecation_tag() {
  notebook=$1
  tmpfile=$(mktemp)
  
  # Check if the deprecation tag already exists
  if jq -e '.metadata.deprecated' "$notebook" > /dev/null; then
    echo "Deprecation tag already exists in $notebook"
  else
    jq '.metadata.deprecated = true' "$notebook" > "$tmpfile" && mv "$tmpfile" "$notebook"
    echo "Deprecation tag added to $notebook"
  fi
}

# Usage: ./add_deprecation_tag.sh <notebook-path>
add_deprecation_tag "$1"
