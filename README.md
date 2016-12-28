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
4. Constante k<sub>o</sub>.

### Reactores adiabático 
Los parámetros usados son:  

1. Temperatura inicial.
2. Concentración inicial.
3. Energía de activación.
4. Constante k<sub>o</sub>.
5. Calor de reacción.
6. Peso molecular.
7. Densidad de la mezcla.
8. Tipo de reacción (exotérmico o endotérmico).

### Reactores no isotermo y no adiabático 
Los parámetros usados son:  

1. Temperatura inicial.
2. Concentración inicial.
3. Energía de activación.
4. Constante k<sub>o</sub>.
5. Calor de reacción.
6. Peso molecular.
7. Calor específico
8. Densidad de la mezcla.
9. Coeficiente de transmisión de calor.
10. Area de transmisión de calor.
11. Volumen del reactor.
12. Temperatura del intercambiador de calor.
13. Tipo de reacción (exotérmico o endotérmico).


### Optimización de reactores
A partir de ciertos parámetros se puede calcular la conversión optima y el tiempo óptimo de operación.  
Los parámetros usados son:  

1. Candida de moles a reaccionar.
2. Temperatura inicial.
3. Concentración inicial.
4. Energía de activación.
5. Constante k<sub>o</sub>.
6. Volumen del reactor.
7. Coste de la reacción.
8. Valor aumentado por mol transformado.

