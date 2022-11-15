echo "Activating Python environment..."
source ../bin/activate

echo "Deploying backend server..."
python manage.py runserver 0.0.0.0:8000

echo "Server deployed!"