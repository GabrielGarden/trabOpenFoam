#!/bin/bash
cd "${0%/*}/logs"

# Gerar gráfico no Gnuplot
echo "Verificando arquivos..."
ls -l ./UxFinalRes_0 ./UyFinalRes_0 ./UzFinalRes_0 ./pFinalRes_0

# Plotagem temporário
cat << EOF > plot_script.gp
set logscale y
set xlabel "Segundos"
set ylabel "Residuos"
set title "Grafico de Residuos FINAL"

set output "Grafico_de_Residuos_FINAL.png"  # Nome do arquivo de saída
set terminal png                      # Formato da imagem (PNG)


plot "./UxFinalRes_0" using 1:2 with lines title "Residuo Ux", \
     "./UyFinalRes_0" using 1:2 with lines title "Residuo Uy", \
     "./UzFinalRes_0" using 1:2 with lines title "Residuo Uz", \
     "./pFinalRes_0" using 1:2 with lines title "Residuo p"
EOF

# Rodar o gnuplot
gnuplot plot_script.gp

# Removendo temporário após a execução
rm plot_script.gp
cd .. || exit 1
echo "Gráfico gerado e salvo como Grafico_de_Residuos_FINAL.png"

