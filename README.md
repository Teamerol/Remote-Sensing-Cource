# Remote-Sensing-Cource
Scripts in Python created for processing and researching sentinel-2 images.

Рекомендации к использованию:
1. Использовать **на свой страх и риск**.
2. Большая часть скриптов писалась на скорую руку, поэтому не представляет из себя ничего красивого в плане дизайна кода.
3. Если будете совместно запускать скрипты, то некоторые (или даже многие) вещи могут не работать. При необходимости обращайтесь, и я постараюсь помочь.
4. Скрипт Histogram.py строит трехмерную гистограмму, но она очень странно выглядит. Очень желательна валидация и перепроверка.

Задачи, выполняемые скриптами:
1. Change_format.py - преобразование формата из .jp2 в .img.
2. Create_images.py - создание серии картинок с визуализацией содержимого каждого канала.
3. Filter.py - преобразование каналов высокочастотным (high pass) и низкочастотным (low pass) фильтрами с целью выделения границ и повышения контрастности соответственно.
4. Histogram.py - построение двухмерной гистограммы в 3D (***Очень похоже, что строит некорректную диаграмму***).
5. Interpolate.py - простейшая интерполяция значений путём увеличения размера матрицы и вставки старых значений.
6. Scatterplot.py - построение точечной диаграммы по двум каналам.
7. Covariation.py - расчёт матрицы ковариации для двух каналов.
8. PCA_sklearn.py - применение анализа главных компонент для уменьшения размерности данных. Можно использовать одну из двух функций для построения разных изображений.
9. Classification.py - классификация на основе теоремы Байеса в упрощённой интерпретации. Не автоматизирован подсчёт границ для классов.
