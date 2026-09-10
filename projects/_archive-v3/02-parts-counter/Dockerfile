# syntax=docker/dockerfile:1
# projects/02-parts-counter/Dockerfile
#
# The boundary, as a stateless container. Not the agent: the agent needs a provider key and a
# person to talk to, and this project's deployable unit is the thing that owns the data.
#
# Nothing secret appears in this file, and that is a property to check rather than to intend —
# `docker history` prints every ENV and every build argument, so a secret written here is a secret
# published with the image.
#
# Verified against the sources listed in day 8 hub §9 on 2026-09-10. The build itself has NOT been
# run on the authoring machine — there is no container runtime installed on it — so every command
# in the day that would produce a transcript is marked TODO(me) rather than shown with an invented
# one.

# ── stage 1: build the environment ────────────────────────────────────────────────────────────
# `python:3.12-slim` resolved to `3.12.14-slim-trixie` on 2026-09-10 — Debian 13, CPython 3.12.14.
# That is NOT the version `.python-version` pins, and the difference matters below.
FROM python:3.12-slim AS builder

# uv is copied in from its own published image rather than installed with a script, so the build
# has no network dependency on an installer and the version is a tag you can read. Pinned to the
# version this project's SETUP.md was verified with; `:latest` here would make two builds a week
# apart use different resolvers.
COPY --from=ghcr.io/astral-sh/uv:0.12.3 /uv /uvx /bin/

# Copying rather than hardlinking, because the cache mount below and the target live on different
# filesystems and uv warns about it on every layer otherwise.
ENV UV_LINK_MODE=copy
# Compile to bytecode at build time: it costs image size once and saves it on every start.
ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

# `.python-version` pins 3.12.12 and this base image ships 3.12.14. uv is deliberately left free
# to download the pinned interpreter, which is the opposite of the usual `UV_PYTHON_DOWNLOADS=0`
# advice — because with that variable set, uv uses the image's 3.12.14, and `run.py check`'s
# `interpreter` check goes red inside the container while staying green on the laptop. A pin that
# the deployment does not honour is not a pin.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=.python-version,target=.python-version \
    uv python install

# Dependencies first, project second: the dependencies change rarely and the source changes every
# day, so this ordering is what makes the expensive layer cacheable. `--locked` asserts the
# lockfile already answers pyproject and fails if it does not; `--frozen` would install from a
# lockfile that no longer matches and say nothing.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable --no-dev

COPY . /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable --no-dev

# ── stage 2: the image that ships ─────────────────────────────────────────────────────────────
FROM python:3.12-slim

# A system user with a real home directory. `--system` alone creates no home, and a process whose
# HOME points nowhere fails in ways that name the wrong thing.
RUN groupadd --system --gid 10001 app \
 && useradd --system --uid 10001 --gid app --create-home --home-dir /home/app \
            --shell /usr/sbin/nologin app

WORKDIR /app

# `--chown` is not decoration. Without it these files arrive owned by root, and the very first
# thing the boundary does — write a ticket back to its data file — fails with a permission error
# that reads like a bug in the store.
COPY --from=builder --chown=app:app /app /app

# The interpreter uv downloaded in the builder stage, so the pinned version is the one that runs.
COPY --from=builder --chown=app:app /root/.local/share/uv/python /home/app/.local/share/uv/python

ENV PATH="/app/.venv/bin:$PATH"

# Configuration, not secrets. Every one of these has a safe default in the code and every one of
# them is visible in `docker history` — which is exactly why the API key is not among them.
#
# The bind must be stated here and read at construction. The SDK's own FASTMCP_HOST is ignored:
# FastMCP passes host= into its settings explicitly and an init argument outranks the environment,
# so a container that sets FASTMCP_HOST=0.0.0.0 listens on loopback and nothing says so.
ENV PARTS_MCP_HOST=0.0.0.0 \
    PARTS_MCP_PORT=8090 \
    PARTS_MCP_ALLOWED_HOSTS="127.0.0.1:8090,localhost:8090,parts-mcp:8090"

EXPOSE 8090

USER app

# `python:3.12-slim` has no curl, so a `curl -f` health check exits 127 and the container is
# permanently unhealthy while being perfectly well. This asks the boundary the only question worth
# asking — *can you still list your tools* — and sends the Host header the allowlist above expects.
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import json,urllib.request as u; \
req=u.Request('http://127.0.0.1:8090/mcp', \
 data=json.dumps({'jsonrpc':'2.0','id':1,'method':'tools/list'}).encode(), \
 headers={'Content-Type':'application/json','Accept':'application/json, text/event-stream', \
          'Host':'127.0.0.1:8090'}); \
u.urlopen(req, timeout=4).read()" || exit 1

CMD ["python", "run.py", "mcp", "--http"]
