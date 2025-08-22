# -------------------------
# 1) Builder stage
# -------------------------
FROM python:3.13-slim AS builder

WORKDIR /usr/src/app

# Install system deps only for building wheels
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl make gcc libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps (cached if requirements unchanged)
COPY requirements/ ./requirements/
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements/development.txt

# Install jprq (light binary, no system deps)
RUN curl -fsSL https://jprq.io/install.sh | bash


# -------------------------
# 2) Runtime stage
# -------------------------
FROM python:3.13-slim AS runtime

WORKDIR /usr/src/app

# Install minimal tools needed at runtime (make + sqlite3 CLI)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        make sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Copy jprq binary
COPY --from=builder /usr/local/bin/jprq /usr/local/bin/jprq

# Copy only project code
COPY . .

EXPOSE 1028

CMD ["bash", "start.sh"]
