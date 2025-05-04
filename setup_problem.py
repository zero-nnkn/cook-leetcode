import argparse
import os


def create_problem_directory(plan: str, prob: str):
    folder_path = os.path.join(plan, prob)
    os.makedirs(folder_path, exist_ok=True)

    solution_path = os.path.join(folder_path, "solution.py")
    if not os.path.exists(solution_path):
        with open(solution_path, "w") as f:
            f.write("# Write your solution here\n")
        print(f"Created: {solution_path}")
    else:
        print(f"Already exists: {solution_path}")

def main():
    parser = argparse.ArgumentParser(description="Setup Leetcode problem folder.")
    parser.add_argument("--plan", type=str, required=True, help="Plan name (e.g., leetcode75)")
    parser.add_argument("--prob", type=str, required=True, help="Problem name (e.g., '11. Container With Most Water')")

    args = parser.parse_args()
    create_problem_directory(args.plan, args.prob)


if __name__ == "__main__":
    main()
