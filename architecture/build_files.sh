echo "Pip Güncelleniyor..."
pip install --upgrade pip

echo "Requirements kuruluyor..."

pip install -r requirements.txt

chmod +x /var/task/media
chmod +x media/

echo "Tamamlandı"
