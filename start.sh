#!/bin/bash

set -e

# Load environment variables
if [ -f config/settings/.env ]; then
  echo "Loading environment from config/settings/.env"
  set -a
  source config/settings/.env
  set +a
fi

# Apply database migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "========== Starting Tunnels =========="

# Start jprq tunnel
if [ -n "$JPRQ_AUTH_KEY" ]; then
  echo "Authenticating jprq..."
  jprq auth "$JPRQ_AUTH_KEY"

  echo "Starting jprq tunnel on port 1028..."
  jprq http 1028 -s "$JPRQ_URL" > jprq.log 2>&1 &
  sleep 2
  JPRQ_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.jprq\.site' jprq.log | head -n1)
fi

# Show tunnel URLs
echo ""
echo "========== Public URLs =========="
[ -n "$JPRQ_URL" ] && echo "🌀 jprq  → $JPRQ_URL"
echo "================================="

# Start the Uvicorn ASGI server
echo ""
echo "Starting Uvicorn ASGI server..."
uvicorn config.asgi:application --host 0.0.0.0 --port 1028 --reload
