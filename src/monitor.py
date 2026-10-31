"""Funções básicas de monitoramento do CommitFlow."""

from pathlib import Path


def verificar_arquivos(arquivos: list[str]) -> dict:
    """Verifica a existência de arquivos e retorna um resumo."""
    resultados = []

    for nome in arquivos:
        existe = Path(nome).is_file()

        resultados.append({
            "arquivo": nome,
            "existe": existe,
            "status": "ok" if existe else "ausente",
        })

    total = len(resultados)
    encontrados = sum(item["existe"] for item in resultados)

    return {
        "total": total,
        "encontrados": encontrados,
        "ausentes": total - encontrados,
        "sucesso": encontrados == total,
        "detalhes": resultados,
    }
