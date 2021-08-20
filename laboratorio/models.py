from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
#
from random import shuffle
#import itertools
# Trabajar con fechas utilizando Python haremos uso de la librería datetime
from datetime import datetime, date, timedelta
import pytz

author = 'Victor Hugo Ortega Gomez'

doc = """
EL EFECTO DE LOS TIPOS DE CONTRATO EN EL CONSUMO: UN ANÁLISIS EXPERIMENTAL
"""
""


class Constants(BaseConstants):
    name_in_url = 'laboratorio'
    players_per_group = None
    num_rounds = 24

    porcentaje_similitud = 60

    #
    contrato_formal_fijo = 'Contrato formal a tiempo fijo'
    contrato_formal_indefinido = 'Contrato formal a tiempo indefinido'
    contrato_formal_servicios = 'Contrato formal por prestación de servicios'
    contrato_informal_fijo = 'Contrato informal a tiempo fijo'
    contrato_informal_indefinido = 'Contrato informal a tiempo indefinido'
    contrato_informal_servicios = 'Contrato informal por prestación de servicios'

    textoOriginal1 = "El sector eléctrico es una palanca fundamental para el desarrollo futuro de las ciudades y de la industria.\n Actualmente se está produciendo un cambio en el modelo de negocio desempeñado por los distribuidores de electricidad, ya que más allá de ceñirse, única y exclusivamente, al transporte y distribución de electricidad desde una planta generadora hasta los lugares de consumo, están apareciendo una serie de pequeños agentes capaces de producir su propia energía, y, además, de inyectarla en la red. La gestión de este nuevo tipo de agente y de una energía de diversas procedencias representa un reto que se debe afrontar de forma conjunta. En este sentido, las energías renovables tales como la solar o la eólica pueden comenzar a ser competitivas en el mercado, dado que cada vez requieren de una menor cantidad de subvenciones."
    textoAlternativo1 = "El sector energético es una palanca fundamental para el desarrollo futuro de las ciudades y de la industria.\n Actualmente se está produciendo un cambio en el modelo de negocio desempeñado por los distribuidores de energía, ya que más allá de ceñirse, única y exclusivamente, al transporte y distribución de electricidad desde una empresa generadora hasta los lugares de consumo, están apareciendo una gama de pequeños agentes capaces de producir su propia electricidad y, además, de inllectarla en la red. La gestión de este nuevo tipo de agente y de una energía de diversas procedencias representa un reto que se debe afrontar de forma conjunta. En este sentido, las energías renovables tales como la eólica o la solar pueden comensar a ser competitivas en el mercado, dado que cada vez requieren de una menor cantidad de subvenciones."
    NumeroErrores1 = 9

    textoOriginal2 = "Los mercados de energía se han liberalizado en algunos países; están regulados por autoridades nacionales e internacionales (incluidos los mercados liberalizados) para proteger los derechos del consumidor y evitar oligopolios. Los reguladores incluyen la Comisión Australiana del Mercado de la Energía en Australia, la Autoridad del Mercado de la Energía en Singapur, la Comunidad de la Energía en Europa, reemplazando el Mercado Energético Regional de Europa Sudoriental y el mercado energético nórdico para los países nórdicos.\n Los reguladores buscan desalentar la volatilidad de los precios, reformar los mercados si es necesario y buscar evidencia de comportamiento anticompetitivo como la formación de un monopolio."
    textoAlternativo2 = "Los mercados de energía se han liberalizado en muchos países; están regulados por autoridades nacionales e internacionales (incluidos los mercados liberalizados) para proteger los derechos del consumidor y evitar monopolios. Los reguladores incluyen la Comisión Australiana del Mercado de la Energía en Canberra, la Autoridad del Mercado de la Energía en Singapur, la Comunidad de la Energya en Europa, reemplazando el Mercado Energético Regional de Europa Sudoriental y el mercado energético nórdico para los países nórdicos.\n Los reguladores buscan desalentar la volatilidad de los precios, transformar los mercados si es necesario y buscar evidensia de comportamiento anticompetitivo como la formación de un monopolio."
    NumeroErrores2 = 6

    textoOriginal3 = "Los mercados de energía se encuentran regulados en muchas partes del mundo. Los proveedores de energía disfrutan de un monopolio y las tarifas las fija el gobierno. Sin embargo, existe un fuerte impulso hacia la liberalización. En un mercado energético abierto, las leyes de la oferta y la demanda determinan el precio de la energía. Comprender cómo funcionan es necesario si quiere ser un comprador de energía exitoso y convertirse en un “emprendedor energético”.\n La desregulación no es la única fuerza transformadora que cambia el panorama de los mercados energéticos. La actual revolución de las energías renovables está remodelando toda la industria."
    textoAlternativo3 = "Los mercados de energía se encuentran regulados en muchas partes del mundo. Los proveedores de energía disfrutan de un monopolio y las tarifas las fija el gobierno. Sin embargo, existe un fuerte impulso hacia la liberalización. En un mercado energético abierto, las leyes de la oferta y la demanda determinan el precio de la energía. Comprender cómo funcionan es necesario si quiere ser un comprador de energía exitoso y convertirse en un “emprendedor energético”.\n La desregulación no es la única fuerza transformadora que cambia el panorama de los mercados energéticos. La actual revolución de las energías renovables está remodelando toda la industria."
    NumeroErrores3 = 0

    textoOriginal4 = "El análisis de los mercados energéticos mundiales es fundamental para comprender la fluctuación de los precios locales de la energía. La mayoría de los observadores del mercado están acostumbrados a observar el Medio Oriente, Venezuela o China para comprender qué impulsa el precio del petróleo. Pero el análisis de los mercados de gas natural o electricidad a menudo carece de esta perspectiva global. Por ejemplo, el aumento en el comercio de GNL ha provocado la convergencia de los precios del gas a nivel mundial.\n Dado que los precios se basan en gran medida en combustibles que se comercializan en todo el mundo, una perspectiva global puede proporcionar una visión más profunda de los fundamentos de la oferta y la demanda, para así poder realizar un análisis completo de la situación de los mercados locales."
    textoAlternativo4 = "El análisiz de los mercados energéticos mundiales es fundamental para comprender la fluctuación de los precios locales de la energía. La mayoría de los obserbadores del mercado están acostumbrados a obserbar el Medio Oriente, Venezuela o China para comprender qué impulza el precio del petróleo. Pero el análisiz de los mercados de gas natural o electricida a menudo carece de esta perspectiva global. Por ejemplo, el aumento en el comercio de GNL ha provocado la convergencia de los precios del gas a nivel mundial.\n Dado que los presios se basan en gran medida en combustibles que se comercialisan en todo el mundo, una perspectiva global puede proporcionar una visión más profunda de los fundamemtos de la oferta y la demanda, para así poder realizar un análisis completo de la situación de los mercados locales."
    NumeroErrores4 = 9

    textoOriginal5 = "La energía solar es alabada como fuente de combustible inagotable libre de contaminación y de ruidos. Cada hora el sol lanza a la Tierra más energía de la que sería necesaria para satisfacer las necesidades mundiales de energía durante un año entero.\n Por ejemplo, las células solares generan energía para lugares remotos como los satélites en la órbita de la Tierra y las cabañas en las Montañas Rocosas tan fácilmente como suministran la energía a edificios del centro de las ciudades y a los coches futuristas. Un inconveniente es que la tecnología solar puede ser muy costosa y requiere mucho terreno para recolectarla en tasas que resulten útiles para mucha gente. A pesar de los diferentes obstáculos, el uso de la energía solar ha aumentado un 20% al año durante los últimos 15 años gracias al rápido descenso de los precios y a las ganancias en eficiencia.  Los incentivos tributarios, son uno de los mecanismos con los que puede incentivarse el uso de la electricidad solar."
    textoAlternativo5 = "La energía solar es albada como fuente de combustible inagotable libre de contaminación y de ruidos. Cada hora el sol lanza a la planeta más energía de la que sería necesaria para satisfacer las necesidades mundiales de energía durante un año entero.\n Por ejemplo, las células solares generan energía para lugares remotos como los satélites en la órbita de la Tierra y las cabañas en las Montañas Moscosas tan fácilmente como suministran la energía a edificios del centro de las ciudades y a los coches futuristas. Un inconveniente es que la tecnología solar puede ser muy costosa y requiere mucho terreno para recolectarla en tasas que resulten útiles para mucha gente. A pesar de los diferentes obstáculos, el uso de la energía solar ha aumentado un 200% al año durante los últimos 15 años gracias al rápido descenso de los precios y a las ganancias en eficiencia.  Los incentivos tributarios, son uno de los mecanismos con los que puede incentivarse el uso de la electricidad solar."
    NumeroErrores5 = 4

    textoOriginal6 = "El sector eléctrico se fundamenta en el hecho de que las empresas comercializadoras y los grandes consumidores adquieren la energía y potencia en un mercado de grandes bloques de energía, el cual opera libremente de acuerdo con las condiciones de oferta y demanda. Para promover la competencia entre generadores, se permite la participación de agentes económicos, públicos y privados, los cuales deberán estar integrados al sistema interconectado para participar en el mercado de energía mayorista. Como contraparte comercializadores y grandes consumidores actúan celebrando contratos de energía eléctrica con los generadores. El precio de la electricidad en este mercado se establece de común acuerdo entre las partes contratantes, sin la intervención del Estado."
    textoAlternativo6 = "El sector eléctrico se fundanenta en el hecho de que las empresas comercializadoras y los grandes consumidores adquieren la energía y potencia en un mercado de grandes bloques de energía, el cual opera libremente de acuerdo con las condiciones de oferta y demanda. Para promover la competencia entre ganaradores, se permite la participación de agentes económicos, públicos y privados, los cuales deberán estar integrados al sistema interconectado para participar en el mercdo de energía mayorista. Como contraparte comercializadores y grandes consumidores actúan celebrando contratos de enerjía eléctrica con los generadores. El precio de la electricidad en este mercado se establece de común acuerdo entre las partes contratantes, sin la intervensión del Estado."
    NumeroErrores6 = 5

    textoOriginal7 = "El mercado mayorista eléctrico en Colombia es un mercado competitivo creado por la reforma Eléctrica (leyes 142 y 143 de 1994) en el cual participan generadores, transmisores, distribuidores, comercializadores y grandes consumidores de electricidad o usuarios no regulados. El ente regulador CREG, establece las reglas aplicables a este mercado.\n El mercado se divide en dos segmentos: mercado de contratos bilaterales (largo plazo) y la bolsa de energía (corto plazo). La energía puede ser transada en bolsa o mediante contratos bilaterales con otros generadores, comercializadores o directamente con los grandes consumidores o usuarios no regulados (aquellos cuya demanda es 100 kW o 55 MWh/mes)."
    textoAlternativo7 = "El mercado mayorista eléctrico en Colombia es un mercado competitivo creado por la reforma Eléctrica (leyes 412 y 413 de 1994) en el cual participan generadores, transmisores, distribuidores, comercializadores y grandes consumidores de electricidad o usuarios no regulados. El ente regulador RGEG, establece las reglas aplicables a este mercado.\n El mercado se divide en dos segmentos: mercado de contratos bilaterales (largo plazo) y la bolsa de energía (corto plazo). La energía puede ser transada en bolsa o mediante contratos bilatares con otros generadores, comercialisadores o directamente con los grandes consumidores o usuarios no regulados (aquellos cuya demanda es 55 kW o 100 MWh/mes)."
    NumeroErrores7 = 7

    textoOriginal8 = "El ecoturismo está dirigido a visitantes que desean experimentar el medio ambiente de manera consciente y amigable con los ecosistemas de la región. Es una forma de turismo que implica la visita de áreas naturales frágiles, vírgenes y relativamente tranquilas, concebida como una alternativa de bajo impacto y, a menudo, a pequeña escala al turismo de masas comercial estándar. El propósito de esta actividad es educar al viajero e integrarlo con los cuidados del ambiente, proporcionar fondos para la conservación ecológica, beneficiar directamente el desarrollo económico y el empoderamiento político de las comunidades locales, o fomentar el respeto por las diferentes culturas y los derechos humanos."
    textoAlternativo8 = "El ecoturismo está dirigido a turistas que desean experimentar el medio ambiente de forma consciente y amigable con los ecosistemas de la región. Es una forma de turismo que implica la visita de áreas naturales frágiles, vírgenes y relativamente pacíficas, concebida como una alternativa de bajo impacto y, a menudo, a pequeña escala al turismo de masas comercial estándar. El propósito de esta actividad es educar al viajero e integrarlo con los cuidados del ambiente, proporcionar fondos para la conservación ecológica, beneficiar directamente el desarrollo económico y el enpoderamiento político de las comunidades locales, o fomentar el respeto por las diferentes culturas y los derechos humanos."
    NumeroErrores8 = 4

    textoOriginal9 = 'Según la Sociedad Internacional de Ecoturismo (TIES), el ecoturismo puede definirse como “viajes responsables a áreas naturales que conservan el medio ambiente, sustentan el bienestar de la población local e implican interpretación y educación”. Estos viajes se pueden crear gracias a una red internacional de personas, instituciones y la industria del turismo donde los turistas y los profesionales del turismo se educan sobre temas ecológicos.\n Al mismo tiempo, el Ecoturismo Nacional de Australia define el ecoturismo como "turismo ecológicamente sostenible con un enfoque principal en la experiencia de áreas naturales que fomenta el entendimiento, la apreciación y la conservación ambiental y cultural".'
    textoAlternativo9 = 'Según la Sociedad Internacional de Ecoturismo (TIES), el ecoturismo se refiere a “viajes responsables a áreas naturales que conservan el medio ambiente, sustentan el bienestar de la población local e implican interpretación y educación”. Estos viajes se pueden crear gracias a una red internacional de personas, instituciones y la sociedad del turismo donde los turistas y los empresarios del turismo se educan sobre temas ecológicos.\n De igual manera, el Ecoturismo Nacional de Australia define el ecoturismo como "turismo ecológicamente sostenible con un enfoque principal en la experiencia de áreas naturales que fomenta el entendimiento, la apreciación y la conservación ambiental y cultural".'
    NumeroErrores9 = 8

    textoOriginal10 = "Las ventajas que ofrece el ecoturismo a los viajeros son personales, pero sus efectos son generalizados. Al visitar áreas de impresionante belleza natural, ver animales en sus hábitats nativos y conocer a miembros de las comunidades locales, los viajeros pueden aumentar su conciencia sobre la importancia de conservar los recursos y evitar el desperdicio. Se les anima a vivir de manera más sostenible en casa y también pueden aumentar su comprensión y sensibilidad hacia otras culturas. Además, los viajeros aprenden cómo ayudar a apoyar a otras comunidades, no entregando obsequios como juguetes y papelería, sino comprando productos y productos locales. Cuando los ecoturistas regresan a casa, transmiten el mensaje a sus familias, amigos y compañeros de trabajo.\n El ecoturismo permite a los países y comunidades construir sus economías sin dañar el medio ambiente, lo que significa que la vida silvestre local puede prosperar y los visitantes pueden disfrutar de destinos naturales."
    textoAlternativo10 = "Las ventajas que ofrece el ecoturismo a los viajeros son personales, pero sus efectos son generalizados. Al visitar áreas de impresionante belleza natural, ver animales en sus hábitats nativos y conocer a miembros de las comunidades locales, los turistas pueden aumentar su conciencia sobre la importancia de conservar los recursos y evitar el desperdisio. Se les anima a vivir de manera más sostenible en casa y también pueden aumentar su comprensión y sensibilidad hacia otras culturas. Además, los viajeros aprenden cómo ayudar a apoyar a otras comunidades, no entregando obsequios como juguetes y papelería, sino comprando productos y productos locales. Cuando los ecoturistas regresan a casa, transmiten el mensaje a sus familias, amigos y compañeros de trabajo.\n El ecoturismo permite a los países y comunidades construir sus economías sin dañar el medio ambiente, lo que significa que la vida silvestre local puede prosperar y los visitantes pueden disfrutar de destinos naturales."
    NumeroErrores10 = 2

    textoOriginal11 = "Colombia es mundialmente famosa por su biodiversidad. Desde sus densas selvas, exuberantes selvas tropicales y playas de arena blanca hasta sus impresionantes cadenas montañosas e interminables desiertos y llanuras, el país está lleno de aves y animales raros. Los viajeros conscientes del medio ambiente pueden disfrutar del ecoturismo y los viajes de aventura de bajo impacto en Colombia y difundir estas especies.\n Los Andes colombianos albergan muchos de los ecosistemas más ricos e inusuales del país y el Parque Nacional Chingaza es uno de los mejores lugares para el ecoturismo en el país. Este enorme parque, cercano a la capital, Bogotá, se extiende en altitudes de 800 a 4.000 metros sobre el nivel del mar y es hogar de osos de anteojos, jaguares, pumas, monos lanudos, tucanes y el imponente cóndor andino."
    textoAlternativo11 = "Colonbia es mundialmente famosa por su biodiversidad. Desde sus densas selvas, eshuberantes selvas tropicales y playas de arena blanca hasta sus impresionantes cadenas montañosas e interminables deciertos y llanuras, el país está lleno de aves y animales exóticos. Los viajeros concientes del medio ambiente pueden disfrutar del ecoturismo y los viajes de aventura de bajo impacto en Colombia y difundir estas especies.\n Los Andes colombianos albergan muchos de los ecosistemas más ricos e inusuales del paíz y el Parque Nacional Chingaza es uno de los mejores lugares para el ecotirismo en el país. Este enorme parque, cercano a la capital, Bogotá, se extiende en altitudes de 8000 a 4.0000 metros sobre el nivel del mar y es hogar de osos de anteojos, jaguares, pumas, monos lanudos, tucanes y el imponente cóndor andino."
    NumeroErrores11 = 9

    textoOriginal12 = "El monte Nyiragongo rara vez está tranquilo. El volcán montañoso en el este de la República Democrática del Congo (RDC) es uno de los pocos lugares del mundo con un lago de lava persistente burbujeando dentro del cráter de su cima. Su reputación letal se debe a una tormenta perfecta de factores a causa de las complejidades geológicas de la región, su lava es muy fluida y es capaz de moverse a 64 kilómetros por hora.\n Las erupciones del Nyiragongo suelen producirse cuando la presión por la acumulación del magma o un terremoto abre fisuras en las laderas de la montaña, provocando el drenaje catastrófico del lago de lava o la erupción del magma almacenado a más profundidad, pero al igual que los volcanes que las forman, cada erupción tiene su propio comportamiento y propiedades, y no hay dos idénticas."
    textoAlternativo12 = "El monte Nyiragongo rara vez está tranquilo. El volcán montanoso en el este de la República Socialista del Congo (RDC) es uno de los pocos lugares del mundo con un lago de lava persistente burbujeando dentro del cráter de su sima. Su reputación letal se debe a una serie perfecta de factores a causa de las complejidades geológicas de la región, su lava es muy fluida y es capaz de moverse a 64 kilómetros por hora.\n Las erupciones del Nyiragongo suelen producirse cuando la preción por la acumulación del magma o un terremoto abre fisuras en las laderas de la montaña, provocando el drenaje catastrófico del lago de laba o la erupción del magma almacenado a más profundidad, pero al igual que los volcanes que las forman, cada erupción tiene su propio comportamiento y propiedades, y no hay dos idénticas."
    NumeroErrores12 = 6

    textoOriginal13 = "Famosos por su memoria, inteligencia y sociabilidad, los elefantes al igual que los humanos, son particularmente vulnerables al estrés y al trauma, presentando consecuencias psicológicas a largo plazo. Además de ser importantes contribuyentes a los ingresos del turismo en muchos países de África y Asia, son una parte sustancial de nuestro patrimonio cultural e histórico y es un placer para nosotros contemplarlos.\n Como todos los mamíferos altamente sociales, los elefantes tienen un sistema de comunicación bien desarrollado que hace uso de todos sus sentidos (oído, olfato, visión y tacto), incluida una capacidad excepcional para detectar vibraciones."
    textoAlternativo13 = "Famosos por su memoria, inteligencia y sociabilidad, los elefanfes al igual que los humanos, son particularmente vulnerables al estrés y al trauma, presentando consecuencias psicológicas a largo plazo. Además de ser importantes contribuyentes a los ingresos del turismo en muchos países de Áfrika y Asia, son una parte sustancial de nuestro patrimonio cultural e histórico y es un placer para nosotros contemplarlos.\n Como todos los mamíferos altamente sociales, los elefantes tienen un sistema de comunicasión bien desarrollado que hace uso de todos sus sentidos (oído, olfato, visión y tacto), incluida una capacidad excepcional para detectar vibraciones." 
    NumeroErrores13 = 3

    textoOriginal14 = "El ecoturismo consiste en recorrer las áreas naturales sin perturbarlas, con el único fin de apreciarlas, disfrutarlas y estudiarlas tanto los atractivos naturales como flora, fauna, y paisajes, así como también las manifestaciones culturales que ahí pueden presentarse. Canadá es una referencia en ecoturismo. Un país preocupado por proteger su patrimonio natural y concienciado con la importancia de proteger sus espacios verdes. Comprometidos con la naturaleza, los canadienses han desarrollado una gran política de protección forestal para preservar sus excelentes bosques que a su vez son el hogar de animales en peligro como el oso negro, el alce, el ciervo o el lobo gris. Este tipo de turismo y la promoción del mismo genera ingresos para todas aquellas personas que dependen de esto, y al mismo tiempo contribuye de manera directa a la protección, conservación y la restauración de los ecosistemas de la tierra en Canadá, como en los demás países que promuevan este tipo de turismo."
    textoAlternativo14 = "El ecoturismo consiste en recorrer las áreas naturales sin peturbarlas, con el único fin de apreciarlas, disfrutarlas y estudiarlas tanto los atractivos naturales como flora, fauna, y paisajes, así como también las manifestaciones culturales que ahí pueden presentarse. Canadá es una referendia en ecoturismo. Un país preocupado por proteger su patrimonio natural y concienciado con la importancia de proteger sus espacios berdes. Comprometidos con la naturalez, los canadienses han desarrollado una gran política de protección forestal para conservar sus excelentes bosques que a su vez son el hogar de animales en peligro como el oso negro, el venado, el ciervo o el lobo gris. Este tipo de turismo y la promoción del mismo genera ingresos para todas aquellas personas que dependen de esto, y al mismo tiempo contribuye de manera directa a la protección, conservación y la restaurasión de los ecosistemas de la tierra en Colombia, como en los demás países que promuevan este tipo de turismo."
    NumeroErrores14 = 8

    textoOriginal15 = 'Una nebulosa es una nube gigante de polvo y gas en el espacio. Algunas nebulosas provienen del gas y el polvo arrojados por la explosión de una estrella moribunda, como una supernova. Otras nebulosas son regiones donde comienzan a formarse nuevas estrellas. Por esta razón, algunas nebulosas se denominan "viveros de estrellas". Las nebulosas están formadas por polvo y gases, principalmente hidrógeno y helio. El polvo y los gases en una nebulosa están muy dispersos, pero la gravedad puede comenzar a juntar lentamente acumulaciones de polvo y gas. A medida que estos grupos se hacen cada vez más grandes, su gravedad se vuelve cada vez más fuerte.\n Eventualmente, el grupo de polvo y gas se vuelve tan grande que colapsa por su propia gravedad. El colapso hace que el material en el centro de la nube se caliente, y este núcleo caliente es el comienzo de una estrella.'
    textoAlternativo15 = 'Una nebulosa es una nube jigante de polvo y gaz en el espacio. Algunas nebuloas provienen del gas y el polvo arrojados por la explosión de una extrella moribunda, como una supernoba. Otras nebulosas son regiones donde comienzan a formarse nuevas estrellas. Por esta razón, algunas nebulosas se denominan "viveros de estrellas". Las nebulosas están formadas por polvo y gases, principalmente hidrógeno y helio. El polvo y los gases en una nebulosa están muy dispersos, pero la gravedad puede comenzar a unirlas lentamente acumulaciones de polvo y gas. A medida que estos grupos se hacen cada vez más grandes, su gravedad se vuelve cada vez más fuerte.\n Eventualmente, el grupo de polvo y gas se vuelve tan grande que colpsa por su propia gravedad. El colapso hace que el material en el centro de la nube se caliente, y este núcleo caliente es el comienzo de una estrella.' 
    NumeroErrores15 = 7

    textoOriginal16 = "Las nebulosas existen en el espacio entre las estrellas, también conocido como espacio interestelar. La nebulosa conocida más cercana a la Tierra se llama Nebulosa Helix. Es el remanente de una estrella moribunda, posiblemente una como el Sol. Se encuentra aproximadamente a 700 años luz de la Tierra. Eso significa que incluso si pudiera viajar a la velocidad de la luz, ¡aún le tomaría 700 años llegar allí!\n Los astrónomos usan telescopios muy poderosos para tomar fotografías de nebulosas lejanas. Telescopios espaciales como el Telescopio Espacial Spitzer de la NASA y el Telescopio Espacial Hubble han capturado muchas imágenes de nebulosas lejanas."
    textoAlternativo16 = "Las nebulosas existen en el espacio entre las estrellas, también conocido como espacio interestelar. La nebuloza conocida más cercana a la Tierra se llama Nebulosa Helix. Es el remanente de una estrella moribunda, posiblemente una como el Sol. Se encuentra aproximadamente a 70 años luz de la Tierra. Eso significa que incluso si pudiera viajar a la velocidad de la luz, ¡aún le tomaría 700 anos llegar allí!\n Los astrónomos usan telescopios muy poderosos para tomar fofografías de nebulosas lejanas. Telescopios espaciales como el Telescopio Espacial Spitzer de la NASA y el Telescopio Espacial Huble han capturado muchas imágenes de nebulosas lejanas."
    NumeroErrores16 = 5

    textoOriginal17 = "Una supernova ocurre cuando una estrella de gran masa llega al final de su vida. Cuando se detiene la fusión nuclear en el núcleo de la estrella, la estrella colapsa. El gas que cae hacia adentro rebota o se calienta con tanta fuerza que se expande hacia afuera desde el núcleo, lo que hace que la estrella explote. La capa de gas en expansión forma un remanente de supernova, una nebulosa difusa especial. Aunque gran parte de la emisión óptica y de rayos X de los remanentes de supernova se origina a partir de gas ionizado, una gran cantidad de la emisión de radio es una forma de emisión no térmica llamada emisión de sincrotrón. Esta emisión se origina a partir de electrones de alta velocidad que oscilan dentro de campos magnéticos."
    textoAlternativo17 = "Una supernova ocurre cuando una estrella de gran masa llega al final de su vida. Cuando se detiene la fusión nuclear en el núcleo de la extrella, la estrella colapsa. El gas que cae hacia adentro rebota o se calienta con tanta fuerza que se expande hacia afuera desde el núcleo, lo que hace que la estrella explote. La capa de gas en expansión forma un remanente de supernova, una nebulosa difusa especial. Aunque gran parte de la emisión óptica y de rayos Y de los remanentes de supernova se origina a partir de gas ionizado, una gran cantidad de la emisión de radio es una forma de emisión no térmica llamada emisión de sincrotrón. Esta emisión se orijina a partir de electrones de alta velocidad que oscilan dentro de campos magnéticos."
    NumeroErrores17 = 3

    textoOriginal18 = 'PK164+31.1, conocida también como Jones-Emberson 1, es una nebulosa planetaria poco brillante que se encuentra a unos 1.600 años luz de distancia hacia la constelación del Lince (Lynx). Debido a su magnitud 17 es sólo visible en telescopios de tamaño considerable. Cerca del centro de la nebulosa se puede ver una estrella enana blanca azul caliente que es lo que queda del núcleo ya que el gas es expulsado en diferentes etapas al final de la vida de la estrella.  La nebulosa en expansión se desvanecerá durante los próximos miles de años mientras la estrella central puede sobrevivir durante miles de millones de años.\n Descubierta en 1939 por Rebecca Jones y Richard M. Emberson, su designación "PK" proviene de los nombres de los astrónomos checoslovacos Lubos Perek y Lubos Kohoutek , quienes en 1967 crearon un extenso catálogo de todas las nebulosas planetarias conocidas en la Vía Láctea a partir de 1964.'
    textoAlternativo18 = 'PK164+31.1, conocida también como Jones-Emberson 1, es una nebulosa planetaria poco brillante que se encuentra a unos 1.600 años luz de distancia hacia la constelación del Lince (Linx). Debido a su manitud 17 es sólo visible en telescopios de tamaño considerable. Cerca del centro de la nebulosa se puede ver una estrella pequeña blanca asul caliente que es lo que queda del núcleo ya que el gas es expulsado en diferentes fases al final de la vida de la estrella.  La nebulosa en expansión se desvanecerá durante los próximos miles de años mientras la estrella central puede sobrevivir durante miles de millones de años.\n Descubierta en 1739 por Rebecca Jones y Richard M. Emberson, su designación "OK" proviene de los nombres de los astrónomos checoslovacos Lubos Perek y Luboš Kohoutek , quienes en 1967 crearon un largo catálogo de todas las nebulosas planetarias conocidas en la Vía Láctea a partir de 1964.'
    NumeroErrores18 = 8

    textoOriginal19 = "Los agujeros negros son los restos fríos de antiguas estrellas, tan densas que ninguna partícula material, ni siquiera la luz, es capaz de escapar a su poderosa fuerza gravitatoria. Cuando las estrellas gigantes alcanzan el estadio final de sus vidas estallan en cataclismos conocidos como supernovas. Tal explosión dispersa la mayor parte de la estrella al vacío espacial, pero quedan una gran cantidad de restos «fríos» en los que no se produce la fusión.\n En los restos inertes de una supernova no hay una fuerza que se resista a la gravedad, por lo que la estrella empieza a replegarse sobre sí misma. Sin una fuerza que frene la gravedad, el emergente agujero negro encoje hasta un volumen cero, en cuyo punto pasa a ser infinitamente denso. Incluso la luz de dicha estrella es incapaz de escapar a su inmensa fuerza gravitatoria, que se ve atrapada en órbita, por lo que la oscura estrella se conoce con el nombre de agujero negro."
    textoAlternativo19 = "Los agujeros negros son los restos fríos de viejas estrellas, tan densaz que ninguna partícula materal, ni siquiera la luz, es capaz de escapar a su poderosa fuersa gravitatoria. Cuando las estrellas gigantes alcanzan el estadio final de sus vidas estallan en cataclismos conocidos como supernovas. Tal explosión dispersa la mayor parte de la estrella al vacío espacial, pero quedan una gran cantidad de restos «fríos» en los que no se produce la fusión.\n En los restos inertes de una supernova no hay una fuerza que se resista a la grabedad, por lo que la estrella empieza a replegarse sobre sí misma. Sin una fuerza que frene la gravedad, el emergente agugero negro encoge hasta un volumen cero, en cuyo punto pasa a ser infinitamente denso. Incluso la luz de dicha estrella es incapaz de escapar a su inmensa fuerza gravitatoria, que se ve atrapada en órbita, por lo que la oscura estrella se conoce con el nombre de agujero negro."
    NumeroErrores19 = 7

    textoOriginal20 = "Cada agosto, la Tierra atraviesa una nube de restos que deja a su paso el cometa Swift-Tuttle. Esto produce una ráfaga de estrellas fugaces en el cielo a medida que los pequeños meteoros arden en la atmósfera superior. Se trata de la lluvia de meteoros de las Perseidas, que puede producir hasta 60 estrellas fugaces por hora en un año normal. Con cielos despejados, podrán verse decenas de estrellas fugaces cada hora incluso desde un jardín o parque suburbano.\n Este año promete ser particularmente bueno para las Perseidas, ya que el pico de la lluvia coincidirá con un cielo oscuro y sin Luna. Una delgada luna creciente se pondrá a principios de la tarde, dejando a su paso condiciones de observación excelentes conforme anochezca."
    textoAlternativo20 = "Cada ahosto, la Tierra atraviesa una nube de restos que deja a su paso el cometa Swit-Tuttle. Esto produce una ráfaga de estrelas fugaces en el cielo a medida que los pequeños meteoros arden en la atmósfera superior. Se trata de la lluvia de meteoros de las Perseidas, que puede producir hasta 60 estrellas fugaces por hora en un año normal. Con cielos despejados, podrán verse decenas de estrellas fugaces cada ora incluso desde un jardín o parque suburbano.\n Este año promete parecer particularmente bueno para las Perseidas, ya que el pico de la lluvia coincdirá con un cielo oscuro y sin Luna. Una delgada luna creciente se pondrá a principios de la tarde, dejando a su paso condisiones de observación excelentes conforme anochezca."
    NumeroErrores20 = 7

    textoOriginal21 = "El cometa Halley es uno de los más famosos fenómenos estelares del planeta. Es un cometa que se aproxima a la Tierra aproximadamente cada 75 años, lo que hace posible que un ser humano lo vea dos veces en su vida. La última vez que estuvo aquí fue en 1986, y se prevé que regrese en 2061.\n La Misión Giotto proporcionó a los astrónomos la primera visión de la estructura y superficie del cometa Halley. Al entrar en el interior del sistema solar, y aproximarse al perihelio, el Sol calienta su superficie, causando la sublimación de su materia, y pasando directamente del estado sólido al gaseoso, emitiendo una gran cantidad de gas volátil desde su oscura superficie."
    textoAlternativo21 = "El cometa Halley es uno de los más famosos fenómemos estelares del planeta. Es un cometa que se aproxima a la Tierra aproximadamente cada 75 años, lo que hace posible que un ser humano lo vea dos veces en su vida. La última vez que estuvo aquí fue en 1886, y se prevé que regrese en 2061.\n La Misión Giotto proporcionó a los astrónomos la primera visión de la estructura y superficie del cometa Halley. Al entrar en el interior del sistema solar, y aproximase al perihelio, el Sol calienta su superficie, causando la sublimación de su materia, y pasando directamente del estado sólido al gaseoso, emitiendo una gran cantidad de gas volátil desde su oscura superficie."
    NumeroErrores21 = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_field(label):
    return models.StringField(

        choices=[
            ['Fuertemente en desacuerdo', ""],
            ['En desacuerdo', ""],
            ['Ni de acuerdo, ni en desacuerdo', ""],
            ['De acuerdo', ""],
            ['Fuertemente de acuerdo', ""],
        ],
        label=label,
        widget=widgets.RadioSelect,
    )


