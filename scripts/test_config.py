from src.core.config import load_config


def main():
    config = load_config()
    print("CONFIG LOADED:")
    print(config)


if __name__ == "__main__":
    main()