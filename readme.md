
```markdown
# CMACameraStreamer - Transmisión de Cámara CMA en Tiempo Real

Esta librería permite transmitir frames de una cámara en tiempo real mediante WebSocket, detectando movimiento y enviando los datos de los frames a un servidor específico. Los datos son enviados en forma de imágenes JPEG comprimidas, y el comportamiento de transmisión se ajusta según la calidad de la imagen seleccionada.

## Características

- **Conexión WebSocket**: Se conecta a un servidor WebSocket para la transmisión de frames.
- **Detección de Movimiento**: Solo transmite imágenes cuando detecta movimiento en la cámara.
- **Calidad Ajustable**: Puedes elegir entre tres niveles de calidad de transmisión ("low", "medium", "high") que afectan la resolución y la frecuencia de envío de los frames.
- **Recuperación Automática**: Si la conexión se pierde, la librería intentará reconectarse automáticamente.

## Instalación

1. Instalar las dependencias necesarias:
   ```bash
   pip install python-socketio opencv-python
   ```

2. Si no tienes instalado `opencv-python`, puedes instalarlo usando:
   ```bash
   pip install opencv-python
   ```

## Uso

1. Importa y crea una instancia de la clase `CMACameraStreamer`:

   ```python
   from CMACameraStreamer import CMACameraStreamer

   server = CMACameraStreamer(
       server_url='ws://www.cmasystems.com.mx/',
       group_name='1733252767654',
       quality='medium'  # Opciones: "low", "medium", "high"
   )
   server.connect_and_stream()
   ```

2. La clase `CMACameraStreamer` se conecta a un servidor WebSocket y comienza a transmitir frames de la cámara con el nivel de calidad seleccionado.

## Métodos

### `__init__(self, server_url, group_name, quality="high")`
Inicializa la clase `CMACameraStreamer` para transmitir datos desde la cámara.

- **server_url** (str): URL del servidor WebSocket.
- **group_name** (str): Nombre del grupo donde se enviarán los frames.
- **quality** (str): Nivel de calidad de la imagen ("low", "medium", "high").

### `_set_quality(self, quality)`
Define la resolución y el intervalo de envío según el nivel de calidad seleccionado.

- **quality** (str): Nivel de calidad ("low", "medium", "high").
- **retorna**: Diccionario con la resolución y el intervalo entre frames.

### `_on_connect(self)`
Se llama cuando se establece la conexión con el servidor.

### `_on_disconnect(self)`
Se llama cuando se pierde la conexión con el servidor.

### `_on_message(self, data)`
Recibe y maneja mensajes del servidor.

### `_gen_frames(self)`
Genera y envía frames de la cámara. Si se detecta movimiento, se transmite el frame a través de WebSocket.

### `connect_and_stream(self)`
Intenta establecer la conexión con el servidor y comienza a transmitir frames de la cámara.

## Ejemplo de Uso

El siguiente ejemplo muestra cómo crear una instancia de la clase `CMACameraStreamer`, conectarse a un servidor WebSocket y comenzar la transmisión de frames:

```python
server = CMACameraStreamer(
    server_url='ws://www.cmasystems.com.mx/',
    group_name='1733252767654',
    quality='medium'  # Opciones: "low", "medium", "high"
)
server.connect_and_stream()
```

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna idea o encuentras un error, abre un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
```

Este README proporciona detalles sobre la instalación, uso, métodos y cómo integrar la librería en un proyecto para realizar transmisión en tiempo real desde una cámara con detección de movimiento.