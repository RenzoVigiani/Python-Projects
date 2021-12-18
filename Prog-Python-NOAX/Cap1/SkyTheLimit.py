# Instalamos las biblioteca que emplearemos (Yahoo Finance, Google Translator)
#pip install itranslate yfinance

# Cargamos la bibliotecas que emplearemos en este programa
from itranslate import itranslate as itrans
from PIL import Image
import requests
import yfinance as yf

def add_linebreaks (s, col_width = 120):
  """
  Formatea una cadena de texto añadiendo saltos de línea cada
  cierto número de caracteres. Además, garantiza que el salto
  siempre se produzca en un espacio (para evitar cortar palabras)
  :param s: la cadena que se desea formatear.
  :param col_width: el ancho deseado de columna.
  :return: la cadena formateada.
  """
  s_out = ""
  break_at_next_space = False
  for i in range(len(s)):
    if (i+1) % col_width == 0:
      break_at_next_space = True
    if break_at_next_space and s[i] == ' ':
      s_out += "\n"
      break_at_next_space = False
    else:
      s_out += s[i]
  return s_out


# Solicita al usuario el periodo de consulta
print("Introduzca el periodo para el que quiere consultar la variación.")
print("Las opciones válidas son 'Y' (año), 'M' (mes), 'D' (día): ")
valid_options = {
    'Y': ('y', 'año'), 
    'M': ('mo', 'mes'), 
    'D': ('d', 'día')
}
option = input()
while option.upper() not in valid_options.keys():
  print("La opción introducida no es válida.")
  option = input("Las opciones válidas son 'Y' (año), 'M' (mes), 'D' (día): ")

# Extraemos algunos de los tickers más populares
tickers = yf.Tickers("AAPL MSFT AMZN TSLA")

# Recorremos los tickers 
for ticker in tickers.tickers.values():
  # Descarga y muestra el logotipo de la empresa
  im = Image.open(requests.get(ticker.info['logo_url'], stream=True).raw)
  im.show()
  
  # Imprime el nombre completo de la empresa y el exchange
  print(f"{ticker.info['longName']} ({ticker.info['exchange']})")

  # Traduce la descripción de la empresa al español
  summary = itrans(ticker.info['longBusinessSummary'], to_lang='es')
  summary = add_linebreaks(summary)
  print(summary)
  print()

  # Extrae el histórico de valores de la compañía
  # El intervalo es de un minuto para variación intradía, 
  # o de un día para variación mensual o anual.
  period_code, period_name = valid_options[option.upper()]
  if period_code == 'd':
    interval = '1m'
  else:
    interval = '1d'
  values = ticker.history(period=f"1{period_code}", interval=interval).Close

  # Calculamos la tasa de variación
  pct = 100 * (values[-1] - values[0]) / values[0]

  # El precio actual es mayor que al inicio del periodo: la acción ha subido
  if pct > 0:
    print(f"El precio de la acción ha subido un {pct:.2f}% en el último {period_name}.")

  # El precio actual es menor que al inicio del periodo: la acción ha bajado
  elif pct < 0:
    print(f"El precio de la acción ha bajado un {-pct:.2f}% en el último {period_name}.")
  
  # El precio no ha variado.
  else:
    print(f"El precio de la acción se ha mantenido en el último {period_name}")

  # Imprime un par de líneas en blanco antes de pasar al siguiente ticker
  print("\n\n")