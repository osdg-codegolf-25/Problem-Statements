#!/bin/bash
# first do:
# docker build -t evaluator .
docker run --rm --read-only \
    -v $(realpath testcases):/sandbox/testcases/:ro \
    -v $(realpath tester.py):/sandbox/tester.py:ro \
    -v $(realpath $1):/sandbox/repo:ro \
    --memory=128m --memory-swap=128m \
    --cpus="1" --cpu-shares=256 \
    --network=none \
    evaluator
