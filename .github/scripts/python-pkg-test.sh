#!/usr/bin/env bash

failed="false"

echo "::group::Airtime Analyzer"
if ! make -C analyzer test; then
  failed="true"
fi
echo "::endgroup::"

echo "::group::API Client"
if ! make -C api_clients test; then
  failed="true"
fi
echo "::endgroup::"

if [[ "$failed" = "true" ]]; then
  echo "Python tests failed"
  exit 1
fi
echo "Python tests passed!"
