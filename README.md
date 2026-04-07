title: Data Cleaning OpenEnv
emoji: 🧹
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: 2.13.0
python_version: '3.10'
app_file: app.py
pinned: false

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
