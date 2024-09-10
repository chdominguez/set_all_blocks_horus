#!/bin/bash

echo "Building plugin..."

current_version=$(git describe --tags)

echo "Current version: $current_version"

sed -i "s/\"version\": \"[^\"]*\"/\"version\": \"$current_version\"/" set_all_remotes/plugin.meta

rm set_all_remotes.hp

zip -r set_all_remotes.hp set_all_remotes
