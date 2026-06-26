# Pull UV Binary
FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:latest AS uv_bin

# Pull base image
FROM --platform=linux/arm64 python:3.10-slim-bullseye

# Set Environment Variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set Working Directory
WORKDIR /bookstore

# Set Injection
COPY --from=uv_bin /uv /usr/local/bin/uv

# Set Dependency Caching
COPY pyproject.toml uv.lock /bookstore/
RUN uv sync --frozen --no-dev 

# Copy Source Code
COPY . .
