from pathlib import Path

import environ
import os

env = environ.Env()

BACKEND_DIR = Path(__file__).resolve(strict=True).parent.parent
APPS_DIR = BACKEND_DIR / "apps"
ENV_DIR = BACKEND_DIR.parent / ".envs"

environ.Env.read_env(os.path.join(ENV_DIR, "docker.env"))
environ.Env.read_env(os.path.join(ENV_DIR, "postgres.env"))
