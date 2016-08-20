#!/usr/bin/env bash
docker build -t security-flask .
docker run security-flask python -m unittest
