from pathlib import Path
import subprocess
import sys
import requests
import json

# API URL to fetch records
API_URL = "https://osdg.iiit.ac.in/codegolf/api/pending_repos"

# Path to the shell script that runs Docker
RUN_SCRIPT = "./run.sh"


def fetch_records():
    """Fetches evaluation records from the API."""
    try:
        response = requests.get(API_URL, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching records: {e}")
        return None


def run_evaluator(repo: Path):
    """Runs the evaluator using the shell script."""
    try:
        result = subprocess.run(
            [RUN_SCRIPT, str(repo)], capture_output=True, text=True, timeout=60
        )

        if result.returncode == 0:
            ret = json.loads(result.stdout)  # Parse JSON output
            for r in ret:
                r["repo_name"] = repo.name
                r["verification"] = r.pop("passed")

            return ret
        else:
            print("Evaluator failed:", result.stderr)
            return None
    except subprocess.TimeoutExpired:
        print("Evaluator timed out!")
        return None


def main(submissions_dir: Path):
    records = fetch_records()
    if not records:
        print("No records fetched. Exiting.")
        return

    batch = []
    for record in records:
        results = run_evaluator(submissions_dir / record)
        if results:
            for res in results:
                res.pop("detail")
            batch.extend(results)

    return batch


if __name__ == "__main__":
    print(json.dumps(main(Path(sys.argv[1]))))
