library(sf)
library(plotly)
library(shiny)
library(maps)

# Charger les données de séismes
seismes <- read.csv("/Users/33784/Desktop/Projet Math/seismes_2014.csv", stringsAsFactors = FALSE)

# Échantillonner les données pour réduire le nombre de marqueurs affichés
sampled_seismes <- seismes[sample(nrow(seismes), 1000), ]

# Convertir les données en coordonnées sphériques
sampled_seismes$phi <- (90 - sampled_seismes$lat) * pi / 180
sampled_seismes$theta <- (360 - sampled_seismes$lon) * pi / 180
sampled_seismes$r <- sampled_seismes$mag * 200000 # Définir une échelle pour les marqueurs en fonction de la magnitude

# Charger les données géographiques des pays
map_data <- map_data("world")

# Filtrer les données pour afficher uniquement les pays
countries <- unique(map_data$region)

# Créer une palette de couleurs fluo
color_palette <- c("#FF00FF", "#00FFFF", "#FFFF00", "#00FF00", "#FF0000")

# Définir l'interface utilisateur
ui <- fluidPage(
  titlePanel("Séismes dans le monde en 2014"),
  plotlyOutput("globe")
)

# Définir le serveur
server <- function(input, output) {
  
  # Créer un globe terrestre avec les données échantillonnées
  output$globe <- renderPlotly({
    plot_geo() %>%
      add_trace(
        type = "scattergeo", mode = "markers", lon = sampled_seismes$lon, lat = sampled_seismes$lat,
        marker = list(
          color = sampled_seismes$mag,
          colorscale = list(list(0, color_palette[1]), list(1, color_palette[5])),
          size = sampled_seismes$r,
          sizemode = "diameter",
          sizeref = 100000
        ),
        text = paste("Magnitude:", sampled_seismes$mag, "<br>",
                     "Date:", sampled_seismes$date, "<br>",
                     "Latitude:", sampled_seismes$lat, "<br>",
                     "Longitude:", sampled_seismes$lon)
      ) %>%
      layout(
        geo = list(
          showframe = FALSE,
          showcoastlines = TRUE,
          showland = TRUE,
          showocean = FALSE,
          landcolor = "black",
          coastlinecolor = "white",
          projection = list(type = "orthographic", rotation = list(lon = -60, lat = 30))
        )
      )
  })
}

# Lancer l'application Shiny
shinyApp(ui = ui, server = server)