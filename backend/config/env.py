from pathlib import Path

import environ

# ENVIRONMENTS
env = environ.Env()

# PATHS
BACKEND_DIR = Path(__file__).resolve(strict=True).parent.parent  # /backend
PROJECT_DIR = BACKEND_DIR.parent  # /src
ENV_DIR = BACKEND_DIR.parent / ".envs"
