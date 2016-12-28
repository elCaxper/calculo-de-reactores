# Aplicación gráfica para el cálculo de reactores químicos
Permite calcular reactores químicos discontinuos, continuos y de lecho fijo. También permite optimizar la conversión.

## Módulos necesarios:
1. Para la visualización de los datos *PyQtGraph*
2. Para el cálculo de los resultados *Scipy Library*
3. Para la parte gráfica *PySide*

## Reactores discontinuos (Batch Reactor)
Se puede calcular el tiempo y temperatura para una conversión determinada. El cálculo se puede realizar para distintos órdenes de reacción.

### Reactores isotermos 
Los parámetros usados son: 
1. Temperatura inicial.
2. Concentración inicial.
3. Energía de activación.
4. Constante k~o.

### Reactores adiabático 
Los parámetros usados son: 
1. Temperatura inicial
2. Concentración inicial
3. Energía de activación
4. Constante k~o
5. Calor de reacción.
6. Peso molecular.
7. Densidad de la mezcla.
8. Tipo de reacción (exotérmico o endotérmico)

### Reactores no isotermo y no adiabático 
Los parámetros usados son: 
1. Temperatura inicial
2. Concentración inicial
3. Energía de activación
4. Constante k~o
5. Calor de reacción.
6. Peso molecular.
7. Calor específico
8. Densidad de la mezcla.
9. Coeficiente de transmisión de calor.
10. Area de transmisión de calor
11. Temperatura del intercambiador de calor.
12. Tipo de reacción (exotérmico o endotérmico)


