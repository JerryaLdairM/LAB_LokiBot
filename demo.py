#!/usr/bin/env python3
"""
LokiBot - Script de Demostración
Ejecuta una demostración completa del sistema
"""

import subprocess
import time
import requests
import json
from pathlib import Path

def print_banner():
    banner = """
    ██╗      ██████╗ ██╗  ██╗██╗██████╗  ██████╗ ████████╗
    ██║     ██╔═══██╗██║ ██╔╝██║██╔══██╗██╔═══██╗╚══██╔══╝
    ██║     ██║   ██║█████╔╝ ██║██████╔╝██║   ██║   ██║   
    ██║     ██║   ██║██╔═██╗ ██║██╔══██╗██║   ██║   ██║   
    ███████╗╚██████╔╝██║  ██╗██║██████╔╝╚██████╔╝   ██║   
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝    ╚═╝   
    
    🔥 LokiBot - Demostración de Capacidades 🔥
    ⚠️  Solo para propósitos educativos ⚠️
    """
    print(banner)

def esperar_servidor(url, timeout=30):
    """Espera a que el servidor esté disponible"""
    print(f"[*] Esperando que el servidor esté disponible en {url}...")
    for i in range(timeout):
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                print(f"[+] Servidor disponible en {url}")
                return True
        except:
            time.sleep(1)
            if i % 5 == 0:
                print(f"[*] Esperando... ({i}/{timeout})")
    return False

def simular_victima(email, password):
    """Simula una víctima enviando credenciales"""
    print(f"[*] Simulando víctima: {email}")
    try:
        data = {
            'email': email,
            'password': password
        }
        response = requests.post('http://localhost:8000/', data=data)
        if response.status_code == 200:
            print(f"[+] Datos enviados exitosamente para {email}")
            return True
        else:
            print(f"[-] Error enviando datos para {email}: {response.status_code}")
            return False
    except Exception as e:
        print(f"[-] Error conectando al servidor de phishing: {e}")
        return False

def obtener_estadisticas():
    """Obtiene estadísticas del servidor C2"""
    try:
        response = requests.get('http://localhost:5000/stats')
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[-] Error obteniendo estadísticas: {response.status_code}")
            return None
    except Exception as e:
        print(f"[-] Error conectando al servidor C2: {e}")
        return None

def main():
    print_banner()
    
    print("\n=== DEMOSTRACIÓN LOKIBOT ===")
    print("[1] Iniciando servidores...")
    
    # Verificar si los servidores están ejecutándose
    c2_disponible = esperar_servidor('http://localhost:5000', 5)
    phishing_disponible = esperar_servidor('http://localhost:8000', 5)
    
    if not c2_disponible or not phishing_disponible:
        print("\n[!] Los servidores no están ejecutándose.")
        print("    Ejecuta primero:")
        print("    1. python servidor_c2.py")
        print("    2. python login.py")
        print("    Luego ejecuta este script nuevamente.")
        return
    
    print("\n[2] Simulando ataques de phishing...")
    
    # Simular diferentes víctimas
    victimas = [
        ('usuario@ejemplo.com', 'clave123'),      # Credenciales válidas
        ('admin@facebook.com', 'adminpass'),      # Credenciales válidas
        ('victima1@test.com', 'wrongpass'),       # Credenciales inválidas
        ('victima2@test.com', 'password123'),     # Credenciales inválidas
        ('target@empresa.com', 'qwerty'),         # Credenciales inválidas
    ]
    
    print(f"[*] Simulando {len(victimas)} víctimas...")
    
    for i, (email, password) in enumerate(victimas, 1):
        print(f"\n[{i}/{len(victimas)}] Atacando: {email}")
        if simular_victima(email, password):
            time.sleep(2)  # Esperar entre ataques
    
    print("\n[3] Recolectando resultados...")
    time.sleep(3)  # Esperar a que se procesen los datos
    
    # Obtener estadísticas
    stats = obtener_estadisticas()
    if stats:
        print(f"\n📊 ESTADÍSTICAS FINALES:")
        print(f"  Total de intentos: {stats['total_intentos']}")
        print(f"  Credenciales válidas: {stats['credenciales_validas']}")
        print(f"  Sistemas infectados: {stats['sistemas_infectados']}")
        print(f"  Wallets detectados: {stats['wallets_total']}")
        print(f"  Targets válidos (no VM): {stats['targets_no_vm']}")
        print(f"  Con permisos admin: {stats['con_permisos_admin']}")
    
    print("\n[4] Acceso al panel C2:")
    print("    🌐 Dashboard: http://localhost:5000")
    print("    📊 Estadísticas: http://localhost:5000/stats")
    print("    💾 Exportar datos: http://localhost:5000/export")
    
    print("\n[5] Archivos generados:")
    archivos = [
        'intentos.txt',
        Path.home() / 'AppData' / 'Roaming' / 'sistema_update.json'
    ]
    
    for archivo in archivos:
        if Path(archivo).exists():
            print(f"    ✅ {archivo}")
        else:
            print(f"    ❌ {archivo} (no encontrado)")
    
    print("\n🎯 DEMOSTRACIÓN COMPLETADA")
    print("   Revisa el dashboard en http://localhost:5000 para ver los resultados completos")

if __name__ == '__main__':
    main()
