# Contexto de adaptación del repo

Este repo fue tomado de una presentación/proyecto de otra persona y se está adaptando a un estilo propio, más profesional, claro y paso a paso.

## Objetivo general

- Convertir la presentación en una experiencia limpia y sobria.
- Sacar memes, GIFs, chistes y referencias al autor/repositorio anterior.
- Mantener el enfoque didáctico: una explicación progresiva para construir un ayudante de cocina con IA local.
- Preparar la presentación para que luego se puedan ir agregando capturas propias.

## Estado actual

- La presentación principal ya no es `slides.html`.
- El archivo activo ahora es `index.html`.
- URL local usada para probar:

```text
http://127.0.0.1:8010/index.html#0
```

## Cambios hechos

### Limpieza de contenido

- Se eliminaron los GIFs y memes de la presentación.
- Se reemplazaron frases informales/chistes por texto profesional.
- Se quitaron QR que apuntaban al autor/repositorio anterior.
- Se neutralizaron referencias al repo anterior en la presentación.
- Se limpió el README para que no arrastre enlaces al autor original.

### Archivos eliminados o marcados como borrados

Se sacaron assets humorísticos o innecesarios:

- `assets/agent86.gif`
- `assets/cat-type.gif`
- `assets/keanu-thanks.gif`
- `assets/zoolander.gif`
- assets animados del proyecto original reemplazados por videos/capturas propias.
- `assets/Buff-Doge-vs-Cheems.png`
- `assets/futurama-meme.jpg`
- `assets/it-works-on-my-machine.jpg`
- `assets/spiderman-meme.png`
- `assets/The_Square_Hole.jpg`
- archivos `*_Zone.Identifier`

### Interfaz de las diapositivas

- Se agregó navegación visual fija abajo:
  - flecha atrás
  - contador `1/30`
  - flecha adelante
- Las flechas se deshabilitan en la primera y última diapo.
- Se mantiene navegación por teclado:
  - derecha, espacio, PageDown o `n` para avanzar
  - izquierda, PageUp o `b` para retroceder
- Click en la diapositiva avanza, pero no si se hace click en enlaces, botones, videos o controles.

### Diseño visual

- Se mejoró la paleta para una estética clara y profesional:
  - fondo claro
  - acento bordó
  - acento secundario verde azulado
  - paneles blancos
  - código oscuro con borde lateral
- Se ajustaron sombras, espaciados, paneles, placeholders, código, imágenes y videos.

### Adaptación responsive

Se rearmó el CSS para que cada diapo entre dentro del 100% del ancho y 100% del alto visible.

Cambios importantes:

- `.slide` ocupa `100vw` y `100dvh`.
- El contenido tiene `max-height` calculado para respetar padding y controles.
- Imágenes y videos usan `object-fit: contain`.
- Se agregaron media queries para:
  - pantallas chicas / proyectores tipo `1366x768`
  - pantallas estándar tipo `1920x1080`
  - pantallas grandes tipo `3840x2160`
  - pantallas muy grandes tipo `5120x2880` o más
- Se agregó una función JS `fitActiveSlide()` que mide la diapo activa y reduce levemente la escala si algo se pasa del viewport.

## Validaciones hechas

Se validó en navegador interno con estos tamaños:

- `1366x768`
- `1920x1080`
- `3840x2160`
- `5120x2880`

Resultado:

- Las 30 diapositivas entran sin desbordar.
- En `1366x768`, algunas diapositivas se escalan levemente, con escala mínima aproximada `0.91`.
- En `3840x2160`, no hizo falta escalar: escala `1`.
- No quedaron QR.
- No quedaron referencias a autores, QR, repositorios anteriores o assets humorísticos del proyecto original.
- Las referencias locales a assets actuales existen.

## Archivos tocados

- `index.html`: presentación principal, estilos, navegación, responsive y ajuste automático.
- `README.md`: limpieza de referencias y tono.
- `main.py`: salida de consola más sobria.
- `pyproject.toml`: descripción más profesional.
- `slides.html`: reemplazado por `index.html`.

## Próximos pasos sugeridos

- Reemplazar `URL_DE_TU_REPOSITORIO` por el repo final propio.
- Reemplazar `URL_DEL_DATASET/recetas.json` por una fuente propia o local.
- Ir cambiando los placeholders por capturas reales propias.
- Revisar si el título “Agente de recomendaciones de cocina con IA local” se mantiene o si se adapta a otra identidad.
- Si se agregan nuevas capturas, verificar nuevamente en `1366x768`, `1920x1080` y `3840x2160`.

## Nota de continuidad

La conversación venía trabajando sobre `C:\00\agent-main`.

La presentación debe abrirse desde:

```text
C:\00\agent-main\index.html
```

O desde el servidor local:

```text
http://127.0.0.1:8010/index.html#0
```
