# GO1 `/scan` en ROS2

Esta guia deja accesibles los topics ROS1 del NX `192.168.123.15` en tu ROS2 Humble local usando `ros1_bridge` dentro de Docker. El ejemplo principal sigue siendo `/scan`.

El montaje final queda asi:

- Raspberry: enruta entre `192.168.12.0/24` y `192.168.123.0/24`
- NX `192.168.123.15`: publica `/scan` en ROS1
- Portatil Ubuntu 22.04: levanta un bridge ROS1 -> ROS2 y consume topics como `/scan` desde ROS2

Dentro del contenedor se usa `ROS 1 Noetic + ROS 2 Foxy` sobre `Ubuntu 20.04`, porque esa combinacion si tiene paquetes binarios de `ros1_bridge`. El host puede seguir usando `ROS 2 Humble`.

El script principal de bridge publica todos los topics ROS1 disponibles mediante `dynamic_bridge --bridge-all-1to2-topics`.

## Configuracion final

### Raspberry

Hay que dejar activo el reenvio IPv4 de forma persistente:

```bash
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-ipforward.conf
sudo sysctl --system
```

Comprobacion:

```bash
sysctl net.ipv4.ip_forward
```

Salida esperada:

```bash
net.ipv4.ip_forward = 1
```

### NX `192.168.123.15`

Hay que dejar persistente la ruta de vuelta hacia la red WiFi de la Raspberry, `192.168.12.0/24`, via `192.168.123.161`.

La opcion recomendada es un servicio `systemd`.

Archivo `/etc/systemd/system/unitree-static-route.service`:

```ini
[Unit]
Description=Static route to Raspberry WiFi subnet
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
ExecStart=/sbin/ip route add 192.168.12.0/24 via 192.168.123.161
ExecStop=/sbin/ip route del 192.168.12.0/24 via 192.168.123.161
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Activacion:

```bash
sudo systemctl daemon-reload
sudo systemctl enable unitree-static-route.service
sudo systemctl start unitree-static-route.service
```

Comprobacion:

```bash
ip route | grep 192.168.12.0
```

Salida esperada:

```bash
192.168.12.0/24 via 192.168.123.161 dev eth0
```

### Portatil

En el portatil la ruta hacia `192.168.123.0/24` puede perderse tras reinicio o reconexion WiFi si no la dejas persistente en NetworkManager. Cuando haga falta, vuelve a crearla:

```bash
sudo ip route add 192.168.123.0/24 via 192.168.12.1
```

Comprobaciones rapidas:

```bash
ip route | grep 192.168.123.0
ping 192.168.123.15
```

Tu entorno ROS2 local debe usar:

```bash
export ROS_DOMAIN_ID=42
export ROS_LOCALHOST_ONLY=0
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

Tambien puedes dejarlo preparado con:

```bash
./docker/setup_ros2_go1.sh
```

## Arranque normal

### Terminal 1: bridge ROS1 -> ROS2

Desde `/home/bee/gral-iiriondo/unitree_ws`:

```bash
./docker/run_ros1_bridge_go1.sh
```

Notas:

- El script intenta usar `docker` y, si no tiene permisos, cae automaticamente a `sudo docker`
- Detecta la IP local del portatil hacia la Raspberry
- Fuerza `CycloneDDS` a usar `wlo1`
- Publica todos los topics ROS1 disponibles

Log util esperado:

```text
created 1to2 bridge for topic '/scan' with ROS 1 type 'sensor_msgs/LaserScan' and ROS 2 type 'sensor_msgs/msg/LaserScan'
[INFO] ... Passing message from ROS 1 sensor_msgs/LaserScan to ROS 2 sensor_msgs/msg/LaserScan
```

### Terminal 2: consumir `/scan` en ROS2

```bash
./docker/setup_ros2_go1.sh
ros2 topic list
ros2 topic echo /scan sensor_msgs/msg/LaserScan --qos-reliability best_effort
```

Notas:

- `ros2 topic list` puede no mostrar `/scan` hasta que exista un suscriptor ROS2 real
- `ros2 topic echo /scan sensor_msgs/msg/LaserScan --qos-reliability best_effort` suele disparar la creacion del bridge para ese topic

Comandos utiles:

```bash
ros2 topic info /scan -v
ros2 topic hz /scan
```

### Terminal opcional: verificar el bridge

Si quieres confirmar que el contenedor sigue vivo y que el bridge va creando topics:

```bash
sudo docker ps
```

## Comprobacion base de ROS1

Si algo falla, primero verifica el lado ROS1 desde el portatil:

```bash
sudo docker run --rm -it --net=host \
  --add-host nx:192.168.123.15 \
  -e ROS_MASTER_URI=http://192.168.123.15:11311 \
  -e ROS_IP=192.168.12.191 \
  osrf/ros:noetic-desktop-full \
  bash -lc 'source /opt/ros/noetic/setup.bash && rostopic list && rostopic echo /scan'
```

Si esta prueba funciona, la red y ROS1 estan bien.

## Frecuencia observada

Mediciones realizadas:

- ROS1 directo: `/scan` estable a unas `10 Hz`
- ROS2 tras el bridge: alrededor de `7-8 Hz`

Esto indica:

- el lidar y el topic ROS1 del robot estan bien
- hay algo de jitter o perdida al pasar por bridge + DDS + CLI ROS2

Para uso normal de visualizacion o consumo de datos, esa tasa suele ser valida.

## Si reinicias todo

Despues de reiniciar robot o portatil, lo normal es:

- Raspberry: no tocar nada si el `sysctl` persistente ya esta creado
- NX: no tocar nada si el servicio `unitree-static-route.service` esta habilitado
- Portatil: puede que tengas que volver a añadir la ruta a `192.168.123.0/24` si no la has dejado persistente

Secuencia minima de comprobacion:

```bash
ip route | grep 192.168.123.0
ping 192.168.123.15
```

Si eso responde, ya puedes lanzar el bridge.

## Archivos de este repo

- Script de arranque del bridge: `/home/bee/gral-iiriondo/unitree_ws/docker/run_ros1_bridge_go1.sh`
- Script para preparar ROS2 local: `/home/bee/gral-iiriondo/unitree_ws/docker/setup_ros2_go1.sh`
- Script de pruebas centrado en `/scan`: `/home/bee/gral-iiriondo/unitree_ws/docker/run_ros1_bridge_go1_scan.sh`
- Imagen Docker: `/home/bee/gral-iiriondo/unitree_ws/docker/ros1_bridge_go1.Dockerfile`

## Notas

- `ROS_DOMAIN_ID` debe estar entre `0` y `232`
- En este setup se usa `42`
- `ROS1 Noetic` esta EOL desde mayo de 2025
- En Ubuntu 22.04, usar `ros1_bridge` nativamente con ROS1 no es la via simple; por eso aqui se usa un contenedor aislado
