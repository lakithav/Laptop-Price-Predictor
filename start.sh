#!/bin/bash
cd website
gunicorn app:app --bind 0.0.0.0:$PORT
