import hashlib
import subprocess
import sys
import json
from pathlib import Path

base_dir = Path(__file__).parent.resolve()
testcases_dir = base_dir / "testcases"


def get_file_hash(submission_file):
    try:
        with open(submission_file, mode="r", encoding="utf-8") as file:
            content = file.read()
    except (FileNotFoundError, PermissionError, ValueError, OSError) as e:
        content = ""

    return hashlib.sha1(content.encode()).hexdigest()


def run_with_timeout(command, input_data, time_limit=1):
    try:
        process = subprocess.run(
            command,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=time_limit,
        )
        return process.stdout.strip(), process.stderr.strip()
    except subprocess.TimeoutExpired:
        return None, None


def evaluate_testcases(repo: Path):
    sources = repo / "codegolf"

    results = []
    for program_path in sorted(sources.glob("*.py")):
        problem_name = program_path.stem
        try:
            problem_id = int(problem_name.lstrip("q"))
        except ValueError:
            continue

        for input_file in sorted((testcases_dir / problem_name).glob("*.in")):
            output_file = input_file.with_suffix(".out")
            with open(input_file, "r") as f:
                input_data = f.read()
            with open(output_file, "r") as f:
                expected_output = f.read().strip()

            result, err = run_with_timeout([sys.executable, program_path], input_data)

            if result != expected_output:
                results.append(
                    {
                        "problem_id": problem_id,
                        "passed": False,
                        "detail": (
                            f"Failed with error for testcase at {input_file}"
                            if err
                            else (
                                f"Time limit exceeded for testcase at {input_file}"
                                if result is None
                                else f"Failed testcase at {input_file} (expected output matching {output_file})"
                            )
                        ),
                        "code_hash": get_file_hash(program_path),
                    }
                )
                break
        else:
            results.append(
                {
                    "problem_id": problem_id,
                    "passed": True,
                    "detail": f"All testcases passed!",
                    "code_hash": get_file_hash(program_path),
                }
            )

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tester.py <path to your repo - top level dir>")
        sys.exit(1)

    try:
        repo = Path(sys.argv[1]).resolve(strict=True)
    except FileNotFoundError:
        print("Error: First argument must be a valid path.")
        print("Usage: python3 tester.py <path to your repo (top level dir)>")
        sys.exit(1)

    evaluate_testcases(repo)
