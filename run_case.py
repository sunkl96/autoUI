import sys
import subprocess

WIN = sys.platform.startswith('win')


def main():
    steps = [
        "venv\\Script\\activate" if WIN else "source venv/bin/activate",
        "pytest --alluredir allure-results --clean-alluredir",
        "allure generate allure-results -c -o allure-report",
        "allure open allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step if WIN else step, shell=True)


if __name__ == "__main__":
    main()