#!/bin/bash

python3 -m alembic upgrade head
python3 -m uvicorn src.main:app --reload
