import os
import argparse
from dotenv import load_dotenv

from simmons.crew import SimonsCrew

load_dotenv()


def run_crew(topic: str, language: str, transcription: str, output_directory: str):

    inputs = {
        'topic': topic,
        'language': language,
        'transcription': transcription,
        'output_directory': output_directory,
    }

    crew = SimonsCrew()

    crew.crew().kickoff(inputs=inputs)


def main():
    parser = argparse.ArgumentParser(description='Simmons Crew - Documentation Generation Tool')
    parser.add_argument('-t', '--topic', type=str, help='Topic for the documentation generation')
    parser.add_argument('-f', '--file', type=str, help='Path to the transcription file')
    parser.add_argument('-l', '--language', type=str, default='en-US', help='Language for the transcription (default: en-US)')

    args = parser.parse_args()

    if not args.topic:
        parser.error("The --topic argument is required.")

    if not args.file:
        parser.error("The --file argument is required.")

    if not os.path.exists(args.file):
        parser.error(f"The file {args.file} does not exist.")

    output_directory = os.getenv('SIMMONS_OUTPUT_DIR', './simmons_output')

    with open(args.file, "r", encoding='utf-8') as file:
        run_crew(
            topic=args.topic,
            language=args.language,
            transcription=file.read(),
            output_directory=output_directory)


if __name__ == "__main__":
    main()
