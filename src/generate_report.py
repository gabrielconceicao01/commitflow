"""Gera um relatório JSON das verificações do CommitFlow."""

import json
import platform
from datetime import UTC, datetime
from pathlib import Path

from src.monitor import verificar_arquivos

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "reports" / "daily_report.json"


def main() -> None:
    """Verifica arquivos e gera um relatório JSON."""
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    arquivos = [
        "README.md",
        ".gitignore",
        "requirements.txt",
        "src/monitor.py",
        "src/generate_report.py",
        "tests/test_monitor.py",
        ".github/workflows/daily.yml",
    ]

    monitoramento = verificar_arquivos(arquivos)

    relatorio = {
        "projeto": "CommitFlow",
        "gerado_em": datetime.now(UTC).isoformat(),
        "ambiente": {
            "python": platform.python_version(),
            "sistema": platform.system(),
        },
        "monitoramento": monitoramento,
    }

    REPORT.write_text(
        json.dumps(relatorio, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(f"Relatório gerado: {REPORT}")
    print(json.dumps(relatorio, indent=2, ensure_ascii=False))

    if not monitoramento["sucesso"]:
        raise SystemExit("Existem arquivos essenciais ausentes.")


if __name__ == "__main__":
    main()
