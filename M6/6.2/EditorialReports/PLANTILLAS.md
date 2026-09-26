# Plantillas de estilo del proyecto

`resources/styles/EditorialStyles.jrtx` centraliza siete estilos reutilizables.

El informe importa la plantilla con:

```xml
<template><![CDATA["resources/styles/EditorialStyles.jrtx"]]></template>
```

La plantilla usa el namespace oficial de JasperReports para `.jrtx` y tipografía DejaVu Sans. Los estilos externos se aplican al título principal, cabecera de grupos, tabla y crosstab; los estilos locales heredados siguen disponibles para el resto del informe.
