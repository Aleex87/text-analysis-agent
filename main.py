from agent import TextAnalystAgent
from util.pretty_print import print_welcome, get_user_input
import os


DATA_FOLDER = "data"


def list_text_files() -> list[str]:
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER, exist_ok=True)
        return []

    files = []
    for name in os.listdir(DATA_FOLDER):
        path = os.path.join(DATA_FOLDER, name)
        if os.path.isfile(path) and name.lower().endswith(".txt"):
            files.append(name)

    return sorted(files)


def load_text_from_file(filename: str) -> str:
    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"File '{filename}' not found in '{DATA_FOLDER}/'"
        )

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def choose_file() -> str:
    print("Please select which file you want to analyze.")
    print(
        "If you want to add a new file, drag and drop it into the "
        "'data/' folder of this project, then type the correct file name.\n"
    )

    while True:
        files = list_text_files()

        if files:
            print("Available files:")
            for file_name in files:
                print(f"- {file_name}")
            print()
        else:
            print("No .txt files found in the 'data/' folder.\n")

        filename = input("File name (or type exit): ").strip()

        if filename.lower() == "exit":
            return ""

        if not filename:
            print("Please enter a file name.\n")
            continue

        if filename not in files:
            print(
                f"File '{filename}' is not available in '{DATA_FOLDER}/'. "
                "Please check the name and try again.\n"
            )
            continue

        return filename


def main() -> None:
    agent = TextAnalystAgent()

    print_welcome(
        title="Text Analyst Agent",
        description="Analyze and explore a text through conversation.",
        version="0.1.0",
    )

    filename = choose_file()
    if not filename:
        return

    try:
        text = load_text_from_file(filename)
    except Exception as exc:
        print(f"Error reading file: {exc}")
        return

    if len(text.split()) < 5:
        print("The selected file is too short. Please use a longer text.")
        return

    agent.set_text(text)

    print(f"\nLoaded file: {filename}")
    print("You can now ask questions about the text.")
    print("Commands: reset, exit\n")

    while True:
        user_input = get_user_input("Ask about the text")

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        if user_input.lower() == "reset":
            agent.reset()
            agent.set_text(text)
            print("Memory cleared. The source text is still loaded.\n")
            continue

        try:
            answer = agent.chat(user_input)
            print(answer)
            print()
        except Exception as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
    