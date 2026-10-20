import logging
from pathlib import Path
LOG_DIR=Path(__file__).resolve().parent /"logs"
LOG_DIR.mkdir(exist_ok=True)

logger=logging.getLogger("rad_python")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter=logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    arquivo=logging.FileHandler(
        LOG_DIR / "app.log",
        encoding="utf-8",
    )
    arquivo.setFormatter(formatter)

    console=logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(arquivo)
    logger.addHandler(console)
