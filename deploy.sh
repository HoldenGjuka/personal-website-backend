echo "Activating Python environment..."
source ../bin/activate

echo "Deploying backend server..."
python manage.py runserver 127.0.0.1:7000

echo "Server deployed!"