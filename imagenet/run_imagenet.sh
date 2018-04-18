#!/bin/bash

set -ex

for f in ./data/*; do
  python classify_image.py --image_file="$f" > ./data/$(basename "$f").txt
done
