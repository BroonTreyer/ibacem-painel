# -*- coding: utf-8 -*-
import base64, pathlib
HERE = pathlib.Path(__file__).parent
html = (HERE/"dash-frutas.html").read_text(encoding="utf-8")

logo = base64.b64encode((HERE/"ibacem-logo.png").read_bytes()).decode("ascii")
video = base64.b64encode((HERE/"ibacem-intro.mp4").read_bytes()).decode("ascii")

html = html.replace("__LOGO__", "data:image/png;base64," + logo)
html = html.replace("__VIDEO__", "data:video/mp4;base64," + video)

out = HERE/"dash-ibacem.html"
out.write_text(html, encoding="utf-8")
print("gerado:", out.name, "| tamanho:", round(len(html)/1024/1024,2), "MB")
