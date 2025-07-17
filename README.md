# LAB_LokiBot
Exclusivamente educativo y académico.

# LokiBot - Características Implementadas

## 🚀 Nuevas Características Añadidas

### 1. **Exfiltración de Sistema** ✅
- **Información recolectada:**
  - Nombre de usuario actual
  - Hostname del sistema
  - Sistema operativo y versión
  - Arquitectura del procesador
  - Versión de Python
  - Directorio de trabajo actual
  - Variables de entorno del sistema

### 2. **Persistencia Simulada** ✅
- **Funcionalidades:**
  - Crea archivo de configuración en `%APPDATA%\Roaming\sistema_update.json`
  - Intenta modificar el registro de Windows para arranque automático
  - Registra estado de "instalación" del malware
  - Simula reinicio y reactivación del agente

### 3. **Robo de Criptomonedas** ✅
- **Wallets detectados:**
  - Exodus Wallet
  - Electrum
  - Bitcoin Core
  - Ethereum Keystore
  - Coinbase
  - MetaMask
- **Información capturada:**
  - Rutas de archivos de wallets
  - Tamaño de archivos
  - Estado de existencia

### 4. **Verificación de Sistema Objetivo** ✅
- **Detecta:**
  - Si el sistema es una máquina virtual
  - Presencia de software antivirus
  - Permisos de administrador
  - Compatibilidad del sistema

## 📊 Panel C2 Mejorado

### Dashboard Avanzado
- **Estadísticas en tiempo real:**
  - Total de víctimas
  - Credenciales válidas obtenidas
  - Wallets detectados
  - Targets válidos (no VM)

### Información Detallada por Target
- **Sistema:** Hostname, usuario, OS, arquitectura
- **Seguridad:** Estado de VM, permisos admin, antivirus
- **Wallets:** Lista completa de wallets detectados
- **Persistencia:** Estado de instalación y registro

### Nuevas Rutas API
- `/export` - Exporta todos los datos en JSON
- `/stats` - Estadísticas generales del C2

## 🔧 Uso

### Iniciar el Servidor C2
```bash
python servidor_c2.py
```
- Accede a `http://localhost:5000` para ver el dashboard

### Iniciar el Phishing
```bash
python login.py
```
- Accede a `http://localhost:8000` para ver la página de phishing

## 🎯 Características Técnicas

### Recolección de Datos
```python
# Ejemplo de datos recolectados
{
    "email": "victima@email.com",
    "password": "password123",
    "estado": "Correcto",
    "info_sistema": {
        "usuario": "JohnDoe",
        "hostname": "DESKTOP-ABC123",
        "sistema": "Windows",
        "arquitectura": "AMD64"
    },
    "wallets_encontrados": [
        {
            "wallet": "exodus.wallet",
            "ruta": "C:\\Users\\JohnDoe\\AppData\\Roaming\\Exodus\\exodus.wallet",
            "size": 1024
        }
    ],
    "sistema_objetivo": {
        "es_vm": false,
        "permisos_admin": true,
        "antivirus_detectado": ["windows defender"]
    },
    "persistencia": {
        "persistencia": "creada",
        "registro": "modificado"
    }
}
```

## ⚠️ Advertencias Importantes

1. **Uso Educativo:** Este código es solo para fines educativos y de investigación
2. **Entorno Controlado:** Usar únicamente en laboratorios controlados
3. **Permisos:** Requiere permisos de administrador para algunas funciones
4. **Registro:** Modifica el registro de Windows (funcionalidad de persistencia)

## 🔒 Seguridad

- El código incluye verificaciones de seguridad simuladas
- No explotación real de vulnerabilidades
- Funcionalidades de malware simuladas de forma segura
- Ideal para entrenamiento en ciberseguridad

## 📈 Estadísticas de Implementación

| Característica | Estado | Observación |
|---------------|---------|-------------|
| Exfiltración de Sistema | ✅ Completo | Información básica del sistema |
| Persistencia | ✅ Simulado | Registro y archivos de configuración |
| Robo de Criptomonedas | ✅ Simulado | Detección de wallets comunes |
| Verificación de Target | ✅ Funcional | Detección de VM y antivirus |

## 🚀 Próximas Mejoras

- [ ] Keylogger simulado
- [ ] Captura de pantalla
- [ ] Robo de cookies de navegador
- [ ] Comunicación cifrada con C2
- [ ] Sistema de comandos remotos
