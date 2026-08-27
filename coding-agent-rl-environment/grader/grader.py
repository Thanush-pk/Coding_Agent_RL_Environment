import subprocess
import sys


def run_tests():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "tests",
            "grader/hidden_tests",
            "-q",
        ],
        capture_output=True,
        text=True,
    )

    return result


def calculate_score(result):
    if result.returncode == 0:
        return 100

    return 0


def main():
    print("Running grader...")

    result = run_tests()

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    score = calculate_score(result)

    print(f"Score: {score}/100")

    sys.exit(0 if score == 100 else 1)


if __name__ == "__main__":
    main()