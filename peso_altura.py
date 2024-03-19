peso = float(input("Informe seu peso: "))
altura  = float(input("Informe sua altura: "))

if peso <= 60 and altura < 1.20:
  print("Classificação A!","\n" , "Peso: ", peso, "kilos", "\n", "Altura: ", altura, "metros")
if peso <= 60 and altura >= 1.20 and altura <=1.70:
  print("Classificação B!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso <= 60 and altura > 1.70:
  print("Classificação C!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso > 60 and peso <= 90 and altura < 1.20:
  print("Classificação D!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso > 60 and peso <= 90 and altura >= 1.20 and altura <= 1.70:
  print("Classificação E!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso > 60 and peso <= 90 and altura > 1.70:
  print("Classificação F!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso > 90 and altura < 1.20:
  print("Classificação G!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso > 90 and altura >= 1.20 and altura <= 1.70:
  print("Classificação H!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
if peso >  90 and altura > 1.70:
  print("Classificação I!","\n" , "Peso: ", peso, "\n", "Altura: ", altura)
