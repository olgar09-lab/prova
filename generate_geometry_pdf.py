from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="ca">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 15mm;
            background-color: #ffffff;
        }
        body {
            font-family: 'Segoe UI', Roboto, Arial, sans-serif;
            color: #333;
            line-height: 1.5;
            margin: 0;
            padding: 0;
        }
        .page {
            height: 267mm;
            page-break-after: always;
            position: relative;
        }
        h1 {
            color: #1a5f7a;
            border-bottom: 2px solid #1a5f7a;
            padding-bottom: 5px;
            font-size: 20pt;
            text-align: center;
            text-transform: uppercase;
        }
        h2 {
            color: #2c3e50;
            background-color: #f2f5f8;
            padding: 5px 10px;
            font-size: 15pt;
            border-left: 5px solid #1a5f7a;
            margin-top: 20pt;
        }
        h3 {
            color: #1a5f7a;
            font-size: 12pt;
            margin-top: 15pt;
            text-decoration: underline;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15pt 0;
            font-size: 10pt;
        }
        th {
            background-color: #1a5f7a;
            color: white;
            padding: 8px;
            text-align: left;
        }
        td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .formula-box {
            background-color: #fcfcfc;
            border: 1px dashed #bbb;
            padding: 10px;
            margin: 10px 0;
            font-family: "Courier New", Courier, monospace;
            font-weight: bold;
        }
        .important {
            color: #c0392b;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="page">
    <h1>Geometria Anal&iacute;tica: Resum Te&ograve;ric (I)</h1>

    <h2>1. Equacions de la Recta i del Pla</h2>

    <h3>A. La Recta (r)</h3>
    <p>Determinada per un punt P(x&#8320;, y&#8320;, z&#8320;) i un vector director v(v&#8321;, v&#8322;, v&#8323;).</p>
    <ul>
        <li><strong>Vectorial:</strong> (x, y, z) = (x&#8320;, y&#8320;, z&#8320;) + &lambda;(v&#8321;, v&#8322;, v&#8323;)</li>
        <li><strong>Param&egrave;trica:</strong> x = x&#8320; + &lambda;v&#8321;; y = y&#8320; + &lambda;v&#8322;; z = z&#8320; + &lambda;v&#8323;</li>
        <li><strong>Cont&iacute;nua:</strong> (x-x&#8320;)/v&#8321; = (y-y&#8320;)/v&#8322; = (z-z&#8320;)/v&#8323;</li>
        <li><strong>Impl&iacute;cita:</strong> Intersecci&oacute; de dos plans Ax + By + Cz + D = 0 i A'x + B'y + C'z + D' = 0.</li>
    </ul>

    <h3>B. El Pla (&pi;)</h3>
    <p>Determinat per un punt P i un vector normal n(A, B, C) o dos vectors directors u i v.</p>
    <ul>
        <li><strong>Equaci&oacute; General (Impl&iacute;cita):</strong> Ax + By + Cz + D = 0. On el vector normal &eacute;s n = (A, B, C).</li>
        <li><strong>Producte Vectorial:</strong> Si tenim dos vectors directors u i v, el normal &eacute;s n = u &times; v.</li>
    </ul>

    <h2>2. C&agrave;lcul d'Angles (&alpha;)</h2>
    <div class="formula-box">
        1. Entre dues rectes (u, v): cos &alpha; = |u &middot; v| / (|u| &middot; |v|)<br>
        2. Entre recta i pla (v, n): sin &alpha; = |v &middot; n| / (|v| &middot; |n|)<br>
        3. Entre dos plans (n&#8321;, n&#8322;): cos &alpha; = |n&#8321; &middot; n&#8322;| / (|n&#8321;| &middot; |n&#8322;|)
    </div>

    <h2>3. Notes Importants</h2>
    <p>&bull; <strong>Recta de tall entre plans:</strong> El seu vector director es troba fent v = n&#8321; &times; n&#8322;.</p>
    <p>&bull; <strong>Vectors directors de plans:</strong> Si el pla &eacute;s Ax + By + Cz + D = 0, qualsevol vector (u&#8321;, u&#8322;, u&#8323;) tal que A&middot;u&#8321; + B&middot;u&#8322; + C&middot;u&#8323; = 0 &eacute;s director.</p>
</div>

<div class="page">
    <h1>Geometria Anal&iacute;tica: Posicions Relatives (II)</h1>

    <h2>1. Dues Rectes (r i s)</h2>
    <p>Estudiem el rang de la matriu M=(u, v) i la matriu ampliada M'=(u, v, PQ).</p>
    <table>
        <tr>
            <th>Posici&oacute;</th>
            <th>Rang M</th>
            <th>Rang M'</th>
            <th>Descripci&oacute;</th>
        </tr>
        <tr>
            <td>Coincidents</td>
            <td>1</td>
            <td>1</td>
            <td>Mateixa recta, mateix vector.</td>
        </tr>
        <tr>
            <td>Paral&middot;leles</td>
            <td>1</td>
            <td>2</td>
            <td>Mateix vector, no punts comuns.</td>
        </tr>
        <tr>
            <td>Secants</td>
            <td>2</td>
            <td>2</td>
            <td>Es tallen en un punt.</td>
        </tr>
        <tr>
            <td>Es creuen</td>
            <td>2</td>
            <td>3</td>
            <td>No paral&middot;leles, no es tallen.</td>
        </tr>
    </table>

    <h2>2. Dos Plans (&pi;&#8321; i &pi;&#8322;)</h2>
    <p>Mirem la proporci&oacute;: A/A' = B/B' = C/C' = D/D'</p>
    <table>
        <tr>
            <th>Posici&oacute;</th>
            <th>Condici&oacute;</th>
            <th>Rang M / M'</th>
        </tr>
        <tr>
            <td>Coincidents</td>
            <td>Totes les proporcions iguals</td>
            <td>1 / 1</td>
        </tr>
        <tr>
            <td>Paral&middot;lels</td>
            <td>A/A' = B/B' = C/C' &ne; D/D'</td>
            <td>1 / 2</td>
        </tr>
        <tr>
            <td>Secants</td>
            <td>Vectors no proporcionals</td>
            <td>2 / 2</td>
        </tr>
    </table>

    <h2>3. Tres Plans</h2>
    <p>S'estudia el sistema de 3 equacions amb 3 inc&ograve;gnites:</p>
    <ul>
        <li><strong>SCD (R=3, R'=3):</strong> Es tallen en un <strong>punt &uacute;nic</strong>.</li>
        <li><strong>SCI (R=2, R'=2):</strong> Es tallen en una <strong>recta</strong> (poden ser plans d'un feix).</li>
        <li><strong>SI (R &lt; R'):</strong> No hi ha punts comuns. Poden formar un <strong>prisma</strong> (talls 2 a 2).</li>
    </ul>

    <p class="important" style="text-align: center; margin-top: 30px;">Recorda sempre comprovar si els vectors s&oacute;n proporcionals abans de fer c&agrave;lculs complexos!</p>
</div>

</body>
</html>
"""

HTML(string=html_content).write_pdf("geometria_analitica_resum.pdf")
print("PDF generat correctament: geometria_analitica_resum.pdf")
