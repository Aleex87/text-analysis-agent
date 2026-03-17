from agent import TextAnalystAgent
from util.pretty_print import print_welcome, get_user_input
import os


DATA_FOLDER = "data"


def load_text_from_file(filename: str) -> str:
    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"File '{filename}' not found in '{DATA_FOLDER}/'")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def list_files():
    if not os.path.exists(DATA_FOLDER):
        return []
    return os.listdir(DATA_FOLDER)


def main() -> None:
    agent = TextAnalystAgent()

    print_welcome(
        title="Text Analyst Agent",
        description="Analyze and explore a text through conversation.",
        version="0.1.0",
    )

    print("Choose input type:")
    print("1 - Paste text")
    print("2 - Load from file\n")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            print("\nPaste your text (or type exit):\n")

            while True:
                text = input("> ")

                if text.lower() == "exit":
                    return

                if text.strip():
                    agent.set_text(text)
                    break
            break

        elif choice == "2":
            print("\nPlace your file inside the 'data/' folder.\n")

            files = list_files()
            if files:
                print("Available files:")
                for f in files:
                    print(f"- {f}")
                print()
            else:
                print("No files found in 'data/' folder.\n")

            print("Enter file name (example: article.txt) or type exit:\n")

            while True:
                filename = input("> ").strip()

                if filename.lower() == "exit":
                    return

                try:
                    text = load_text_from_file(filename)
                    agent.set_text(text)
                    print("\nFile loaded successfully.\n")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    print("Try again or type exit\n")
            break

        else:
            print("Invalid choice. Please type 1 or 2.\n")

    print("You can now ask questions about the text.")
    print("Commands: reset, exit\n")

    while True:
        user_input = get_user_input("Ask about the text")

        if not user_input:
            continue

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "reset":
            agent.reset()
            print("Memory cleared.\n")
            continue

        try:
            answer = agent.chat(user_input)
            print(answer)
            print()
        except Exception as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
    