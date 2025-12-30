#!/bin/bash

echo "🚀 OREA85 Ultimate DDOS - Installer"
echo "================================="

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $python_version"

# Install requirements
echo "📦 Installing requirements..."
pip3 install -r requirements.txt

# Make scripts executable
echo "🔧 Making scripts executable..."
chmod +x basic_ddos.py
chmod +x advanced_ddos.py

echo "✅ Installation complete!"
echo ""
echo "🎯 Usage:"
echo "  python3 basic_ddos.py"
echo "  python3 advanced_ddos.py"
echo "  python3 auto_ddos.py"
echo ""
echo "💎 Created by OREA85"
echo "⚠️  Use only for educational purposes!"