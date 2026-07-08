import subprocess
import json
from concurrent.futures import ThreadPoolExecutor

def run(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')

print("Fetching releases...")
releases_json = run('gh release list --repo UniverseKing4/AI-Vision -L 1000 --json tagName')
releases = [r['tagName'] for r in json.loads(releases_json)]
print(f"Found {len(releases)} releases.")

def delete_release(tag):
    print(f"Deleting {tag}")
    subprocess.run(f'gh release delete "{tag}" -y --cleanup-tag --repo UniverseKing4/AI-Vision', shell=True)

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(delete_release, releases)

print("Fetching runs...")
runs_json = run('gh run list --repo UniverseKing4/AI-Vision -L 1000 --json databaseId')
runs = [r['databaseId'] for r in json.loads(runs_json)]
print(f"Found {len(runs)} runs.")

def delete_run(run_id):
    print(f"Deleting run {run_id}")
    subprocess.run(f'gh run delete {run_id} --repo UniverseKing4/AI-Vision', shell=True)

with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(delete_run, runs)

print("Done!")
