#!/bin/bash

openapi-generator generate \
                  --package-name "osrm_api" \
                  --input-spec ./osrm-openapi.yaml \
                  --generator-name python \
                  --output ..
