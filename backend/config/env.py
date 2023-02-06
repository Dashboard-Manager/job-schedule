from pathlib import Path

import environ

env = environ.Env()

BACKEND_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = BACKEND_DIR / "apps"
ENV_DIR = BACKEND_DIR.parent / ".envs"
