# 📄 Informe de Prueba con PyTesseract

Se realizaron pruebas de reconocimiento óptico de caracteres (OCR) utilizando la biblioteca `pytesseract` en cinco imágenes con diferentes resoluciones y contenido textual. A continuación, se detallan los resultados obtenidos:

## 🧪 Resultados de las pruebas

| Imagen  | Resolución (px) | Palabras detectadas | Tiempo de procesamiento (s) |
|---------|------------------|----------------------|------------------------------|
| img1    | 700 x 400        | 24                   | 0.376                        |
| img2    | 522 x 325        | 252                  | 1.103                        |
| img3    | 3000 x 2000      | 1                    | 2.994                        |
| img4*   | 640 x 480        | 1                    | 0.317                        |
| img5*   | 128 x 128        | 1                    | 0.104                        |

> \*img4 y img5 son versiones redimensionadas de img3.

---

## 📊 Análisis

- **Resolución vs. Tiempo de procesamiento**:  
  Se observa que el tiempo de procesamiento aumenta significativamente con la resolución, independientemente de la cantidad de texto presente. Por ejemplo, la imagen `img3` con resolución **3000x2000 px** y solo **1 palabra** tardó casi **3 segundos**, mientras que su versión redimensionada `img4` (**640x480 px**) con la misma cantidad de texto tardó solo **0.317 segundos**.

- **Cantidad de texto vs. tiempo**:  
  La imagen `img2` tiene una resolución relativamente baja (**522x325 px**) pero contiene **252 palabras**, lo que generó un tiempo de procesamiento mayor (**1.103 segundos**) que imágenes con menos texto. Esto indica que, además de la resolución, la **cantidad de texto también impacta el tiempo**.

---

## 🧠 Conclusiones

1. El tiempo de procesamiento en `pytesseract` **aumenta directamente con la resolución** de la imagen, incluso si el contenido textual es mínimo.
2. La **cantidad de palabras detectadas también influye**, aunque su impacto es menor que el de la resolución.
3. Para optimizar el rendimiento, es recomendable **reducir la resolución** de las imágenes a un tamaño adecuado sin comprometer la legibilidad del texto.
4. Un equilibrio entre resolución y cantidad de información puede ayudar a lograr una mejor eficiencia en sistemas que usen OCR en tiempo real.