def make_field2(label):
    return models.IntegerField(
        choices=[-2, -1, 0, 1, 2],
        label=label,
    )

def make_field3(label):
    return models.StringField(

        choices=[
            ['Muy deshonesto', ""],
            ['Levemente deshonesto ', ""],
            ['Ni deshonesto ni honesto', ""],
            ['Levemente honesto', ""],
            ['Muy honesto', ""],
        ],
        label=label,
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):

    pagoSesion1 = models.CurrencyField(initial=0)
    pagoSesion2 = models.CurrencyField(initial=0)
    pagoSesion3 = models.CurrencyField(initial=0)

    treatment = models.StringField()

    def set_treatment(self):
        if self.session.config['tipo'] == "formal-fijo":
            self.treatment = 'Contrato formal a tiempo fijo'
        elif self.session.config['tipo'] == "formal-indefinido":
            self.treatment = 'Contrato formal a tiempo indefinido'
        elif self.session.config['tipo'] == "formal-servicios":
            self.treatment = 'Contrato formal por prestación de servicios'
        elif self.session.config['tipo'] == "informal-fijo":
            self.treatment = 'Contrato informal a tiempo fijo'
        elif self.session.config['tipo'] == "informal-indefinido":
            self.treatment = 'Contrato informal a tiempo indefinido'
        elif self.session.config['tipo'] == "informal-servicios":
            self.treatment = 'Contrato informal por prestación de servicios'

    def live_test(self, data):
        print('el dato es', data)
        print(self.actividad_2)
        inversion = data['inversion']
        if data['moneda'] == 'Cara':
            pago = inversion * 2 + (2000 - inversion)
            print('el pago de la actividad 2 es:', pago)
            self.payoff = c(pago)
        else:
            pago = inversion * 0 + (2000 - inversion)
            self.payoff = c(pago)
            print('el pago de la actividad 2 es:', pago)

        return {0: pago}

    # Variables que contienen la fecha de inicio y las fechas de espera
    # get time of participant when welcome page is submitted
    start_date = models.StringField()
    next_date = models.StringField()
    date_after_next = models.StringField()
    date_after_after_next = models.StringField()

    # Funcion que determina las fechas de espera
    def get_time(self):
      #  self.starttime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        zona_horaria = datetime.now(pytz.timezone('America/Bogota'))
        fecha_actual = zona_horaria.date()
        cadena_fecha_actual = fecha_actual.strftime('%Y-%m-%d')

        fecha_siguiente = fecha_actual + timedelta(days=2)
        cadena_fecha_siguiente = fecha_siguiente.strftime('%Y-%m-%d')

        fecha_despues_siguiente = fecha_actual + timedelta(days=4)
        cadena_fecha_despues_siguiente = fecha_despues_siguiente.strftime(
            '%Y-%m-%d')

        fecha_nueva = fecha_actual + timedelta(days=6)
        cadena_fecha_nueva = fecha_nueva.strftime('%Y-%m-%d')

        self.start_date = cadena_fecha_actual
        self.next_date = cadena_fecha_siguiente
        self.date_after_next = cadena_fecha_despues_siguiente
        self.date_after_after_next = cadena_fecha_nueva

    consentimiento = models.BooleanField(
        label='¿Autoriza el uso de los datos recolectados que sólo serán utilizados para fines académicos?',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    terminos_actividad = models.BooleanField(
        label='¿Acepta los términos de esta actividad?',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    codigo = models.StringField(
        label='Por favor, escriba el código de identificación que se les envió en el mensaje de la encuesta.')
    confirmacion_codigo = models.StringField(
        label='Por favor confirme el código de identificación')

    #
    texto_digitado1 = models.TextField(label='',)
    texto_digitado2 = models.TextField(label='',)
    texto_digitado3 = models.TextField(label='',)
    texto_digitado4 = models.TextField(label='',)
    texto_digitado5 = models.TextField(label='',)
    texto_digitado6 = models.TextField(label='',)
    texto_digitado7 = models.TextField(label='',)
    texto_digitado8 = models.TextField(label='',)
    texto_digitado9 = models.TextField(label='',)
    texto_digitado10 = models.TextField(label='',)
    texto_digitado11 = models.TextField(label='',)
    texto_digitado12 = models.TextField(label='',)

    porcentaje1 = models.DecimalField(max_digits=5, decimal_places=2)

    #
    erroresTexto1 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto2 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto3 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto4 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto5 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto6 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto7 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto8 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto9 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto10 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto11 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto12 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto13 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto14 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto15 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto16 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto17 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto18 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto19 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto20 = models.IntegerField(label="Indique el número de errores que encontró")
    erroresTexto21 = models.IntegerField(label="Indique el número de errores que encontró")

    # Productos
    productos_alimentos = models.CurrencyField(initial=0)
    productos_snack = models.CurrencyField(initial=0)
    productos_aseo = models.CurrencyField(initial=0)
    productos_electronicos = models.CurrencyField(initial=0)
    productos_servicios = models.CurrencyField(initial=0)
    productos_transporte = models.CurrencyField(initial=0)
    productos_diversion = models.CurrencyField(initial=0)
    productos_ahorro = models.CurrencyField(initial=0)
    productos_deudas = models.CurrencyField(initial=0)

    productos_post_alimentos = models.CurrencyField(initial=0)
    productos_post_snack = models.CurrencyField(initial=0)
    productos_post_aseo = models.CurrencyField(initial=0)
    productos_post_electronicos = models.CurrencyField(initial=0)
    productos_post_servicios = models.CurrencyField(initial=0)
    productos_post_transporte = models.CurrencyField(initial=0)
    productos_post_diversion = models.CurrencyField(initial=0)
    productos_post_ahorro = models.CurrencyField(initial=0)
    productos_post_deudas = models.CurrencyField(initial=0)

    total = models.CurrencyField(initial=0)
    total_post = models.CurrencyField(initial=0)

    actividad_2 = models.IntegerField(
        min=0, max=2000, label='Por favor, indica el monto que invertirás en el activo de riesgo (Recuerde digitar la cantidad sin comas ni puntos)')

    # Encuesta

    edad = models.IntegerField(label='¿Cuántos años cumplidos tiene?')
    ciudad = models.StringField(label='¿En qué ciudad vive actualmente?')
    sexo = models.StringField(
        blank=True,
        label='¿Cuál es su sexo? ',
        choices=['Mujer', 'Hombre'],
        widget=widgets.RadioSelect,
    )

    estrato = models.IntegerField(
        blank=True,
        label='¿Cuál es el estrato de la vivienda en la cual habita actualmente?',
        choices=[1, 2, 3, 4, 5, 6],
        widget=widgets.RadioSelect,
    )

    estado_civil = models.StringField(
        label='¿Cuál es su estado civil? (Por favor, escoja una opción)',
        choices=['Soltero', 'casado', 'Unión libre',
                 'Divorciado', 'Viudo', 'Prefiero no decir']
    )

    hijos = models.IntegerField(label='¿Cuántos hijos tiene usted?')

    etnia = models.StringField(
        label='De acuerdo con su cultura o rasgos físicos, usted es o se reconoce como:(Por favor, escoja una opción)',
        choices=['Afrocolombiano', 'Indigena', 'Mestizo', 'Mulato', 'Blanco',
                 'Raizal del archipielago', 'Palenquero', 'Otro', 'Prefiero no decir']
    )

    religion = models.StringField(
        label='¿En cuál de los siguientes grupos se identifica usted?(Por favor, escoja una opción)',
        choices=['Católico', 'Cristiano', 'Testigo de Jehová', 'Ateo', 'Agnóstico',
                 'Judío', 'Musulmán', 'Hinduista', 'Otro', 'Prefiero no decir']
    )

    estudios = models.StringField(
        label='¿Cuál es el máximo nivel de estudios alcanzado a la fecha? (Por favor, escoja una opción)',
        choices=[
            'Primaria incompleta',
            'Primaria completa',
            'Básica secundaria (9º grado completo)',
            'Media secundaria (11º grado completo)',
            'Técnico incompleto',
            'Técnico completo',
            'Tecnológico incompleto',
            'Tecnológico completo',
            'Pregrado incompleto',
            'Pregrado completo',
            'Postgrado incompleto',
            'Posgrado completo'
        ]
    )

    actividad_actual = models.StringField(
        label='Actualmente, ¿cuál es su actividad principal? (Por favor, escoja una opción)',
        choices=['Estudiar', 'Trabajar', 'Oficios del hogar',
                 'Buscar trabajo', 'Otra actividad']
    )

    esta_laborando = models.BooleanField(
        label='¿Se encuentra usted laborando actualmente? (Por favor, escoja una opción)',
        choices=[
            [True, "Sí"],
            [False, "No"],
        ]
    )

    ingreso_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de ingresos mensuales (incluya mesadas, subsidios y remesas)?',
        choices=[
            'Menos de 327.674',
            'Entre 327.675 y 908.526',
            'Entre 908.527 y 1’817.052',
            'Entre 1´817.053 y 3´998.166',
            'Más de 3´998.167'
        ]
    )

    gasto_mensual = models.StringField(
        label='¿Cuál es su nivel aproximado de gastos mensuales?',
        choices=[
            'Menos de 327.674',
            'Entre 327.675 y 908.526',
            'Entre 908.527 y 1’817.052',
            'Entre 1´817.053 y 3´998.166',
            'Más de 3´998.167'
        ]
    )

    #
    alimentos = models.IntegerField(label="Alimentos")
    aseo = models.IntegerField(label="Productos de aseo")
    electronicos = models.IntegerField(label="Artículos electrónicos")
    transporte = models.IntegerField(label="Transporte")
    servicios = models.IntegerField(label="Pago de servicios")
    diversion = models.IntegerField(label="Diversión y ocio")
    ahorro = models.IntegerField(label="Ahorro")
    deudas = models.IntegerField(label="Pago de deudas")

    # Esacala Likert
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[
                                  1, 2, 3, 4, 5, 6, 7, 8, 9, 10], label="")

    Estabilidad = models.IntegerField(choices=[
                                      1, 2, 3, 4, 5], label='Mantenerse invariable o inalterable en el mismo lugar, estado o situación.')
    Independencia = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Autonomía de tomar las decisiones propias.')
    Descanso = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Reposar fuerzas a través de un estado inactivo')
    Lucro = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Ganancia o provecho de algún actividad u objeto.')
    Protección = models.IntegerField(
        choices=[1, 2, 3, 4, 5], label='Seguridad o respaldo frente a un acontecimiento.')

    encuesta_tabla1_pregunta1 = make_field(
        'Por lo general, cuando consigo lo que quiero es porque me he esforzado por lograrlo.')
    encuesta_tabla1_pregunta2 = make_field(
        'Cuando hago planes estoy casi seguro (a) que conseguiré que lleguen a buen término.')
    encuesta_tabla1_pregunta3 = make_field(
        'Prefiero los juegos que entrañan algo de suerte que los que sólo requieren habilidad.')
    encuesta_tabla1_pregunta4 = make_field(
        'Si me lo propongo, puedo aprender casi cualquier cosa.')
    encuesta_tabla1_pregunta5 = make_field(
        'Mis mayores logros se deben más que nada a mi trabajo arduo y a mi capacidad.')
    encuesta_tabla1_pregunta6 = make_field(
        'Por lo general no establezco metas porque se me dificulta mucho hacer lo necesario para alcanzarlas.')
    encuesta_tabla1_pregunta7 = make_field(
        'La competencia desalienta la excelencia.')
    encuesta_tabla1_pregunta8 = make_field(
        'Las personas a menudo salen adelante por pura suerte.')
    encuesta_tabla1_pregunta9 = make_field(
        'En cualquier tipo de examen o competencia me gusta comparar mis calificaciones con las de los demás.')
    encuesta_tabla1_pregunta10 = make_field(
        'Pienso que no tiene sentido empeñarme en trabajar en algo que es demasiado difícil para mí.')


    encuesta_tabla2_pregunta1 = make_field3(
        'Iglesia / Organizaciones religiosas ')
    encuesta_tabla2_pregunta2 = make_field3(
        'Fuerzas Armadas Militares ')
    encuesta_tabla2_pregunta3 = make_field3(
        'Patrullero de Policía')
    encuesta_tabla2_pregunta4 = make_field3(
        'Policía excluyendo Patrulleros')
    encuesta_tabla2_pregunta5 = make_field3(
        'Dirección de impuestos y Aduanas (DIAN)')
    encuesta_tabla2_pregunta6 = make_field3(
        'Medios de comunicación públicos')
    encuesta_tabla2_pregunta7 = make_field3(
        'Gabinete de ministros')
    encuesta_tabla2_pregunta8 = make_field3(
        'Corte Suprema de Justicia')
    encuesta_tabla2_pregunta9 = make_field3(
        'Partidos Políticos')
    encuesta_tabla2_pregunta10 = make_field3(
        'Universidades Públicas')
    encuesta_tabla2_pregunta11 = make_field3(
        'Universidad del Valle')

    encuesta_tabla3_pregunta1 = make_field2('Llegar tarde a una cita')
    encuesta_tabla3_pregunta2 = make_field2('Comprar a vendedores ambulantes')

    encuesta_tabla3_pregunta4 = make_field2(
        'Trabajar y recibir un pago sin que haya firmado un contrato formal (pintar una casa, realizar un reporte, etc.)')

    encuesta_tabla3_pregunta6 = make_field2(
        'Darle trabajo a alguien y pagarle sin pedirle que firme un contrato formal (pintar una casa, realizar un reporte, etc.)')

    encuesta_tabla3_pregunta8 = make_field2(
        'No cotizar al sistema de pensiones')
    encuesta_tabla3_pregunta9 = make_field2('No aportar al sistema de salud')

    encuesta_tabla3_pregunta12 = make_field2('No tener cuenta bancaria')
    encuesta_tabla3_pregunta13 = make_field2(
        'Pedir dinero prestado a prestamistas informales (ejemplo: gota a gota)')

    encuesta_tabla3_pregunta15 = make_field2(
        'Usar transportes alternativos como piratas o mototaxis')
    encuesta_tabla3_pregunta16 = make_field2(
        'Vender cosas o hacer negocios de manera informal')

    encuesta_tabla3_pregunta18 = make_field2('No votar')
    encuesta_tabla3_pregunta19 = make_field2(
        'Ir a eventos políticos para conseguir empleo/beneficios personales')

    encuesta_tabla3_pregunta21 = make_field2('Comprar productos sin factura')
    encuesta_tabla3_pregunta22 = make_field2('Subarrendar una habitación')

    color = models.StringField()
