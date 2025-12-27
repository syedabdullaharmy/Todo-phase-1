"""Main Entry Point."""

from src.ui.cli import CLI

if __name__ == "__main__":
    try:
        app = CLI()
        app.run()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
