#!/bin/sh

echo 'Starting build script'

echo 'Running migrations'
python3 manage.py migrate --noinput
if [ $? -ne 0 ]; then
  echo 'Migration failed'
  exit 1
fi

echo 'Collecting static files'
python3 manage.py collectstatic --noinput
if [ $? -ne 0 ]; then
  echo 'Collectstatic failed'
  exit 1
fi

echo 'Build script completed'