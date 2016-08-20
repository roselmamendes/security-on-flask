#!/usr/bin/env bash
docker build -t security-flask .
docker run -p 5000:5000 -t security-flask python black_girls/black_girls.py
