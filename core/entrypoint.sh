#!/bin/sh
set -e
echo "Starting manage script";

python3 manage.py collectstatic --noinput

echo "Ending manage script"
exec "$@"
