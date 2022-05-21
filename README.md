# Simulacion-y-estudio-de-conductas-criminales-en-una-sociedad-artificial

Introducción
El objetivo de este trabajo será simular una sociedad artificial donde se estudiará el
comportamiento de criminales, víctimas y policías. El estudio se centrará solamente en robos
urbanos, es decir, robos en calles con o sin violencia en los que un criminal consigue quitar a una
víctima algún objeto que portaba. Para ello utilizaremos el lenguaje de programación Python
que contiene librerías como mesa y networkx con las que implementaremos modelos basados
en agentes que serán la base de este trabajo.
Modelos ABM
Los modelos basados en agentes son un tipo de simulación computacional que nos permite
evaluar el comportamiento de dinámicas e interacciones entre diversos agentes. Estos modelos
son muy útiles para estudiar dinámicas que son difícilmente replicables en la realidad o que son
poco éticas, como es el caso de la criminología.
Antes de empezar a programar se necesita desarrollartres aspectos que generalmente son clave
en este tipo de estudios: los agentes, el entorno y las dinámicas.
Los agentes
Un agente se define como una entidad autónoma, heterogénea, aislada de los demás agentes,
con su propia carga identitaria; con la capacidad de interactuar con otros agentes y el entorno.
Para este estudio determinaremos tres tipos de agentes: criminales, víctimas y policías. Cada
uno tendrán sus patrones de conducta que explicare en más detalle en las dinámicas. En cuanto
al número de agentes que se crearán, irán determinadas por el tamaño del entorno intentando
crear una simulación lo más parecida posible a la realidad.
El entorno
El entorno irá evolucionando a lo largo del estudio, empezando por una cuadrícula de casillas
simple, donde los agentes se podrán mover en cada paso hacia una de las casillas contiguas y a
partir de ahí, se estudiará como afecta el entorno al comportamiento de los diferentes agentes
haciéndolo más complejo, hasta llegar, si es posible, a una recreación de algún lugar real con un
índice de delincuencia alto y en donde los agentes se podrán mover libremente por las calles
simuladas y donde incluso se podrá implementar un clima que determinará el número de
agentes por las calles. Para ello utilizaré datos de geolocalización LBSN extraídos de Foursquare
como utilizan varios estudios criminológicos que serán implementados en el código. En
cualquiera de los casos en el entorno habrá varios nodos de popularidad, donde se concentrarán
con más probabilidad los agentes y varios nodos de delincuencia, donde habrá más criminales.
Las dinámicas
Las dinámicas pueden ser divididas en dos clases, movimiento y comportamiento
El movimiento funcionará de la siguiente manera:
Cada una de las víctimas tendrá una posición inicial que podemos imaginar como su vivienda, y
durante la simulación ira a varios lugares más que previamente habremos determinado que
podríamos pensar como el trabajo, el super, banco etc. este es el movimiento típico de la
mayoría de personas a lo largo de un día, y el trayecto de nodo a nodo se realizara utilizando el
algoritmo de ruta más corta de Dijkstra. El movimiento de los delincuentes no se distingue
mucho del de una víctima cualquiera (Brantingham & Brantingham, 1993) por lo tanto los
criminales tendrán el mismo comportamiento en cuanto a la manera de moverse. Por último, el
movimiento de los policías vendrá determinado por información real de patrullas y sus
comportamientos para abarcar la mayor zona posible.
Comportamiento de los agentes:
Los criminales deberán escoger si cometen el crimen o no, siempre que tengan una víctima
cerca, esta decisión la tomarán en base a una función de beneficio-riesgo en la cual se evaluará
si es rentable realizar el crimen o no. El beneficio vendrá determinado por un parámetro
asignado a las víctimas que evaluará que tan deseable es una víctima para un delincuente, ya
sea por la manera de vestir u otras posibles pistas que pueda dar la víctima al criminal de que el
robo puede ser más productivo. Y el riesgo en cambio vendrá determinado por que tan cerca se
encuentra la policía, posibles vías de escape, entre otros parámetros. Un factor que también se
tendrá en cuenta es el fenómeno de near repeat (Johnson et al. 2007; Morgan 2001) que explica
que en un lugar donde se ha realizado un crimen es más probable que ocurra otro en poco
tiempo.
Bibliografía
Elizabeth R. Groff1 • Shane D. Johnson2 • Amy Thornton2 (2018) State of the Art in AgentBased Modeling of Urban Crime: An Overview
Raquel Roses , Cristina Kadar a , Nick Malleson A data-driven agent-based simulation to predict
crime patterns in an urban environment
Wang X, Liu L, Eck JE (2008) Crime Simulation Using GIS and Artificial Intelligent Agents. In: Eck
JE, Liu L (eds) Artificial crime analysis systems: using computer simulations and geographic
information systems. IGI Global, Hershey, pp 209–224
Mesa python library https://github.com/projectmesa/mesa/tree/main/examples
Brantingham, P. J., & Brantingham, P. L. (1981) Notes on the geometry of crime. In P. J.
Brantingham & P. L. Brantingham (Eds.), Environmental criminology (pp. 27–54). Prospect
Heights.
Python Mesa Tutorial - Build Your ABM Simulation Part1:
https://www.youtube.com/watch?v=PDrAsw3UIlA&t=93s
