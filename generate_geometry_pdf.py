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
    <h1>Geometria Anal\u00edtica: Resum Te\u00f2ric (I)</h1>

    <h2>1. Equacions de la Recta i del Pla</h2>

    <h3>A. La Recta (r)</h3>
    <p>Determinada per un punt P(x\u2080, y\u2080, z\u2080) i un vector director v(v\u2081, v\u2082, v\u2083).</p>
    <ul>
        <li><strong>Vectorial:</strong> (x, y, z) = (x\u2080, y\u2080, z\u2080) + \u03bb(v\u2081, v\u2082, v\u2083)</li>
        <li><strong>Param\u00e8trica:</strong> x = x\u2080 + \u03bbv\u2081; y = y\u2080 + \u03bbv\u2082; z = z\u2080 + \u03bbv\u2083</li>
        <li><strong>Cont\u00ednua:</strong> (x-x\u2080)/v\u2081 = (y-y\u2080)/v\u2082 = (z-z\u2080)/v\u2083</li>
        <li><strong>Impl\u00edcita:</strong> Intersecci\u00f3 de dos plans Ax + By + Cz + D = 0 i A'x + B'y + C'z + D' = 0.</li>
    </ul>

    <h3>B. El Pla (\u03c0)</h3>
    <p>Determinat per un punt P i un vector normal n(A, B, C) o dos vectors directors u i v.</p>
    <ul>
        <li><strong>Equaci\u00f3 General (Impl\u00edcita):</strong> Ax + By + Cz + D = 0. On el vector normal \u00e9s n = (A, B, C).</li>
        <li><strong>Producte Vectorial:</strong> Si tenim dos vectors directors u i v, el normal \u00e9s n = u \u00d7 v.</li>
    </ul>

    <h2>2. C\u00e0lcul d'Angles (\u03b1)</h2>
    <div class="formula-box">
        1. Entre dues rectes (u, v): cos \u03b1 = |u \u00b7 v| / (|u| \u00b7 |v|)<br>
        2. Entre recta i pla (v, n): sin \u03b1 = |v \u00b7 n| / (|v| \u00b7 |n|)<br>
        3. Entre dos plans (n\u2081, n\u2082): cos \u03b1 = |n\u2081 \u00b7 n\u2082| / (|n\u2081| \u00b7 |n\u2082|)
    </div>

    <h2>3. Notes Importants</h2>
    <p>\u2022 <strong>Recta de tall entre plans:</strong> El seu vector director es troba fent v = n\u2081 \u00d7 n\u2082.</p>
    <p>\u2022 <strong>Vectors directors de plans:</strong> Si el pla \u00e9s Ax + By + Cz + D = 0, qualsevol vector (u\u2081, u\u2082, u\u2083) tal que A\u00b7u\u2081 + B\u00b7u\u2082 + C\u00b7u\u2083 = 0 \u00e9s director.</p>
</div>

<div class="page">
    <h1>Geometria Anal\u00edtica: Posicions Relatives (II)</h1>

    <h2>1. Dues Rectes (r i s)</h2>
    <p>Estudiem el rang de la matriu M=(u, v) i la matriu ampliada M'=(u, v, PQ).</p>
    <table>
        <tr>
            <th>Posici\u00f3</th>
            <th>Rang M</th>
            <th>Rang M'</th>
            <th>Descripci\u00f3</th>
        </tr>
        <tr>
            <td>Coincidents</td>
            <td>1</td>
            <td>1</td>
            <td>Mateixa recta, mateix vector.</td>
        </tr>
        <tr>
            <td>Paral\u00b7leles</td>
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
            <td>No paral\u00b7leles, no es tallen.</td>
        </tr>
    </table>

    <h2>2. Dos Plans (\u03c0\u2081 i \u03c0\u2082)</h2>
    <p>Mirem la proporci\u00f3: A/A' = B/B' = C/C' = D/D'</p>
    <table>
        <tr>
            <th>Posici\u00f3</th>
            <th>Condici\u00f3</th>
            <th>Rang M / M'</th>
        </tr>
        <tr>
            <td>Coincidents</td>
            <td>Totes les proporcions iguals</td>
            <td>1 / 1</td>
        </tr>
        <tr>
            <td>Paral\u00b7lels</td>
            <td>A/A' = B/B' = C/C' \u2260 D/D'</td>
            <td>1 / 2</td>
        </tr>
        <tr>
            <td>Secants</td>
            <td>Vectors no proporcionals</td>
            <td>2 / 2</td>
        </tr>
    </table>

    <h2>3. Tres Plans</h2>
    <p>S'estudia el sistema de 3 equacions amb 3 inc\u00f2gnites:</p>
    <ul>
        <li><strong>SCD (R=3, R'=3):</strong> Es tallen en un <strong>punt \u00fanic</strong>.</li>
        <li><strong>SCI (R=2, R'=2):</strong> Es tallen en una <strong>recta</strong> (poden ser plans d'un feix).</li>
        <li><strong>SI (R &lt; R'):</strong> No hi ha punts comuns. Poden formar un <strong>prisma</strong> (talls 2 a 2).</li>
    </ul>

    <p class="important" style="text-align: center; margin-top: 30px;">Recorda sempre comprovar si els vectors s\u00f3n proporcionals abans de fer c\u00e0lculs complexos!</p>
</div>

</body>
</html>
"""

HTML(string=html_content).write_pdf("geometria_analitica_resum.pdf")
print("PDF generated: geometria_analitica_resum.pdf")
