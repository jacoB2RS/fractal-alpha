from pathlib import Path
import yaml


def load_config(path: str = "configs/default.yaml") -> dict:   # her setter vi forventning til at path parameteren skal være en string samt velger configs/test.yaml til standardverdi hvis ikke endret.
    config_path = Path(path)   # her gjør vi om path parametern som er configs/test.yaml til et path objekt, altså en filsti

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:  # her åpner vi innholdet i filen som filstien config_path går til
        return yaml.safe_load(f)
    


