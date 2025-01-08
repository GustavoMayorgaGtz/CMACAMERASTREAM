# CMACameraStreamer

CMACameraStreamer es una librería que te permite transmitir el flujo de video de una cámara a través de WebSocket. Permite configurar la calidad de la transmisión (baja, media, alta) y ajusta la frecuencia de envío de los frames en función de la calidad seleccionada. Ideal para aplicaciones de monitoreo en tiempo real.

## Requisitos

- Python 3.x
- OpenCV
- `python-socketio`

## Instalación

Para instalar las dependencias necesarias, sigue estos pasos:

1. **Clona el repositorio** o descarga los archivos.

2. **Instala las dependencias**:

   Asegúrate de tener `pip` instalado en tu entorno de Python. Si no lo tienes, puedes instalarlo desde [aquí](https://pip.pypa.io/en/stable/).

   Luego, ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```bash
   pip install opencv-python python-socketio
   ```

   **Nota**: Si tienes problemas con la instalación de `opencv-python` en tu sistema, consulta [esta página de instalación](https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html) para más detalles sobre cómo instalar OpenCV en tu sistema operativo.

3. **Instalación de la librería**:

   Si estás utilizando esta librería como un paquete independiente, puedes instalarla ejecutando:

   ```bash
   pip install .
   ```

   Esto instalará la librería en tu entorno de Python.

## Uso

Aquí tienes un ejemplo de cómo utilizar la librería `CMACameraStreamer`:

```python
from cmacamera_streamer import CMACameraStreamer

# Inicializa el streamer con la URL del servidor WebSocket, el nombre del grupo y la calidad de transmisión
server = CMACameraStreamer(
    server_url='ws://www.cmasystems.com.mx/',
    group_name='1733252767654',
    quality='medium'  # Opciones: "low", "medium", "high"
)

# Conectar y empezar a transmitir el video
server.connect_and_stream()
```

## Contribución

Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
