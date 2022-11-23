# Trazadomus 2.0
Sistema de trazabilidad de paquetes en el proceso de esterilización en la CEyE de los hospitales

## WebApp

### Bugs
- [ ] La actualización de las hojas de códigos crea nuevas hojas de códigos
- [ ] No evita duplicación de los nombres de las hojas de códigos

### Pruebas
- [ ] Crear usuario. Se crea un usario, verifica que no exista antes. Solicita datos del usuario. Asigna permisos y un grupo.
- [ ] Crea cliente. Un cliente contiene a uno o más usuarios. Un cliente tiene uno o mas sets o kits. Un cliente tiene uno o más esterilizadores.
- [ ] Crear sets. Un usuario administrador puede crear un set. Cada set esta asignado a un cliente. El set tiene una fecha de caducidad.
- [ ] Crear administrador. Un usuario adquiere permisos de escritura de la configuración de un cliente, lo que incluye: Crear otros usuarios. Crear sets. Consultar tablas y reportes.
- [ ] Crear esterilizador. Un esterilizador esta asociado a un cliente.

### TODO
- [ ] Interfaz adaptativa
- [ ] Configuración de candados en el flujo
  - [ ] Verificación de indicadores antes de enviar a destino
  - [ ] Verificación por paquetes o por lote al terminar un lote
- [ ] Tableros de información básica
- [ ] Niveles de acceso
- [ ] Descarga de las consultas en `.csv`

### Siguientes etapas
Recreación de etiquetas en la webapp

## Terminal de registro

### TODO
- [ ] Facilitar el clonado del sistema
- [ ] Script de configuracion inicial
- [ ] Activar modo kiosko
- [ ] Temporizador del tiempo abierto sin actividad > cierre de sesión del usuario a los 10 min
- [ ] Integración de botones de control de reTerminal
- [ ] Implementación de la función de apagado de la reTerminal

### Bugs
- [ ] Al entregar un paquete no emite ningúna advertencia si el paquete no fue verificado.

### Hardware

#### TODO
- [ ] Adapatación de fuente de poder
- [ ] Comunicación por GPIO al USB de la impresora
- [ ] Salida del puerto USB del scanner en la carcasa
- [ ] Emulación de los botones de la impresora
- [ ] Implementación de la función de apagado de la impresora
- [ ] Circuito de pruebas integrando las señales de USB, botones, LEDs y energía

### Carcasa
- [ ] Eliminación de curvas innecesarias
- [ ] Repanelizado de las partes

# Entrega Intellilab
Imagen para raspberry con script de inicialización
Zip de la webapp
Esquema de la base de datos


## ToDo
- [ ] Definir el hosting
- [ ] Requisitos del hosting


