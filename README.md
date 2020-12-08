# Python_Project

Stud. name: Lupancu Viorica-Camelia

Project name: grep.py \
Project ID: 1 \
Project difficulty: B

Creati un utilitar similar lui "grep" dar in limbajul python care sa suporte urmatoarele optiuni
ale utilitarului "grep" din Linux:
- Cautare dupa expresii regulare intr-un fisier
- Cautare recursiva intr-un folder
- Optiune de tipul "NOT" => sa verifice ca o anumita expresie regulata NU face match
intr-un fisier
- Optiune de tipul "COUNT" care sa spuna de cate ori se face sau match la o expresie
regulata intr-un fisier.
- Optiune de ignore case

INPUT:
- grep.py ".*abc{3,5}.*" a.txt => afiseaza toate liniile din a.txt care au un substring care
respecta expresia regulata ".*abc{3,5}.*"
- grep.py "test" a.txt -ignoreCase => afiseaza toate liniile din a.txt care contin textul "test"
fara sa tina cont de case
- grep.py "test" C:\MyFolder -ignoreCase -count => afiseaza toate fisierele parcurgand
recursiv "C:\MyFolder" care NU contin textul "test" fara sa tina cont de case. Pentru
fiecare fisier este precizat de cate ori s-a gasit textul "text" in acel fisier.

OUTPUT: Verificati ce afiseaza utilitarul grep din linux si incercati sa obtineti un output similar.