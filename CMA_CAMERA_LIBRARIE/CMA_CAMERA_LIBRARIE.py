import socketio
import time
import cv2

class CMACameraStreamer:
    def __init__(self, server_url, group_name, quality="high"):
        """
        Inicializa el streamer de cámara CMA.

        :param server_url: URL del servidor WebSocket.
        :param group_name: Nombre del grupo para el envío de datos.
        :param quality: Calidad de la imagen ("low", "medium", "high").
        """
        self.server_url = server_url
        self.group_name = group_name
        self.sio = socketio.Client()
        self.quality = self._set_quality(quality)

        # Configurar eventos del socket
        self.sio.on('connect', self._on_connect)
        self.sio.on('disconnect', self._on_disconnect)
        self.sio.on('sendMessageToGroup', self._on_message)

    def _set_quality(self, quality):
        """
        Define la resolución y el intervalo de envío según la calidad.

        :param quality: Calidad de la imagen ("low", "medium", "high").
        :return: Tupla con resolución y tiempo entre frames.
        """
        qualities = {
            "low": {"resolution": (320, 240), "frame_interval": 0.03},   # Mayor frecuencia (33 fps aprox.)
            "medium": {"resolution": (640, 480), "frame_interval": 0.1},  # Frecuencia media (10 fps)
            "high": {"resolution": (1920, 1080), "frame_interval": 0.5}  # Menor frecuencia (2 fps)
        }
        return qualities.get(quality, qualities["high"])

    def _on_connect(self):
        print("Conectado al servidor")

    def _on_disconnect(self):
        print("Desconectado del servidor")

    def _on_message(self, data):
        print("Mensaje recibido:", data)

    def _gen_frames(self):
        """Genera y envía frames de video detectando movimiento."""
        camera = cv2.VideoCapture(0)  # Inicializa la cámara
        resolution = self.quality["resolution"]
        frame_interval = self.quality["frame_interval"]

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

        if not camera.isOpened():
            print("Error al abrir la cámara")
            return

        ret, frame1 = camera.read()
        ret, frame2 = camera.read()

        while ret:
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            if contours:  # Si se detecta movimiento
                ret, buffer = cv2.imencode('.jpg', frame1)
                frame = buffer.tobytes()
                if self.sio.connected:
                    print("Movimiento detectado, enviando mensaje")
                    self.sio.emit('cameraStream', {'groupName': self.group_name, 'message': frame})

            frame1 = frame2
            ret, frame2 = camera.read()
            time.sleep(frame_interval)  # Pausa ajustada según la calidad

        camera.release()

    def connect_and_stream(self):
        """Establece la conexión y comienza a transmitir frames."""
        while True:
            try:
                print("Intentando conectar al servidor...")
                self.sio.connect(self.server_url)
                print("Conexión establecida")
                self._gen_frames()
            except socketio.exceptions.ConnectionError:
                print("Error de conexión. Reintentando en 5 segundos...")
                time.sleep(5)
            except Exception as e:
                print(f"Error inesperado: {e}")
                time.sleep(5)

# Ejemplo de uso:
# server = CMACameraStreamer(
#     server_url='ws://www.cmasystems.com.mx/',
#     group_name='1733252767654',
#     quality='medium'  # Opciones: "low", "medium", "high"
# )
# server.connect_and_stream()
