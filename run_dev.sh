echo "Is debug turned on?"

echo "Activating environment..."
source ./../bin/activate

echo "Starting Development Server..."
python manage.py runserver 127.0.0.1:7000