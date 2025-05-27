import argparse
import os
from crew import RichardsCrew


def run_crew(transcription: str, output_path: str, output_filename: str):
    inputs = {
        'transcription': transcription,
        'output_path': output_path,
        'output_filename': output_filename,
    }

    crew = RichardsCrew()

    crew.crew().kickoff(inputs=inputs)


def main():
    parser = argparse.ArgumentParser(description='Richards Crew - Documentation Generation Tool')
    parser.add_argument('file', help='Path to the transcription file')

    args = parser.parse_args()

    if not args.file:
        print("Error: No file provided. Please specify a transcription file.")
        return

    with open(args.file, "r", encoding='utf-8') as file:
        run_crew(
            transcription=file.read(),
            output_path=f"{os.getcwd()}/output",
            output_filename=f"{file.name.split('.')[0].upper()}_OUTPUT.md")


if __name__ == "__main__":
    main()
