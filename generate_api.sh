#!/bin/bash

PKG_NAME="osrm_api"
SPEC_FILE="osrm-openapi.yaml"

REPO_USER="1papaya"
REPO_ID="osrm-openapi"

if [ -d "${REPO_ID}" ]; then
	echo "Refreshing repo ${REPO_ID}"
	git -C "${REPO_ID}" pull
else
	git clone "https://github.com/${REPO_USER}/${REPO_ID}.git"
fi

openapi-generator generate \
                  --package-name "${PKG_NAME}" \
                  --input-spec "${REPO_ID}/${SPEC_FILE}" \
                  --generator-name python \
                  --output .
