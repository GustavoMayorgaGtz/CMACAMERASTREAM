from CMA_CAMERA_LIBRARIE import CMACameraStreamer
server = CMACameraStreamer(
    server_url='ws://www.cmasystems.com.mx/',
    group_name='<groupname>',
    quality='low'  # Opciones: "low", "medium", "high"
)
server.connect_and_stream()