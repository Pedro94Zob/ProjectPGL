cd /home/pedroelmordjenne/ProjectPGL
# Lire le fichier data.csv pour obtenir le prix d'ouverture et de clôture
opening=$(head -n 1 data.csv | cut -d',' -f2)
closing=$(tail -n 1 data.csv | cut -d',' -f2)

# Calculer une volatilité approximative (écart entre ouverture et clôture)
volatilite=$(echo "$closing - $opening" | bc -l)

# Obtenir la date et l'heure actuelles pour nommer le rapport
current_date=$(date "+%Y-%m-%d_%H-%M-%S")
report_file="report_${current_date}.txt"

# Générer le rapport
echo "Rapport du $(date '+%Y-%m-%d %H:%M:%S')" > "$report_file"
echo "Prix d'ouverture : ${opening}" >> "$report_file"
echo "Prix de clôture : ${closing}" >> "$report_file"
echo "Volatilité (approximative) : ${volatilite}" >> "$report_file"

# Ajouter, commit et pousser le rapport sur GitHub
git add "$report_file"
git commit -m "Ajout du rapport quotidien: ${current_date}"
git push origin main
