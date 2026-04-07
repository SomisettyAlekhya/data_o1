
# OpenEnv Data Cleaning Environment (FULL PASS)

## Real-world Task
Simulates dataset cleaning:
- Missing values
- Duplicate removal
- Type conversion

## Actions
- fix_missing
- remove_duplicates
- convert_type

## Rewards
- +0.3 per correct step
- -0.1 invalid action
- 1.0 when fully cleaned

## Tasks
- Easy: missing values
- Medium: missing + duplicates
- Hard: full pipeline

## Run
docker build -t openenv .
docker run -p 8000:8000 openenv

## Inference
python inference.py
